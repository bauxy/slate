from util import *
#!SNIP START
# For eligibility, we need to pass in data about the insurance company.
data = {
    'insurer'  : 'vsp',
    'username' : 'jeremy.bluvol@gmail.com', # insurance username, not Bauxy's
    'password' : 'Iwonttellyou',
    'refresh'  : False
}
response = requests.get(API_ROOT + 'patients/72/eligibility/', auth=user, data=data)
printj(response.json())
#!SNIP END
print dump(response).decode('utf-8')
