# Bills

Available commands:

`POST /api/v1.5/bills/`

`GET /api/v1.5/bills/{id}/`

`POST /api/v1.5/bills/{id}/`

`PATCH /api/v1.5/bills/{id}/`

Request parameters, specified in the `POST` body of an HTTP request

```json
{
    "patient" : "URL of a patient object",
    "insurance": "URL of an insurance company object",
    "provider": "URL of a healthcare provider object | null",
    "purchase_date": "ISO-8601 datetime | null",
    "transaction_no": "... | null",
    "total_discount": "number | null",
    "total_discount_type": "Percent | Value | null",
    "shipping_cost": "number | null",
    "payment_method" : "CASH | CREDIT | null",
    "created_at" : "ISO-8601 datetime",
    "updated_at" : "ISO-8601 datetime",
    "deleted_at" : "ISO-8601 datetime | null",
    "generated_bill_image": "URL | null",
    "is_bill_generated" : "true | false",
    "original_bill_image" : "URL | null",
    "items" : "[URL of an item object, ...]"
}
```

JSON parameter names | Value | Required
---------------------|-------|---------
patient | url of patient object | True
insurance | url of insurance company | True
provider | url of provider object | True
purchase_date | ISO-8601 datetime | False
transaction_no | int | False
total_discount | Float | False
total_discount_type | `Percent` or `Value` | False
shipping_cost | Float | False
payment_method | `CASH` or `CREDIT` | False
generated_bill_image | url to a bill image | False
is_bill_generated | Boolean | False
original_bill_image | File (as in multi-part form data) | True

In order to create a bill, `original_bill_image` needs to be sent to the server. Once processed, the server will reply with a `url` pointing to the bill image on Amazon S3.

<aside class="warning">
Sometimes one may desire to just delegate all responsibility away. We support that! Specifically, one may input only minimal information into our database and have us take care of everything else, so long as an image of the original bill is in our database. In that case, our team of experts will go over the image and handle all the data processing. Be aware that as this requires human intervention, it will slow processing somewhat. If the image quality is poor or not all necessary information is present on the bill, we may not be able to continue processing the claim. Whether or not the process is successful, additional costs will be incurred.
</aside>

<aside class="notice">
Best practice for users who wish to minimize cost is to provide enough data to create a bill whenever possible, instead of providing only minimal data.
</aside>