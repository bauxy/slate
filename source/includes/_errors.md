# Errors

The Bauxy API uses the following error codes:

Error Code | Meaning
---------- | -------
400 | Bad Request -- Your request sucks
401 | Unauthorized -- Your API key is wrong
403 | Forbidden -- Administrators only
404 | Not Found -- The specified page could not be found
405 | Method Not Allowed -- Invalid method
406 | Not Acceptable -- You requested a format that isn't json
429 | Too Many Requests -- Slow down!
500 | Internal Server Error -- We had a problem with our server. Try again later.
503 | Service Unavailable -- We're temporarially offline for maintenance. Please try again later.
