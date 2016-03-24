from util import *

API_ROOT = 'http://52.36.174.23:8008/api/v1.5/'
#!SNIP START
response = requests.get(API_ROOT + 'planinfo/eyemed/?username=jeremy.bluvol@gmail.com&password=123Awesome!&refresh=True')
printj(response.json())
#!SNIP END
print dump(response).decode('utf-8')
