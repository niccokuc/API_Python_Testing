'''
Created on 7 Jan. 2020

@author: NerminKuc
'''
import requests
import json

# Enter the Longitude and Latitude value
lat = input("Enter Latitude :")
long = input("Enter Longatude :")

# Make the GET request from the API
r = requests.get('https://api.darksky.net/forecast/70aa22b49abb3f52ebfe2aa2438265ee/' + str(lat) + ',' + str(long))
status_API = int(r.status_code)
print(r.content)

# Verify the GET API is working
if status_API == 200:
    print("[+] The API call is good to go! ")
    j = json.loads(r.text)
else:
    print("[-] The API call is BAD! " )
    exit

# What is the current weather at that location?
print("[+] The weather is : " + j['currently']['summary'])


