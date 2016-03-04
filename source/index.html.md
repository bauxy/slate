---
title: Bauxy API Reference
language_tabs:
  - http: HTTP
  - python: Python
toc_footers:
  - "<a href='#'>Sign Up for a Developer Key</a>"
  - "<a href='https://github.com/tripit/slate'>Documentation Powered by Slate</a>"
includes:
  - errors
search: true
---

# Introduction
Welcome to the Bauxy API!

The Bauxy API 1.5 is a RESTful service helping patients get reimbursed for out-of-network insurance claims with minimal overhead.

Healthcare providers can sign up and route their patients through the service automatically, making it easy for patients to receive their claim even if the provider isn't in the patient's insurance network.

We have usagse examples in raw HTTP and Python. You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right. As you can see, when using Python, we recommend the use of the excellent [Requests](http://docs.python-requests.org/en/master/) package.

## Fundamentals of usage
> Get a list of API endpoints

```http
GET /api/{version}/
```

```python
import requests
r = requests.get(API_ROOT)
r.json()
```

The API provides a number of endpoints, the list of which may be retrieved by querying the API root: These endpoints have standardized behavior: in general, the following operations are supported.

> List of items to which the authenticated user has access:

```
GET /api/{version}/{endpoint}/
```

> Given appropriate data, create a new item:

```
POST /api/{version}/{endpoint}/
```

> Given appropriate data, replace the item with the given id:

```
PUT /api/{version}/{endpoint}/{id}/ -> given appropriate JSON data, replace the item with the given id
```

> Given appropriate partial JSON data, update the specified item

```
PATCH /api/{version}/{endpoint}/{id}/
```

> Remove the specified item

```
DELETE /api/{version}/{endpoint}/{id}/ -> remove the item with the given id.
```

Naturally, users may only modify or delete resources which they own.

## Expert Assistance
Sometimes one may desire to just delegate all responsibility away. We support that! Specifically, one may input only minimal information into our database and have us take care of everything else, so long as an image of the original bill is in our database. In that case, our team of experts will go over the image and handle all the data processing. Be aware that as this requires human intervention, it will slow processing somewhat. If the image quality is poor or not all necessary information is present on the bill, we may not be able to continue processing the claim. Whether or not the process is successful, additional costs will be incurred.

## Notes on Incomplete Data
Best practice for users who wish to minimize cost is to provide enough data to create a bill whenever possible, instead of providing only minimal data.

# Authentication
<aside class="warning">
TODO: How exactly do we authenticate, anyway? API key, login/token, basic, something else?
</aside>

# Overview
# Kittens
## Get All Kittens

```ruby
require 'kittn'

api = Kittn::APIClient.authorize!('meowmeowmeow')
api.kittens.get
```

```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.get()
```

```shell
curl "http://example.com/api/kittens"
  -H "Authorization: meowmeowmeow"
```

> The above command returns JSON structured like this:

```json
[
  {
    "id": 1,
    "name": "Fluffums",
    "breed": "calico",
    "fluffiness": 6,
    "cuteness": 7
  },
  {
    "id": 2,
    "name": "Max",
    "breed": "unknown",
    "fluffiness": 5,
    "cuteness": 10
  }
]
```

This endpoint retrieves all kittens.

### HTTP Request
`GET http://example.com/api/kittens`

### Query Parameters

Parameter    | Default | Description
------------ | ------- | --------------------------------------------------------------------------------
include_cats | false   | If set to true, the result will also include cats.
available    | true    | If set to false, the result will include kittens that have already been adopted.

<aside class="success">
Remember — a happy kitten is an authenticated kitten!
</aside>

## Get a Specific Kitten

```ruby
require 'kittn'

api = Kittn::APIClient.authorize!('meowmeowmeow')
api.kittens.get(2)
```

```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.get(2)
```

```shell
curl "http://example.com/api/kittens/2"
  -H "Authorization: meowmeowmeow"
```

> The above command returns JSON structured like this:

```json
{
  "id": 2,
  "name": "Max",
  "breed": "unknown",
  "fluffiness": 5,
  "cuteness": 10
}
```

This endpoint retrieves a specific kitten.
<aside class="warning">Inside HTML code blocks like this one, you can't use Markdown, so use <code>&lt;code&gt;</code> blocks to denote code.</aside>

### HTTP Request
`GET http://example.com/kittens/<ID>`

### URL Parameters

Parameter | Description
--------- | --------------------------------
ID        | The ID of the kitten to retrieve
