from util import *
#!SNIP START
response = requests.get(API_ROOT + 'insurance_companies/1/')
company = response.json()
printj(company)
#!SNIP END
