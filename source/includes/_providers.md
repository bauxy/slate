# Healthcare Providers

Available commands:

`POST /api/v1.5/providers/`

`GET|PUT|PATCH|POST /api/v1.5/providers/{id}/`

Complete provider data, as returned by the API:

```json
{
    "user" : "URL of a User login account",
    "name" : "... | null",
    "email" : "must.be@unique.and.valid",
    "phone_number" : "+999999999 | null",
    "address" : "URL of an Address | null",
    "tax_id" : "...",
    "created_at" : "ISO-8601 datetime",
    "updated_at" : "ISO-8601 datetime",
    "deleted_at" : "ISO-8601 datetime"
}
```

JSON Parameter name | Value | Required
--------------------|-------|---------
user | url of user login account | False
name | String - e.g., Mike Tyson | True
email | unique email address | True
phone_number | +999999999 | False
address | url of address object | False
tax_id | String | True
