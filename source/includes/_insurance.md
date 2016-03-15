# Insurance Companies
> Get the insurance company with id 1

```python
response = requests.get(API_ROOT + 'insurance_companies/1/')
company = response.json()
printj(company)
```

```http
GET /api/v1.5/insurance_companies/1/ HTTP/1.1
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
Date: Tue, 15 Mar 2016 12:55:11 GMT
X-Frame-Options: DENY
Content-Type: application/json
```

Available commands:

`POST /api/v1.5/insurance_companies/` - for admins only

`GET /api/v1.5/insurance_companies/{id}/`

`GET /api/v1.5/insurance_companies/`

Complete company data, as returned by the API:

```json
{
    "id": 1,
    "is_dental": false,
    "is_medical": false,
    "is_vision": true,
    "name": "VSP",
    "url": "http://api-staging.bauxy.com/api/v1.5/insurance_companies/1/"
}
```

JSON Parameter name | Value                  | Required
------------------- | ---------------------- | --------
name                | Insurance company name | True
is_vision           | Boolean                | False
is_medical          | Boolean                | False
is_dental           | Boolean                | False

We develop custom processes to ensure maximal claim acceptance rates at every supported insurance company. However, this means that we cannot allow outside users to add companies. If you represent an insurance company and would like us to add support, please reach out to us at [info@bauxy.com](mailto:info@bauxy.com)!
