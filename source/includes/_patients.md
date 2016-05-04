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
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
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
    'email': 'ab@c.de'
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

email=ab%40c.de
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
    "first_name": "",
    "gender": null,
    "id": 87,
    "is_member": null,
    "last_name": "",
    "phone_number": null,
    "relation_to_member": null,
    "relationship_type": "Self",
    "updated_at": "2016-03-15T13:37:35.805489Z",
    "url": "http://api-staging.bauxy.com/api/v1.5/patients/87/",
    "user":{
        "id":22,
        "email":"ab@c.de",
        "is_staff":false,
        "url":"http://api-staging.bauxy.com/api/v1.5/users/22/",
        "username":"ab@c.de"
    }
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
