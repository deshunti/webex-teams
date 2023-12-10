# Fill in this file with the code to create a room membership from the Webex Teams exercise
import requests

access_token = 'ODU0YmFjYWItZGE2OS00YzEzLWE0NmMtYjU3MTE1NTBkNmJkMGE2MTZmMmQtNWE4_P0A1_36820416-bfff-433a-84bf-39585b2b3f67'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZjg3NGU2NDAtOTcwNy0xMWVlLTk2MWYtZTUwNTc5ODE4MDRl'
person_email = 'escaleraeber@gmail.com'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())