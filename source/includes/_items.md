# Items

Available commands:

`POST /api/v1.5/items/`

`GET|PUT|PATCH|POST /api/v1.5/items/{id}/`

Complete item data, as returned by the API:

``` json
{
    "bill" : "URL for the bill to which this Item is attached",
    "item_type" : "coating | frame | exam | lens_contact | lens_single | lens_bifocal | lens_trifocal | lens_progressive | null",
    "quantity" : "number | null",
    "name" : "... | null",
    "cost" : "number | null",
    "discount" : "number | null",
    "discount_type" : "Percent | Value | null",
    "created_at" : "ISO-8601 datetime",
    "updated_at" : "ISO-8601 datetime",
    "deleted_at" : "ISO-8601 datetime"
}
```

JSON Parameter name | Value | Required
--------------------|-------|---------
bill | bill id url | True
item_type | `coating`, `frame`, `exam`, `lens_contact`, `lens_single`, `lens_bifocal`, `lens_trifocal`, `lens_progressive` | True
quantity | Integer | True
name | String | True
cost | Float | True
discount | Float | False
discount_type | `Percent`, `Value` | False