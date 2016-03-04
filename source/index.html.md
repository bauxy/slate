---
title: Bauxy API Reference
language_tabs:
  - http: HTTP
  - python: Python
toc_footers:
  - "<a href='#'>Sign Up for a Developer Key</a>"
  - "<a href='https://github.com/tripit/slate'>Documentation Powered by Slate</a>"
includes:
  - errors
search: true
---

# Introduction
Welcome to the Bauxy API!

The Bauxy API 1.5 is a RESTful service helping patients get reimbursed for out-of-network insurance claims with minimal overhead.

Healthcare providers can sign up and route their patients through the service automatically, making it easy for patients to receive their claim even if the provider isn't in the patient's insurance network.

We have usagse examples in raw HTTP and Python. You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right. As you can see, when using Python, we recommend the use of the excellent [Requests](http://docs.python-requests.org/en/master/) package.

# Overview
## Fundamentals of usage
> Get a list of API endpoints

```http
GET /api/{version}/
```

```python
import requests
r = requests.get(API_ROOT)
r.json()
```

The API provides a number of endpoints, the list of which may be retrieved by querying the API root: These endpoints have standardized behavior: in general, the following operations are supported.

> List of items to which the authenticated user has access:

```
GET /api/{version}/{endpoint}/
```

> Given appropriate data, create a new item:

```
POST /api/{version}/{endpoint}/
```

> Given appropriate data, replace the item with the given id:

```
PUT /api/{version}/{endpoint}/{id}/
```

> Given appropriate partial JSON data, update the specified item

```
PATCH /api/{version}/{endpoint}/{id}/
```

> Remove the specified item

```
DELETE /api/{version}/{endpoint}/{id}/
```

Naturally, users may only read, modify or delete resources which they own.

## Expert Assistance
Sometimes one may desire to just delegate all responsibility away. We support that! Specifically, one may input only minimal information into our database and have us take care of everything else, so long as an image of the original bill is in our database. In that case, our team of experts will go over the image and handle all the data processing. Be aware that as this requires human intervention, it will slow processing somewhat. If the image quality is poor or not all necessary information is present on the bill, we may not be able to continue processing the claim. Whether or not the process is successful, additional costs will be incurred.

## Notes on Incomplete Data
Best practice for users who wish to minimize cost is to provide enough data to create a bill whenever possible, instead of providing only minimal data.

# Authentication
<aside class="warning">
TODO: How exactly do we authenticate, anyway? API key, login/token, basic, something else?
</aside>

# Users
`users/` endpoint: login accounts to our system.

Users can be individuals who have signed up with us, in which case they are tied to a single Patient account. Alternately, they may be healthcare providers, who manage a number of Patient accounts.
<aside class="warning">
TODO: is users/ even exposed to the outside world yet? What’s the interface?
</aside>

<aside class="notice">
Note that one creates a user by <code>POST</code>ing to <code>patients/</code> or
<code>providers/</code>; <code>POST users/</code> is forbidden. This is because
every user must fall into one of those two classes.
</aside>

# Insurance Companies
`insurance_companies/` endpoint.

## Read-only
We develop custom processes to ensure maximal claim acceptance rates at every supported insurance company. However, this means that we cannot allow outside users to add companies. If you represent an insurance company and would like us to add support, please reach out to us at [info@bauxy.com](mailto:info@bauxy.com)!

> Complete company data, as returned by the API:

```json
{
    "name" : "...",
    "is_vision" : true | false,
    "is_medical" : true | false,
    "is_dental" : true | false
}
```

# Patients
`patients/` endpoint.

> Minimum data required to create a patient:

```json
{
    "first_name" : "...",
    "last_name" : "...",
    "email" : "must.be@unique.and.valid"
}
```

> Complete patient data, as returned by the API:

```json
{
    "first_name" : "...",
    "last_name" : "...",
    "email" : "must.be@unique.and.valid",
    "phone_number" : "..." | null,
    "address" : "URL of an Address object | null",
    "gender" : "M" | "F" | null,
    "is_member" : true | false | null,
    "relation_to_member" : "URL of a Patient object | null",
    "relationship_type" : "Self" | "Spouse" | "Child" | "Other",
    "dob" : "ISO-8601 datetime (date of birth) | null",
    "updated_at" : "ISO-8601 datetime | null",
    "deleted_at" : "ISO-8601 datetime | null",
    "eligibility" : "..." | null
}
```

> In order to create a claim or invoice, more patient data is required than is required to create a patient. Specifically, the following fields may not be null in that case:

```json
{
    "first_name" : "...",
    "last_name" : "...",
    "email" : "must.be@unique.and.valid",
    "phone_number" : "...",
    "address" : "URL of an Address object",
    "is_member" : true | false,
    "relation_to_member" : "URL of a Patient object if not "is_member"",
    "relationship_type" : "Self" | "Spouse" | "Child" | "Other",
    "dob" : "ISO-8601 datetime (date of birth)"
}
```

## Notes
Anybody may create a patient, including unauthenticated users. This is so that individuals my sign up as patients if they like.

## Patient Creation Example
<aside class="warning">
TODO: Let's use a standard library like Requests, or generate our own official Bauxy API library, but not a generic-sounding and undocumented library `util`.
</aside>

```python
>>> import util
>>> firstname = 'Mike'
>>> lastname = 'Tyson'
>>> email = 'mike.tyson@gmail.com'
>>> util.post_status('/api/v1.5/patients/', {'firstname': firstname, 'lastname': lastname, 'email': email})
201
```

# Healthcare Providers
`providers/` endpoint: describes healthcare providers in our system.
<aside class="warning">
TODO: are we still using the flow in which providers POST to providers/ to add their user accounts?
</aside>

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

# Addresses
`adddresses/` endpoint: describes physical addresses

> Minimum data required to create an address:

```json
{
    "line1" : "...",
    "city"  : "...",
    "zipcode" : "...",
    "state" : "...",
}
```

> Complete bill data, as returned by the API:

```json
{
    "line1" : "...",
    "line2" : "...",
    "city"  : "...",
    "zipcode" : "...",
    "state" : "...",
}
```
