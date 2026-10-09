  ##### IMPORT PACKAGES #####
import keyring     # for safely storing the API-key
import requests    # to get access to the API data
import json        # for data in json-format 

  ##### PYTHON KEYRING #####
# run in terminal to save API key with keyring: 
# keyring set strømpriser api-key
key:str = str(keyring.get_password("strømpriser", "api-key"))   # Access the key in the program
print(key)      

  ##### FUNCTION FOR JSON FORMATING #####
# I found this as https://www.dataquest.io/blog/api-in-python/ 
def jprint(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print(text) 

  ##### FETCH DATA FROM STRØMPRISER API #####
headers = {"x-api-key": "key"}
response = requests.get('https://api.strompriseridag.no/v1/NO5', headers=headers)
print(response.status_code)
jprint(response.json())                      
