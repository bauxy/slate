# Bills
> GET a bill

```python
response = requests.get(API_ROOT + 'bills/10/', auth=user)
printj(response.json())
```

```http
GET /api/v1.5/bills/10/ HTTP/1.1
Host: api-staging.bauxy.com
Connection: keep-alive
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Basic cGV0ZXI6MXFheg==
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
Date: Tue, 15 Mar 2016 14:58:56 GMT
X-Frame-Options: DENY
Content-Type: application/json
```

```json
{
    "final_cost": 0,
    "generated_bill_image": null,
    "id": 10,
    "insurance": "http://api-staging.bauxy.com/api/v1.5/insurance_companies/1/",
    "is_bill_generated": false,
    "items": [],
    "original_bill_image": "https://bauxy-aptible-bucket-test.s3.amazonaws.com/bauxy-aptible-bucket-test/test_image.jpg",
    "patient": "http://api-staging.bauxy.com/api/v1.5/patients/5/",
    "payment_method": null,
    "provider": null,
    "purchase_date": null,
    "shipping_cost": null,
    "total_cost": 0,
    "total_discount": null,
    "total_discount_type": null,
    "transaction_no": null,
    "url": "http://api-staging.bauxy.com/api/v1.5/bills/10/"
}
```

> POST a bill

```python
data = {
    'patient'   : "http://api-staging.bauxy.com/api/v1.5/patients/87/",
    'insurance' : "http://api-staging.bauxy.com/api/v1.5/insurance_companies/1/",
    'provider'  : "http://api-staging.bauxy.com/api/v1.5/providers/3/"
}
response = requests.post(API_ROOT + 'bills/', auth=user, data=data)
printj(response.json())
```

```http
POST /api/v1.5/bills/ HTTP/1.1
Host: api-staging.bauxy.com
Content-Length: 237
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.9.1
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Authorization: Basic cGV0ZXI6MXFheg==

patient=http%3A%2F%2Fapi-staging.bauxy.com%2Fapi%2Fv1.5%2Fpatients%2F87%2F&insurance=http%3A%2F%2Fapi-staging.bauxy.com%2Fapi%2Fv1.5%2Finsurance_companies%2F1%2F&provider=http%3A%2F%2Fapi-staging.bauxy.com%2Fapi%2Fv1.5%2Fproviders%2F3%2F
HTTP/1.1 201 Created
x-xss-protection: 1; mode=block
x-content-type-options: nosniff
Transfer-Encoding: chunked
Vary: Accept, Cookie
Server: nginx/1.9.2
Connection: keep-alive
Location: http://api-staging.bauxy.com/api/v1.5/bills/13/
Allow: GET, POST, HEAD, OPTIONS
Date: Tue, 15 Mar 2016 15:06:05 GMT
X-Frame-Options: DENY
Content-Type: application/json
```

```json
{
    "final_cost": 0,
    "generated_bill_image": null,
    "id": 13,
    "insurance": "http://api-staging.bauxy.com/api/v1.5/insurance_companies/1/",
    "is_bill_generated": false,
    "items": [],
    "original_bill_image": null,
    "patient": "http://api-staging.bauxy.com/api/v1.5/patients/87/",
    "payment_method": null,
    "provider": "http://api-staging.bauxy.com/api/v1.5/providers/3/",
    "purchase_date": null,
    "shipping_cost": null,
    "total_cost": 0,
    "total_discount": null,
    "total_discount_type": null,
    "transaction_no": null,
    "url": "http://api-staging.bauxy.com/api/v1.5/bills/13/"
}
```

Available commands:

`POST /api/v1.5/bills/`

`GET /api/v1.5/bills/{id}/`

`POST /api/v1.5/bills/{id}/`

`PATCH /api/v1.5/bills/{id}/`

Request parameters, specified in the `POST` body of an HTTP request

JSON parameter names | Value                             | Required
-------------------- | --------------------------------- | --------
patient              | url of patient object             | True
insurance            | url of insurance company          | True
provider             | url of provider object            | True
purchase_date        | ISO-8601 datetime                 | False
transaction_no       | int                               | False
total_discount       | Float                             | False
total_discount_type  | `Percent` or `Value`              | False
shipping_cost        | Float                             | False
payment_method       | `CASH` or `CREDIT`                | False
generated_bill_image | url to a bill image               | False
is_bill_generated    | Boolean                           | False
original_bill_image  | File (as in multi-part form data) | True

<aside class="warning">
Sometimes one may desire to just delegate all responsibility away. We support that! Specifically, one may input only minimal information into our database and have us take care of everything else, so long as an image of the original bill is in our database. In that case, our team of experts will go over the image and handle all the data processing. Be aware that as this requires human intervention, it will slow processing somewhat. <br /><br />If the image quality is poor or not all necessary information is present on the bill, we may not be able to continue processing the claim. Whether or not the process is successful, additional costs will be incurred.
</aside>

<aside class="notice">
Best practice for users who wish to minimize cost is to provide enough data to create a bill whenever possible, instead of providing only minimal data.
</aside>
