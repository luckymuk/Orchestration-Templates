#The following test cases are for CBAM and test out the POST / GET / MODIFY / TERMINATE functionality.
import requests as r
import json
import pytest
import time

def method_http_get(url, user, passwd):
   t=r.get(url,auth=(user,passwd))
#  print("%s".format(r.contents)) if r.ok else print("%s".format("Request failed"))
   print('"%s".format(r.contents)' if r.ok else '"%s".format("Request failed")')

if __name__ == "__main__":
   method_http_get('https://10.142.0.3/people','bob','123')
   method_http_get('https://10.142.0.3/people/1','bob','123')
   
   
   
#The following test cases are for CBAM and test out the POST / GET / MODIFY / TERMINATE functionality.
import requests as r
import json
import time

def method_http_get(url, user, passwd):
   t=r.get(url,auth=(user,passwd))
#  print("%s".format(r.contents)) if r.ok else print("%s".format("Request failed"))
   print("All good!! %s"%t if t.ok else "Request failed %s"%t)

if __name__ == "__main__":
    method_http_get('http://10.142.0.3:8000/people','bob','123')
    method_http_get('http://10.142.0.3:8000/people/1','bob','123')
    method_http_get('http://10.142.0.3:8000/peo','bob','123')
   
   
   
