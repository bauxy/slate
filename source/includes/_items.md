# Items
> GET an item

```python
response = requests.get(API_ROOT + 'items/8/', auth=user)
printj(response.json())
```

```http
GET /api/v1.5/items/8/ HTTP/1.1
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
Date: Tue, 15 Mar 2016 15:30:53 GMT
X-Frame-Options: DENY
Content-Type: application/json
```

```json
{
    "bill": "http://api-staging.bauxy.com/api/v1.5/bills/10/",
    "cost": 320.0,
    "discount": 5.0,
    "discount_type": "Percent",
    "final_cost": 304.0,
    "id": 8,
    "item_type": "lens_contact",
    "name": "CatEye green cosmetic shaping lenses",
    "quantity": null,
    "url": "http://api-staging.bauxy.com/api/v1.5/items/8/"
}
```

Available commands:

`POST /api/v1.5/items/`

`GET|PUT|PATCH|POST /api/v1.5/items/{id}/`

Complete item data, as returned by the API:

JSON Parameter name | Value                                                                                                          | Required
------------------- | -------------------------------------------------------------------------------------------------------------- | --------
bill                | bill id url                                                                                                    | True
item_type           | `coating`, `frame`, `exam`, `lens_contact`, `lens_single`, `lens_bifocal`, `lens_trifocal`, `lens_progressive` | True
quantity            | Integer                                                                                                        | True
name                | String                                                                                                         | True
cost                | Float                                                                                                          | True
discount            | Float                                                                                                          | False
discount_type       | `Percent`, `Value`                                                                                             | False
