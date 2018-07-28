from config import RATING_CONFIG


def get_scores(player, clan_score, donations):
    player_score = {
        'role': RATING_CONFIG['role'](player['role']),
        'levelScore': RATING_CONFIG['levelScore'](player['level']),
        'donationScore': RATING_CONFIG['donationScore'](player['donation'], player['received'], donations),
        'trusted': RATING_CONFIG['trusted'](player['trusted']),
        'trophies': RATING_CONFIG['trophies'](player['trophies']),
        'bestTrophies': RATING_CONFIG['bestTrophies'](player['trophies'], clan_score),
        'wins': RATING_CONFIG['wins'](player['wins'], player['losses'], player['winsThreeCrown'],
                                      player['warWins'], player['challengeMax']),
        'commons': RATING_CONFIG['commons'](player['averageLevel']['common']),
        'rares': RATING_CONFIG['rares'](player['averageLevel']['rare']),
        'epics': RATING_CONFIG['epics'](player['averageLevel']['epic']),
        'legendaries': RATING_CONFIG['legendaries'](player['averageLevel']['legendary'])
    }
    return player_score


if __name__ == '__main__':
    for _ in RATING_CONFIG.keys():
        print(_)
