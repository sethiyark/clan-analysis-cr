import json

import requests

from config import *


def get_player_details():
    with open('players.json') as player_json:
        return json.load(player_json)


def get_player_details_api():
    response = requests.get(API_URL + '/clans/' + CLAN_TAG + '/members', headers=HEADERS).json()
    player_details = {}
    for player in response['items']:
        is_trusted = False
        if player['tag'] in TRUSTED:
            is_trusted = True
        player_details[player['tag']] = {
            'name': player['name'],
            'role': player['role'],
            'level': player['expLevel'],
            'donation': player['donations'],
            'received': player['donationsReceived'],
            'trusted': is_trusted
        }
    for key, _ in player_details.items():
        member = requests.get(API_URL + '/players/' + key.replace('#', ' '), headers=HEADERS).json()
        cards = {'common': [], 'rare': [], 'epic': [], 'legendary': []}
        for c in member['cards']:
            if c['maxLevel'] == 13:
                cards['common'].append(c['level'])
            elif c['maxLevel'] == 11:
                cards['rare'].append(c['level'])
            elif c['maxLevel'] == 8:
                cards['epic'].append(c['level'])
            else:
                cards['legendary'].append(c['level'])
            player_details[key]['averageLevel'] = {'common': 0, 'rare': 0, 'epic': 0, 'legendary': 0}
        for k, v in cards.items():
            total = 0
            for i in v:
                total += i
            player_details[key]['averageLevel'][k] = total / len(v)
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
    return player_details


def generate_player_details():
    player_details = get_player_details_api()
    with open('players.json', 'w') as player_file:
        json.dump(player_details, player_file)


if __name__ == '__main__':
    print(generate_player_details())
