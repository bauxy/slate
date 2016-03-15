# Healthcare Providers
> GET a provider:

```python
response = requests.get(API_ROOT + 'providers/3/')
printj(response.json())
```

```http
GET /api/v1.5/providers/3/ HTTP/1.1
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
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Date: Tue, 15 Mar 2016 14:46:45 GMT
X-Frame-Options: DENY
Content-Type: application/json
```

```json
{
    "address": {
        "city": "San Francisco",
        "id": 2,
        "line1": "995 Market St",
        "line2": "",
        "url": "http://api-staging.bauxy.com/api/v1.5/addresses/2/",
        "zipcode": "94103"
    },
    "email": "gleb+jins@bauxy.com",
    "id": 3,
    "name": "JINS",
    "phone_number": "0987654321",
    "url": "http://api-staging.bauxy.com/api/v1.5/providers/3/",
    "user": {
        "email": "gleb@bauxy.com",
        "id": 1,
        "is_staff": true,
        "url": "http://api-staging.bauxy.com/api/v1.5/users/1/",
        "username": "bauxyadmin"
    }
}
```

Available commands:

`POST /api/v1.5/providers/`

`GET|PUT|PATCH|POST /api/v1.5/providers/{id}/`

JSON Parameter name | Value                     | Required
------------------- | ------------------------- | --------
user                | url of user login account | False
name                | String - e.g., Mike Tyson | True
email               | unique email address      | True
phone_number        | +999999999                | False
address             | url of address object     | False
tax_id              | String                    | True
