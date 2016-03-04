# Bills
`bills/` endpoint: describes a bill from a healthcare provider to an insurance company based on services rendered to a patient.

> Minimum data required to create a bill:

```json
{
    "patient" : "URL of a patient object",
    "insurance": "URL of an insurance company object"
}
```

> Complete bill data, as returned by the API:

```json
{
    "patient" : "URL of a patient object",
    "insurance": "URL of an insurance company object",
    "provider": "URL of a healthcare provider object | null",
    "purchase_date": "ISO-8601 datetime | null",
    "transaction_no": "..." | null,
    "total_discount": number | null,
    "total_discount_type": "Percent" | "Value" | null,
    "shipping_cost": number | null,
    "payment_method" : "CASH" | "CREDIT" | null,
    "created_at" : "ISO-8601 datetime",
    "updated_at" : "ISO-8601 datetime",
    "deleted_at" : "ISO-8601 datetime | null",
    "generated_bill_image": "URL | null",
    "is_bill_generated" : true | false,
    "original_bill_image" : "URL | null",
    "items" : [URL of an item object, ...]
}
```

> In order to create a claim or invoice, more data is required than is required to create a bill. Specifically, the following fields may not be null in that case:

```json
{
    "patient" : "URL of a patient object",
    "insurance": "URL of an insurance company object",
    "provider": "URL of a healthcare provider object",
    "purchase_date": "ISO-8601 datetime"
}
```
