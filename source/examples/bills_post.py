from util import *
#!SNIP START
data = {
    'patient'   : "http://api-staging.bauxy.com/api/v1.5/patients/87/",
    'insurance' : "http://api-staging.bauxy.com/api/v1.5/insurance_companies/1/",
    'provider'  : "http://api-staging.bauxy.com/api/v1.5/providers/3/"
}
response = requests.post(API_ROOT + 'bills/', auth=user, data=data)
printj(response.json())
#!SNIP END
print dump(response).decode('utf-8')
