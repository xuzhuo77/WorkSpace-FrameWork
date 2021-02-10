import requests
import json
url = "http://localhost:9030/safety/api/suppliesWarehouse/statisticsBenchmark"

payload = "{\n\n    \"regionId\"    :210203000000\n\n          \n}"
headers = {
  'Content-Type': 'application/json',
  'access_token': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjciLCJ1c2VyR3VpZCI6IjBjN2ZmNDgzLTBlMGYtNDU2ZS1iYWFiLWQ3YTdlNDJmNjA4MSIsImV4cCI6MTU5MTkzMDUxN30.HSKmweJZmTH8jrHcaXrX-54aJSWA6q-cKJu4JQn2lak'
}

response = requests.request("POST", url, headers=headers, data = payload)
data=response.text.encode('utf-8')

print (json.dumps(data, sort_keys=True, indent=2) )
