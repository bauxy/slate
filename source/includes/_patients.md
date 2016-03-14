# Patients

`POST /api/v1.5/patients/`

`GET|PUT|PATCH|POST /api/v1.5/patients/{id}/`

Complete patient data, as returned by the API:

```json
{
    "first_name" : "...",
    "last_name" : "...",
    "email" : "must.be@unique.and.valid",
    "phone_number" : "... | null",
    "address" : "URL of an Address object | null",
    "gender" : "M | F | null",
    "is_member" : "true | false | null",
    "relation_to_member" : "URL of a Patient object | null",
    "relationship_type" : "Self | Spouse | Child | Other",
    "dob" : "ISO-8601 datetime (date of birth) | null",
    "updated_at" : "ISO-8601 datetime | null",
    "deleted_at" : "ISO-8601 datetime | null",
    "eligibility" : "... | null"
}
```

JSON Parameter name | Value | Required
--------------------|-------|---------
first_name | String | True
last_name | String | True
email | Email | True
phone_number | +99999999999 format | False
address | url of address object | False
gender | `M`, `F` | False
is_member | Boolean | False
relation_to_member | url of patient member | False
relationship_type | `Self`, `Spouse`, `Child`, `Other` | False
dob | ISO-8601 datetime (date of birth) | False

<aside class="notice">
Anybody may create a patient, including unauthenticated users. This is so that individuals my sign up as patients if they like.
</aside>

## Checking Patient Eligibility

`GET /api/v1.5/patients/{id}/eligibility`


> curl -d "127.0.0.1/api/v1.5/patients/72/eligibility/?insurer=vsp&username=jeremy.bluvol@gmail.com&password=Iwonttellyou&refresh=False"

``` json
{
    "Contact Lens Exam": {
        "EligibleAsOfDate": "2016-03-01",
        "Eligible": true,
        "Copay": "$0",
        "Coverage": "$105.00",
        "PlanRefreshDate": "2017-03-01"
    },
    "Frame": {
        "EligibleAsOfDate": "2016-03-01",
        "Eligible": true,
        "Copay": "$25.00",
        "Coverage": "$70.00",
        "PlanRefreshDate": "2017-03-01"
    },
    "Prescription Lenses": {
        "Single Vision": " $30.00",
        "EligibleAsOfDate": "2016-03-01",
        "Bifocal": " $50.00",
        "Progressive": " $50.00",
        "Eligible": true,
        "Copay": "$25.00",
        "Trifocal": " $65.00",
        "Coverage:": "*** Depends on lenses",
        "PlanRefreshDate": "2017-03-01"
    },
    "MemberDependent": {
        "username": "Jeremy Bluvol",
        "email": "jeremy.bluvol@gmail.com"
    },
    "Exam": {
        "EligibleAsOfDate": "2016-03-01",
        "Eligible": true,
        "Copay": "$15.00",
        "Coverage": "$45.00",
        "PlanRefreshDate": "2017-03-01"
    }
}
```

We can contact VSP or Eyemed on behalf of the user to fetch their eligibility information. Either username/password needs to be passed as parameters or the rest of the data - firstname, lastname, memberID, date of birth and ssn.

URL Parameter name | Value | Required
-------------------|-------|---------
firstname | First name | False
lastname | Last name | False
memberID | memberID | False
birthday_day | [1-31] | False
birthday_month | [1-12] | False
birthday_year | 4-digit year | False
ssn | social security number | False
username | insurer login | False
password | insurer password | False
refersh | `True` or `False`. If `True`, it will force checking plan eligibility from the insurance provider's website. There is a limit of 1 ``refresh`` request per day. | False
insurer | `vsp`, `eyemed` | True

Gives back a `JSON` string of user's plan eligibility, like an example on the right from `VSP`.


