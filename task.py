import requests

url = "https://apihub.document360.io/v2/Drive/Folders"

headers = {
 "Authorization: Bearer YOUR_PROJECT_API_TOKEN",  # Replace with actual token
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

# Check for errors
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")
import requests

url = "https://apihub.document360.io/v2/Drive/Folders"
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

data = {
    "name": "MyNewFolder",
    "parentFolderId": None  # or set to a valid folder ID
}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())  # Get folder ID and name

