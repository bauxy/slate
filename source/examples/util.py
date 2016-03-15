import json
import requests

API_ROOT = 'http://api-staging.bauxy.com/api/v1.5/'

def printj(json_object):
    "Pretty-print a json object"
    print json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))

# This particular username and password doesn't work, for obvious reasons; use your own.
user = ('username', 'password')
