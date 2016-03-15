# Patients
> GET a patient

```python
response = requests.get(API_ROOT + 'patients/8/', auth=user)
patient = response.json()
printj(patient)
```

```http
GET /api/v1.5/patients/8/ HTTP/1.1
Host: api-staging.bauxy.com
Connection: keep-alive
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Basic cGV0ZXI6MXFheg==
User-Agent: python-requests/2.9.1


HTTP/1.1 200 OK
x-xss-protection: 1; mode=block
x-content-type-options: nosniff
Content-Encoding: gzip
Transfer-Encoding: chunked
Vary: Accept-Encoding
Vary: Accept
Server: nginx/1.9.2
Connection: keep-alive
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Date: Tue, 15 Mar 2016 13:29:51 GMT
X-Frame-Options: DENY
Content-Type: application/json
```

```json
{
    "address": "http://api-staging.bauxy.com/api/v1.5/addresses/2/",
    "dob": "1974-11-15",
    "email": "gleb@bauxy.com",
    "first_name": "Gleb",
    "gender": "M",
    "id": 8,
    "is_member": null,
    "last_name": "Rybkin",
    "phone_number": null,
    "relation_to_member": "http://api-staging.bauxy.com/api/v1.5/patients/5/",
    "relationship_type": "Self",
    "updated_at": "2016-02-12T22:33:42.105308Z",
    "url": "http://api-staging.bauxy.com/api/v1.5/patients/8/",
    "user": null
}
```

> POST a minimal patient

```python
patient = {
    'first_name' : 'Adam',
    'last_name'  : 'Baker',
    'email'      : 'ab@c.de'
}
response = requests.post(API_ROOT + 'patients/', data=patient)
printj(response.json())
```

```http
POST /api/v1.5/patients/ HTTP/1.1
Host: api-staging.bauxy.com
Content-Length: 47
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.9.1
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded

first_name=Adam&last_name=Baker&email=ab%40c.de
HTTP/1.1 201 Created
x-xss-protection: 1; mode=block
x-content-type-options: nosniff
Transfer-Encoding: chunked
Vary: Accept
Server: nginx/1.9.2
Connection: keep-alive
Location: http://api-staging.bauxy.com/api/v1.5/patients/87/
Allow: GET, POST, HEAD, OPTIONS
Date: Tue, 15 Mar 2016 13:37:35 GMT
X-Frame-Options: DENY
Content-Type: application/json
```

```json
{
    "address": null,
    "dob": null,
    "email": "ab@c.de",
    "first_name": "Adam",
    "gender": null,
    "id": 87,
    "is_member": null,
    "last_name": "Baker",
    "phone_number": null,
    "relation_to_member": null,
    "relationship_type": "Self",
    "updated_at": "2016-03-15T13:37:35.805489Z",
    "url": "http://api-staging.bauxy.com/api/v1.5/patients/87/",
    "user": null
}
```

`POST /api/v1.5/patients/`

`GET|PUT|PATCH|POST /api/v1.5/patients/{id}/`

Complete patient data, as returned by the API:

JSON Parameter name | Value                              | Required
------------------- | ---------------------------------- | --------
first_name          | String                             | True
last_name           | String                             | True
email               | Email                              | True
phone_number        | +99999999999 format                | False
address             | url of address object              | False
gender              | `M`, `F`                           | False
is_member           | Boolean                            | False
relation_to_member  | url of patient member              | False
relationship_type   | `Self`, `Spouse`, `Child`, `Other` | False
dob                 | ISO-8601 datetime (date of birth)  | False

<aside class="notice">
Anybody may create a patient, including unauthenticated users. This is so that individuals my sign up as patients if they like.
</aside>

## Checking Patient Eligibility
`GET /api/v1.5/patients/{id}/eligibility`

> curl -d "127.0.0.1/api/v1.5/patients/72/eligibility/?insurer=vsp&username=jeremy.bluvol@gmail.com&password=Iwonttellyou&refresh=False"

```json
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

URL Parameter name | Value                                                                                                                                                           | Required
------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------
firstname          | First name                                                                                                                                                      | False
lastname           | Last name                                                                                                                                                       | False
memberID           | memberID                                                                                                                                                        | False
birthday_day       | [1-31]                                                                                                                                                          | False
birthday_month     | [1-12]                                                                                                                                                          | False
birthday_year      | 4-digit year                                                                                                                                                    | False
ssn                | social security number                                                                                                                                          | False
username           | insurer login                                                                                                                                                   | False
password           | insurer password                                                                                                                                                | False
refersh            | `True` or `False`. If `True`, it will force checking plan eligibility from the insurance provider's website. There is a limit of 1 ``refresh`` request per day. | False
insurer            | `vsp`, `eyemed`                                                                                                                                                 | True

Gives back a `JSON` string of user's plan eligibility, like an example on the right from `VSP`.
