from util import *
#!SNIP START
response = requests.get(API_ROOT + 'addresses/2/', auth=user)
printj(response.json())
#!SNIP END
print dump(response).decode('utf-8')
