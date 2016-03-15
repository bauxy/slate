from util import *
#!SNIP START
response = requests.get(API_ROOT + 'items/8/', auth=user)
printj(response.json())
#!SNIP END
print dump(response).decode('utf-8')
