# Addresses

Available commands:

`POST /api/v1.5/addresses/`

`GET|PUT|PATCH /api/v1.5/addresses/{id}/`

Minimum data required to create an address:

JSON Parameter name | Value | Required
--------------------|-------|---------
line1 | Address | True
line2 | Address | False
zipcode | zip  code | True
state | 2-letter state code name | True

The `POST` command will accept `JSON` body in the request, like in the example on the right.

```json
{
    "line1" : "...",
    "city"  : "...",
    "zipcode" : "...",
    "state" : "..."
}
```