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


def get_device_id_list(device_list):
    #print("\nList of Device IDs")
    device_id_list = []
    for item in device_list['response']:
        device_id_list.append(item['id'])
    return device_id_list

def get_device_platform_list(device_list):
    #print("\nList of Device IDs")
    device_platform_list = []
    for item in device_list['response']:
        device_platform_list.append(item['platformId'])
    return device_platform_list

def get_device_id_and_platform_list(device_list):
    #print("\nList of Device IDs")
    device_info_list = []
    #device_id_list = []
    #device_platform_list = []
    for item in device_list['response']:
        #device_id_list.append(item['id'])
        #device_platform_list.append(item['platformId'])
        device_info_list.append((item['id'],item['platformId']))
    print(device_info_list)
    return (device_info_list)

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
    ##print(device_list['response'])
    return device_list


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

def get_device_interfaces(token, net_device_id):
    # network interfaces for a specific device
    #https://{{dnac}}:{{port}}/dna/intent/api/v1/interface/network-device/{{network_device_id}}
    url = 'https://' + DNAC_IP + '/dna/intent' + '/api/' +  DNAC_VERSION + \
    '/interface/network-device' + net_device_id

    #Build header Info
    hdr = {
            'x-auth-token': token,
            'content-type' : 'application/json'
            }

    # Make the Get Request for a specific device
    resp = requests.get(url, headers=hdr)
    interface_list = resp.json()
    #print(interface_list)
    print("PortName \t\t Status \t MacADDR \t\t \
    PortMode \t PortType \t IPv4 \t Mask")

    for item in interface_list["response"]:
        if item['status'] == 'not applicable':
            item['status'] = "\tN/A"
        print(f"{item['portName']} \t {item['status']} \t \
        {item['macAddress']} \t {item['portMode']} \t\t {item['portType']} \
        {item['ipv4Address']} \t {item['ipv4Mask']}")




if __name__ == "__main__":
 # Get a Token
 token = get_auth_token()

 # Get the list of devices and list of device IDs
 device_list = get_device_list(token)
 device_ids = get_device_id_list(device_list)
 #print(f"\n{device_ids}")
 devices = get_device_id_and_platform_list(device_list)
 #exit(0)

 # Query a specific device based on its MACAddress and Mgmt IP
 querystring = {
    "macAddress":"84:8a:8d:05:76:00",
    "managementIpAddress":"10.10.20.81"
 }
 print("\n")
 get_specific_device(token, querystring)

 # Option 1: Query another specific device based on deviceID
 # Test with a list of only ONE element
 ##device_ids = ["6b741b27-f7e7-4470-b6fc-d5168cc59502"]
 #for net_device_id in device_ids:
#     #querystring = {
#        #"id": net_device_id
#     #}
#     print("\n")
#     #get_specific_device(token, querystring)
#     get_device_interfaces(token, net_device_id)

# Option 2: Another way
# Test with a list of only ONE element
 #devices = [('6b741b27-f7e7-4470-b6fc-d5168cc59502', 'AIR-CT3504-K9')]
 for item in devices:
     #print(f"{item}")
     net_device_id = item[0]
     platform = item[1]
     print("\n")
     print(f"DeviceID = {net_device_id} \nPlatform = {platform}")
     get_device_interfaces(token, net_device_id)
