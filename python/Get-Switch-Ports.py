import requests

url = "https://api.meraki.com/api/v0/devices/Q2CX-KZDV-HMWG/switchPorts"

payload = {}
headers = {
  'Accept': '*/*',
  'X-Cisco-Meraki-API-Key': 'e35fd60c7cc8d1bb4f5c00bb1e47c76e8aac7e2d'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
