# Fill in this file with the authentication code from the Webex Teams exercise
import requests
import json

access_token = 'NzhmYThkOTUtNGU2OS00MmFmLTgzNTYtNzRiYzg2MjBkMGZkZDFkZTE0OTMtMjUw_P0A1_36820416-bfff-433a-84bf-39585b2b3f67'
url = 'https://webexapis.com/v1/people/me'

headers = {
    'Authorization': 'Bearer {} ' .format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
