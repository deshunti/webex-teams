# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json

access_token = 'ODU0YmFjYWItZGE2OS00YzEzLWE0NmMtYjU3MTE1NTBkNmJkMGE2MTZmMmQtNWE4_P0A1_36820416-bfff-433a-84bf-39585b2b3f67'
url = 'https://webexapis.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
      'email': 'websterdeshunti@gmail.com'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))