import requests
import json

#Get API Key
API_Key = input ("Please enter you Meraki API Key  ")

organisation_url = "https://api.meraki.com/api/v0/organizations"
headers = {"X-Cisco-Meraki-API-Key": API_Key}

#Get All organisation ID associated with account
response = requests.request("GET", organisation_url, headers=headers)

#Decode json response
org_data=json.loads(response.text)

print("{0:<20} {1:>15} {2:>20} {3:>15} {4:>22} {5:>16}". format("Camera Serial Number", "Model Number", "Zone_ID", "Zone Label", "Network ID", "Organisation ID"))
#For each oranization_id search for cameras
for o in org_data:
    organisation_id = o['id']
    #Build Inventory URL
    inventory_url = "https://api.meraki.com/api/v0/organizations/" + organisation_id + "/inventory"

    response = requests.request("GET", inventory_url, headers=headers)
    inv_data=json.loads(response.text)
    #For all lines of Inventory check is the device is a cemera and print out information
    for i in inv_data:
        if i['model'][0:2] == 'MV':
            #Build Zone URL
            zone_url = "https://api.meraki.com/api/v0/devices/" + i['serial'] + "/camera/analytics/zones"
            response = requests.request("GET", zone_url, headers=headers)
            zone_data=json.loads(response.text)
            for z in zone_data:
                print("{0:<20} {1:>15} {2:>20} {3:>15} {4:>22} {5:>16}".format(i['serial'], i['model'], z['zoneId'], z['label'], i['networkId'], organisation_id))
