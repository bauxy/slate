# Healthcare Providers
> Minimum data required to create a provider:

```json
{
    "user" : "URL of a User login account",
    "email" : "must.be@unique.and.valid",
}
```

> Complete provider data, as returned by the API:

```json
{
    "user" : "URL of a User login account",
    "name" : "..." | null,
    "email" : "must.be@unique.and.valid",
    "phone_number" : "+999999999" | null,
    "address" : "URL of an Address | null",
    "tax_id" : "...",
    "created_at" : "ISO-8601 datetime",
    "updated_at" : "ISO-8601 datetime",
    "deleted_at" : "ISO-8601 datetime",
}
```

> In order to create a claim or invoice, more data is required than is required to create a provider. Specifically, the following fields may not be null in that case:

```json
{
    "user" : "URL of a User login account",
    "name" : "...",
    "email" : "must.be@unique.and.valid",
    "phone_number" : "+999999999",
    "address" : "URL of an Address",
}
```

<aside class="warning">
TODO: are we still using the flow in which providers POST to providers/ to add their user accounts?
</aside>
