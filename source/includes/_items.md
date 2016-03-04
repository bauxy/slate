# Items
`items/` endpoint: describes particular line items from a bill.

> Minimum data required to create an item:

```json
{
    "bill" : "URL for the bill to which this Item is attached",
}
```

> Complete item data, as returned by the API:

```json
{
    "bill" : "URL for the bill to which this Item is attached",
    "item_type" : "coating" | "frame" | "exam" | "lens_contact" | "lens_single" | "lens_bifocal" | "lens_trifocal" | "lens_progressive" | null
    "quantity" : number | null,
    "name" : "..." | null,
    "cost" : number | null,
    "discount" : number | null,
    "discount_type" : "Percent" | "Value" | null,
    "created_at" : "ISO-8601 datetime",
    "updated_at" : "ISO-8601 datetime",
    "deleted_at" : "ISO-8601 datetime",
}
```

> In order to create a claim or invoice, more data is required than is required to create an item. Specifically, the following fields may not be null in that case:

```json
{
    "bill" : "URL for the bill to which this Item is attached",
    "item_type" : "coating" | "frame" | "exam" | "lens_contact" | "lens_single" | "lens_bifocal" | "lens_trifocal" | "lens_progressive" | null
    "quantity" : number | null,
    "name" : "..." | null,
    "cost" : number | null,
}
```
