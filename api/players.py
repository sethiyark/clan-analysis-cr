import json

import requests

from config import *


def get_player_details():
    with open('players.json') as player_json:
        return json.load(player_json)


def get_player_details_api():
    # TODO: Find average card levels for players
    response = requests.get(API_URL + '/clans/' + CLAN_TAG + '/members', headers=HEADERS).json()
    player_details = {}
    for player in response['items']:
        trusted = False
        if player['tag'] in TRUSTED:
            trusted = True
        player_details[player['tag']] = {
            'name': player['name'],
            'role': player['role'],
            'level': player['expLevel'],
            'donation': player['donations'],
            'received': player['donationsReceived'],
            'trusted': trusted
        }
    for key, _ in player_details.items():
        member = requests.get(API_URL + '/players/' + key.replace('#', ' '), headers=HEADERS).json()
        player_details[key]['trophies'] = member['trophies']
        player_details[key]['bestTrophies'] = member['bestTrophies']
        player_details[key]['wins'] = member['wins']
        player_details[key]['losses'] = member['losses']
        player_details[key]['battleCount'] = member['battleCount']
        player_details[key]['winsThreeCrown'] = member['threeCrownWins']
        player_details[key]['challengeMax'] = member['challengeMaxWins']
        player_details[key]['totalDonations'] = member['totalDonations']
        player_details[key]['warWins'] = member['warDayWins']
        player_details[key]['clanCards'] = member['clanCardsCollected']
    # member = requests.get(API_URL + '/players/' + ' 2YGJ8U0Q', headers=HEADERS).json()
    # for k, _ in member.items():
    #     print(k)
    # print(member)
    return player_details


def generate_player_details():
    player_details = get_player_details_api()
    with open('players.json', 'w') as player_file:
        json.dump(player_details, player_file)


if __name__ == '__main__':
    print(get_player_details())
