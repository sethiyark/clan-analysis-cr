import requests

from config import *

headers = {
    'authorization': API_TOKEN,
    'Accept': 'application/json'
}

response = requests.get(API_URL + '/' + CLAN_TAG, headers=headers)

clan_info = response.json()
print(clan_info)
