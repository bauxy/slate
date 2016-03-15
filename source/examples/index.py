from util import *
#!SNIP START
response = requests.get(API_ROOT)
actions = response.json()
printj(actions)
#!SNIP END
print
print dump(response).decode('utf-8')
