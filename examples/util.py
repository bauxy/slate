import json
import requests
from requests_toolbelt.utils import dump
from functools import partial

API_ROOT = 'http://api-staging.bauxy.com/api/v1.5/'

def printj(json_object):
    "Pretty-print a json object"
    print json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))

# This particular username and password doesn't work, for obvious reasons; use your own.
user = ('peter', '1qaz')

dump = partial(dump.dump_response, request_prefix='', response_prefix='')
