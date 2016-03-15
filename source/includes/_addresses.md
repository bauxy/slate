# Addresses
> GET an address

```python
response = requests.get(API_ROOT + 'addresses/2/', auth=user)
printj(response.json())
```

```http
GET /api/v1.5/addresses/2/ HTTP/1.1
Host: api-staging.bauxy.com
Connection: keep-alive
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
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
Date: Tue, 15 Mar 2016 15:34:58 GMT
X-Frame-Options: DENY
Content-Type: application/json
```

```json
{
    "city": "San Francisco",
    "id": 2,
    "line1": "995 Market St",
    "line2": "",
    "url": "http://api-staging.bauxy.com/api/v1.5/addresses/2/",
    "zipcode": "94103"
}
```

Available commands:

`POST /api/v1.5/addresses/`

`GET|PUT|PATCH /api/v1.5/addresses/{id}/`

Minimum data required to create an address:

JSON Parameter name | Value                    | Required
------------------- | ------------------------ | --------
line1               | Address                  | True
line2               | Address                  | False
zipcode             | zip  code                | True
state               | 2-letter state code name | True
