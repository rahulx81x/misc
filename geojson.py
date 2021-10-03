import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
forurl = dict()
forurl['address'] = address
if api_key is not False:
    forurl['key'] = api_key
url = serviceurl + urllib.parse.urlencode(forurl)

content = urllib.request.urlopen(url, context=ctx)
data = content.read().decode()
try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

print(js['results'][0]['place_id'])
