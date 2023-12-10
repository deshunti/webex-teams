# Fill in this file with the code to create a new room from the Webex Teams exercise
import requests

access_token = 'ODU0YmFjYWItZGE2OS00YzEzLWE0NmMtYjU3MTE1NTBkNmJkMGE2MTZmMmQtNWE4_P0A1_36820416-bfff-433a-84bf-39585b2b3f67'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'DevNet Associate Training!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
