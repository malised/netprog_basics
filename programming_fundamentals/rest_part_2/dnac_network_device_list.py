import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_IP, DNAC_USERNAME, DNAC_PASSWORD, DNAC_VERSION
from dnac_login import get_auth_token


def myprint_device_list(device_list):
    print("Hostname \t Mac Address \t\t SW Version \t\t Serial Number \t \
    Management IP Address \t Platform ID \t\t Device ID")

    for item in device_list['response']:
        print(f"{item['hostname']} \t {item['macAddress']} \t {item['softwareVersion']} \t \
        {item['serialNumber']} \t \
        {item['managementIpAddress']} \t \
        {item['platformId']} \t \
        {item['id']} ")


def get_device_list(token):
    #Network Device endpoint
    #url = "https://sandboxdnac.cisco.com/api/v1/network-device"
    url = 'https://' + DNAC_IP + '/api/' +  DNAC_VERSION + '/network-device'

    #Build header Info
    hdr = {
            'x-auth-token': token,
            'content-type' : 'application/json'
            }

    # Make the Get Request
    resp = requests.get(url, headers=hdr)

    #capture the data from the controller
    device_list = resp.json()

    #pretty print the data we want
    myprint_device_list(device_list)
    #print(device_list['response'])


def get_specific_device(token, querystring):
    #Network Device endpoint
    #url = "https://sandboxdnac.cisco.com/api/v1/network-device"
    url = 'https://' + DNAC_IP + '/api/' +  DNAC_VERSION + '/network-device'

    #Build header Info
    hdr = {
            'x-auth-token': token,
            'content-type' : 'application/json'
            }

    # Make the Get Request for a specific device
    resp = requests.get(url, headers=hdr, params=querystring)

    #capture the data from the controller
    queried_device = resp.json()

    #pretty print the data we want
    myprint_device_list(queried_device)

    #return queried_device



if __name__ == "__main__":
 # Get a Token
 token = get_auth_token()

 # Get the list of devices
 get_device_list(token)

 # Query a specific device
 querystring = {
    "macAddress":"84:8a:8d:05:76:00",
    "managementIpAddress":"10.10.20.81"
 }
 #print(get_specific_device(token, querystring))
 get_specific_device(token, querystring)

 # Query another specific device
 querystring = {
    "id": "6b741b27-f7e7-4470-b6fc-d5168cc59502"
 }
 #print(get_specific_device(token, querystring))
 get_specific_device(token, querystring)
