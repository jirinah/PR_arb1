  ##### IMPORT PACKAGES #####
import requests
import json

  ##### REQUEST API-DATA #####
cat = requests.get('https://catfact.ninja/facts') # request the API-data
print(cat.status_code)                            # check if the request went okay (should print 200)
print(cat.json())

  ##### FUNCTION FOR JSON FORMAT #####
def jprint(obj):                     # found it at https://www.dataquest.io/blog/api-in-python/
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print(text) 
jprint(cat.json())

# Now the API-data from catfacts is ready to be used 
