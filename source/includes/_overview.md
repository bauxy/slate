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
