# Insurance Companies

Available commands:

`POST /api/v1.5/insurance_companies/` - for admins only

`GET /api/v1.5/insurance_companies/{id}/`

`GET /api/v1.5/insurance_companies/`

Complete company data, as returned by the API:

```json
{
    "name" : "...",
    "is_vision" : "true | false",
    "is_medical" : "true | false",
    "is_dental" : "true | false"
}
```

JSON Parameter name | Value | Required
--------------------|-------|---------
name | Insurance company name | True
is_vision | Boolean | False
is_medical | Boolean | False
is_dental | Boolean | False

We develop custom processes to ensure maximal claim acceptance rates at every supported insurance company. However, this means that we cannot allow outside users to add companies. If you represent an insurance company and would like us to add support, please reach out to us at [info@bauxy.com](mailto:info@bauxy.com)!
