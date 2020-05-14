import requests
import json


url = "https://api.meraki.com/api/v0/devices/Q2CX-KZDV-HMWG/switchPorts"

payload = {}
headers = {
  'Accept': '*/*',
  'X-Cisco-Meraki-API-Key': 'e35fd60c7cc8d1bb4f5c00bb1e47c76e8aac7e2d'
}

response = requests.request("GET", url, headers=headers, data = payload)

if (response.status_code) ==200:
    inv_data=json.loads(response.text)
    print("{0:<20} {1:>30} {2:>20}". format("Port Number", "Port Name", "VLAN"))

    for i in inv_data:
        if i['name'] == None:
            i['name'] = 'Blank'
        print("{0:<20} {1:>30} {2:>20}". format(i['number'], i['name'], i['vlan']))

else:
    print("Unexpected status code: " + str(response.status_code))


#print(response.headers)
