#Python 2.7.6
#RestfulClient.py

import requests                                                                         #HTTP Library for Python
from requests.auth import HTTPDigestAuth
from requests.auth import HTTPBasicAuth                                                 #HTTP Basic authentication
import json                                                                             #Builtin JSON decoder when dealing with JSON data
import getpass                                                                          #Prompt the user for a password without echoing
#from termcolor import colored, cprint

url_status = 'https://10.1.20.101/api/v3.1/status?_include=status'                              #API endpoint to get the server status
headers_status = {'Tenant': 'default_tenant'}                                                   #Header required for the API call
username = raw_input('what is your username: ')                                         #Get username from user
password = getpass.getpass('Enter your password: ')                                     #Get password from user
auths = HTTPBasicAuth(username,password)                                                #Get authenticated to run the API call
myResponse = requests.get(url_status,headers=headers_status,auth=auths, verify=False)                   #Run a GET request using URL, header and authentication.
if(myResponse.ok):
        print (json.loads(myResponse.content))                                                          #Print response text
        #print ('\033[92m' + '(myResponse.status_code)')                                                                        #Print response code
        print (myResponse.status_code)                                                                  #Print response code
else:
        print (myResponse.status_code)

############################# GET TOKEN ##########################

url_token = 'https://10.1.20.101/api/v3.1/tokens'                                       #API endpoint to get the server status
headers_token = {'Tenant': 'default_tenant'}                                                   #Header required for the API call
#username = raw_input('what is your username: ')                                         #Get username from user
#password = getpass.getpass('Enter your password: ')                                     #Get password from user
#auths = HTTPBasicAuth(username,password)                                                #Get authenticated to run the API call
myResponse = requests.get(url_token,headers=headers_token,auth=auths, verify=False)                   #Run a GET request using URL, header and authentication.
if(myResponse.ok):
#       token = myResponse.content
#        print (token)
        json_obj=json.loads(myResponse.content)
        tokens=json_obj["accessToken"]
        print (tokens)
        print (myResponse.content)
        print (json.loads(myResponse.content))                                                          #Print response text
        print (myResponse.status_code)                                                                  #Print response code
else:
        print (myResponse.status_code)
