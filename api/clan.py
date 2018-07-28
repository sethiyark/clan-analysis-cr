import requests

from config import *


def get_clan_info():
    response = requests.get(API_URL + '/clans/' + CLAN_TAG, headers=HEADERS).json()
    return {'name': response['name'], 'score': response['clanScore'], 'donations': response['donationsPerWeek']}


if __name__ == '__main__':
    print(get_clan_info())
