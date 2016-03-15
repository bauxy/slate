from util import *
#!SNIP START
# For eligibility, we need to pass in data about the insurance company.
response = requests.get(API_ROOT + 'providers/3/')
printj(response.json())
#!SNIP END
print dump(response).decode('utf-8')
