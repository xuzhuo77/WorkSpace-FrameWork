import requests

url = "http://localhost:9030/safety/auth/loginSafetyValidate"

payload = "{\n    \"username\": \"admin\",\n    \"password\": \"WE@3dfsa\"\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
