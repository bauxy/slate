from util import *
#!SNIP START
response = requests.get(API_ROOT + 'patients/8/', auth=user)
patient = response.json()
printj(patient)
#!SNIP END
print dump(response).decode('utf-8')

# Post patient
patient = {
    'first_name' : 'Adam',
    'last_name'  : 'Baker',
    'email'      : 'ab@c.de'
}
response = requests.post(API_ROOT + 'patients/', data=patient)
printj(response.json())
print dump(response).decode('utf-8')
