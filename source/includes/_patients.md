# Patients
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
    "relation_to_member" : "URL of a Patient object if not 'is_member'",
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
