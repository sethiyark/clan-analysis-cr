import csv
import json
import math

from api.clan import get_clan_info
from api.players import get_player_details
from lib import get_scores

if __name__ == '__main__':
    clan_info = get_clan_info()
    player_details = get_player_details()

    # print(clan_info)
    scores = {}
    for v in player_details.values():
        scores[v['name']] = get_scores(v, clan_info['score'], clan_info['donations'])
    total_score = {}
    for k, values in scores.items():
        total_score[k] = 0
        for v in values.values():
            total_score[k] += v
    # print(total_score)
    with open('player_scores.json', 'w') as score_file:
        json.dump(scores, score_file)

    ALFA = max(total_score.values())
    PHI = min(total_score.values())
    BETA = 100
    X = BETA / (ALFA - PHI)
    B = (- PHI * BETA) / (ALFA - PHI)
    scaled_score = {}
    for k, v in total_score.items():
        scaled_score[k] = math.floor((X * v) + B)
    print(scaled_score)
    stat_file = csv.writer(open('stat_clan.csv', 'w'))

    stat_file.writerow(
        ['Name', 'Level Score', 'Donation Score', 'Trophies Score', 'Wins Score', 'Commons', 'Rares', 'Epics',
         'Legendaries', 'Scaled Score'])
    for k in scores.keys():
        stat_file.writerow([
            str(k).encode('utf-8'),
            scores[k]['levelScore'],
            scores[k]['donationScore'],
            scores[k]['trophies'],
            scores[k]['wins'],
            scores[k]['commons'],
            scores[k]['rares'],
            scores[k]['epics'],
            scores[k]['legendaries'],
            scaled_score[k]
        ])
    # for k, v in player_details.items():
    #     print(k, end=": ")
    #     print(v['name'])
