# Checking Patient Eligibility


```json
{
    "Contact Lens Exam": {
        "Copay": "$0",
        "Coverage": "$105.00",
        "Eligible": true,
        "EligibleAsOfDate": "2016-03-01",
        "PlanRefreshDate": "2017-03-01"
    },
    "Exam": {
        "Copay": "$15.00",
        "Coverage": "$45.00",
        "Eligible": true,
        "EligibleAsOfDate": "2016-03-01",
        "PlanRefreshDate": "2017-03-01"
    },
    "Frame": {
        "Copay": "$25.00",
        "Coverage": "$70.00",
        "Eligible": true,
        "EligibleAsOfDate": "2016-03-01",
        "PlanRefreshDate": "2017-03-01"
    },
    "MemberDependent": {
        "email": "jeremy.bluvol@gmail.com",
        "username": "Jeremy Bluvol"
    },
    "Prescription Lenses": {
        "Bifocal": " $50.00",
        "Copay": "$25.00",
        "Coverage:": "*** Depends on lenses",
        "Eligible": true,
        "EligibleAsOfDate": "2016-03-01",
        "PlanRefreshDate": "2017-03-01",
        "Progressive": " $50.00",
        "Single Vision": " $30.00",
        "Trifocal": " $65.00"
    }
}
```

`GET /api/v1.5/planinfo/eyemed/`

`GET /api/v1.5/planinfo/vsp/`

We can contact VSP or Eyemed on behalf of the user to fetch their eligibility information. This requires one of two parameter sets: either `{refresh, username, password}` or  `{refresh, firstname, lastname, memberID, birthday_day, birthday_month, birthday_year, ssn}`.

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
refresh            | `True` or `False`. If `True`, it will force checking plan eligibility from the insurance provider's website. There is a limit of 1 ``refresh`` request per day. | False
insurer            | `vsp`, `eyemed`                                                                                                                                                 | True

Gives back a `JSON` string of user's plan eligibility, like an example on the right from `VSP`.
