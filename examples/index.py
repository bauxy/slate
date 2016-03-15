from util import *
response = requests.get(API_ROOT)
actions = response.json()
print 'GET:'
print 'HTTP:'
print dump(response).decode('utf-8')
print
print 'JSON:'
printj(actions)
print
print
print "OPTIONS:"
response = requests.options(API_ROOT)
print 'HTTP:'
print dump(response).decode('utf-8')
print
print 'JSON:'
printj(response.json())
