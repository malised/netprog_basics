#! /usr/bin/env python

import requests


login_url = "https://sandboxdnac.cisco.com:443/dna/system/api/v1/auth/token"

username = "devnetuser"
password = "Cisco123!"
# Provinding only the username and password, we can generate the base64 encoding
# for the basic auth using the command below:
# authentication = HTTPBasicAuth(username, password)


payload={}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

# Let's get the token first
response = requests.request("POST", login_url, headers=headers, data=payload)

# Print the "text" of the response body
# Here the type is a string
print(response.text)
print("\n")

# Convert the response in JSON format
# Here the type is a dict (response.json = < class Dict>)
#print(f"\n Its type is {type(response.json())}\n")
response.json()
token = response.json()["Token"]
#print(token)
#print("\n")

# We can print the headers with the following lines
#print(response.headers)
#print(response.headers.get("X-Content-Type-Options"))


# -----
# Use the token obtained to make another request and query the devices list

print("\nMaking the 2nd request....\n")

url = "https://sandboxdnac.cisco.com:443/dna/intent/api/v1/network-device"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-auth-token': token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.status_code)
#print(response.text)
print(response.json())
