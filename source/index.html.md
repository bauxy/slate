---
title: Bauxy API Reference
language_tabs:
  - python: Python
  - http: HTTP
toc_footers:
  - "<a href='#'>Sign Up for a Provider Key</a>"
  - "<a href='https://github.com/tripit/slate'>Documentation Powered by Slate</a>"
includes:
  - users
  - insurance
  - patients
  - providers
  - bills
  - items
  - addresses
  - errors
search: true
---

# Introduction
> We'll be setting up a number of examples to follow, all of which follow similar patterns. For brevity, please assume that all code samples are prefixed as follows:

```python
import json
import requests

API_ROOT = 'http://api-staging.bauxy.com/api/v1.5/'

def printj(json_object):
    "Pretty-print a json object"
    print json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))

# This particular username and password doesn't work, for obvious reasons; use your own.
user = ('username', 'password')
```

Welcome to the Bauxy API!

The Bauxy API 1.5 is a RESTful service helping patients get reimbursed for out-of-network insurance claims with minimal overhead.

Healthcare providers can sign up and route their patients through the service automatically, making it easy for patients to receive their claim even if the provider isn't in the patient's insurance network.

We have usage examples in raw HTTP and Python. You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right. As you can see, when using Python, we recommend the use of the excellent [Requests](http://docs.python-requests.org/en/master/) package.

## Overview
The API provides a number of endpoints, the list of which may be retrieved by querying the API root:

  `GET /api/{version}/`

These endpoints have standardized behavior: in general, the following operations are supported on each:

  `GET /api/{version}/{endpoint}/` -> list of items the authenticated user may access

  `POST /api/{version}/{endpoint}/` -> given appropriate JSON data, create a new item

  `PUT /api/{version}/{endpoint}/{id}/` -> given appropriate JSON data, replace the item with the given id

  `PATCH /api/{version}/{endpoint}/{id}/` -> given partial JSON data, update the item with the given id

  `DELETE /api/{version}/{endpoint}/{id}/` -> remove the item with the given id.

Naturally, users may only modify or delete resources which they own.

## Public API
> List API endpoints

```python
response = requests.get(API_ROOT)
actions = response.json()
printj(actions)
```

```http
GET /api/v1.5/ HTTP/1.1
Host: api-staging.bauxy.com
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.9.1


HTTP/1.1 200 OK
x-xss-protection: 1; mode=block
x-content-type-options: nosniff
Content-Encoding: gzip
Transfer-Encoding: chunked
Vary: Accept-Encoding
Vary: Accept, Cookie
Server: nginx/1.9.2
Connection: keep-alive
Allow: GET, HEAD, OPTIONS
Date: Tue, 15 Mar 2016 13:08:53 GMT
X-Frame-Options: DENY
Content-Type: application/json
```

```json
{
    "addresses": "http://api-staging.bauxy.com/api/v1.5/addresses/",
    "bills": "http://api-staging.bauxy.com/api/v1.5/bills/",
    "insurance_companies": "http://api-staging.bauxy.com/api/v1.5/insurance_companies/",
    "items": "http://api-staging.bauxy.com/api/v1.5/items/",
    "patients": "http://api-staging.bauxy.com/api/v1.5/patients/",
    "planinfo": "http://api-staging.bauxy.com/api/v1.5/planinfo/",
    "providers": "http://api-staging.bauxy.com/api/v1.5/providers/",
    "users": "http://api-staging.bauxy.com/api/v1.5/users/"
}
```

`OPTIONS` method is available to all users at all endpoints, so is omitted from the table. All other omitted methods are unimplemented or forbidden.

Table entries indicate whether or not access is permitted to the given user, as follows:
- `none`: no access is permitted to the given user.
- `read`: user may read from this endpoint; `GET`, `HEAD`.
- `filter read`: this user is permitted access to the specified endpoint with the specified method, provided that the resource at that endpoint applies to the user.
- `write`: user may write to this endpoint; `POST` for list endpoints, or `PUT` / `PATCH` / `DELETE` for detail endpoints. `write` on a detail endpoint implies filtering such that the resource at that endpoint applies to the user.

Bauxy staff members have unrestricted access to all endpoints.

All API endpoints live under the API prefix, currently `/api/v1.5/`. This prefix is omitted from the table for brevity but required for API use.

endpoint                   | Unauthenticated | Authenticated
-------------------------- | --------------- | -----------------
`/`                        | read            | read
`users/`                   | none            | filter read
`users/:id/`               | none            | filter read write
`patients/`                | write           | filter read write
`patients/:id/`            | none            | filter read write
`bills/`                   | none            | filter read write
`bills/:id/`               | none            | filter read write
`items/`                   | none            | filter read write
`items/:id/`               | none            | filter read write
`providers/`               | read write      | read
`providers/:id/`           | read            | read write
`insurance_companies/`     | read            | read
`insurance_companies/:id/` | read            | read
`addresses/`               | none            | filter read write
`addresses/:id/`           | none            | filter read write
`planinfo/`                | none            | filter read
`planinfo/:id/`            | none            | filter read

## Private API
The private API is restricted to superusers, all of whom have unrestricted read and write access to all its endpoints.

The private API prefix is `/api/internal/v1.5/`. As above, this prefix is omitted from this chart for brevity but required for API use.
