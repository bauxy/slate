from util import *
#!SNIP START
# For eligibility, we need to pass in data about the insurance company.
response = requests.get(API_ROOT + 'bills/10/', auth=user)
printj(response.json())
#!SNIP END
print dump(response).decode('utf-8')
