# Checking Patient Eligibility

```python
response = requests.get(API_ROOT + 'planinfo/eyemed/?username=some.insured@bauxy.com&password=_fake_', auth=user)
printj(response.json())
```

```http
GET /api/v1.5/planinfo/eyemed/?username=some.insured@bauxy.com&password=_fake_ HTTP/1.1
Host: api-staging.bauxy.com
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.9.1


HTTP/1.1 200 OK
x-xss-protection: 1; mode=block
x-content-type-options: nosniff
Content-Encoding: gzip
Transfer-Encoding: chunked
Vary: Accept-Encoding
Vary: Cookie
Server: nginx/1.9.2
Connection: keep-alive
Allow: GET, HEAD, OPTIONS
Date: Thu, 24 Mar 2016 13:17:23 GMT
X-Frame-Options: DENY
Content-Type: application/json
```

```json
{
    "Contact Lens Exam": {
        "Copay": null,
        "Coverage": "$160",
        "Eligible": true,
        "EligibleAsOfDate": "2015-12-01",
        "PlanRefreshDate": "2017-03-24"
    },
    "Exam": {
        "Copay": null,
        "Coverage": "$30",
        "Eligible": true,
        "EligibleAsOfDate": "2015-12-01",
        "PlanRefreshDate": "2017-03-24"
    },
    "Frame": {
        "Copay": null,
        "Coverage": "$100",
        "Eligible": true,
        "EligibleAsOfDate": "2015-12-01",
        "PlanRefreshDate": "2017-03-24"
    },
    "MemberDependent": {
        "email": "some.insured@bauxy.com",
        "username": "some.insured"
    },
    "Prescription Lenses": {
        "Bifocal": "$40",
        "Copay": null,
        "Coverage": "*** Depends on lenses",
        "Eligible": true,
        "EligibleAsOfDate": "2015-12-01",
        "PlanRefreshDate": "2017-03-24",
        "Progressive": "$55",
        "ScratchCoating": "$9",
        "Single Vision": "$25",
        "Tint": "$9",
        "Trifocal": "$55",
        "UVTreatment": "$9"
    }
}
```

`GET /api/v1.5/planinfo/eyemed/`

`GET /api/v1.5/planinfo/vsp/`

<aside class="notice">
This endpoint requires authentication. Don't forget to set the appropriate `sessionid` and `csrftoken` cookies!
</aside>

We can contact VSP or Eyemed on behalf of the user to fetch their eligibility information. This requires one of two parameter sets:

The simplest case is to just use `username` and `password` for the relevant insurance provider.

If you know the insurance member's personal data but not their username and password, we can still handle this. In that case, we need `first_name`, `last_name`, `dob_year`, `dob_month`, `dob_day`, and one of `ssn` or `member_id`. Due to PII considerations, use of `ssn` is depreciated.

In either case, we can also accept the optional parameter `refresh`.

URL Parameter name | Value                       | Required
------------------ | --------------------------- | --------
username           | insurer login               | False
password           | insurer password            | False
first_name         | First name                  | False
last_name          | Last name                   | False
dob_year           | [1-31]                      | False
dob_month          | [1-12]                      | False
dob_day            | 4-digit year                | False
member_id          | Insurance Company Member ID | False
ssn                | social security number [1]  | False
refresh            | boolean [2]                 | False

[1] Digits only

[2] If set, it will force checking plan eligibility from the insurance provider's website.
There is a limit of 1 `refresh` request per day.

Returns a `JSON` string of user's plan eligibility, like an example on the right from `EyeMed`.

<aside class="notice">
Bauxy caches everything, with the exception of `password` and `ssn`. Once you've successfully
retrieved eligibiltiy information from a given provider, further requests don't need the
information passed in again. A simple authenticated request to the endpoint will return the
eligbility information.<br />
<br />
This implies that if you've ever retrieved eligibility information using `username` and `password`,
for example, you could refresh it using only `?refresh=true&password=whatever`.
</aside>
