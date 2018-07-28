CLAN_TAG = ' GQQQY9'

API_URL = 'https://api.clashroyale.com/v1'

API_TOKEN = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjEzMjRjNTQ5LTA5OTMtNDdjOC04MjU4LTRiYTRhMWUwYjk0OCIsImlhdCI6MTUzMjc1MzEyNiwic3ViIjoiZGV2ZWxvcGVyL2VhNDQyNGQ3LTkwMDQtNTUwOS04Y2FkLTMyNjJmYjI4NzhmMCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMDMuMjU1LjIyNy4xNzkiXSwidHlwZSI6ImNsaWVudCJ9XX0.MIBkuB8aF0BUjry-ExKldMEDdGcCv1j6rhABPNIyDQjffpKPdMHuXpCwsreAzV__XKoIvCB9_1NKK-mfG3j0hQ'

HEADERS = {
    'authorization': API_TOKEN,
    'Accept': 'application/json'
}

TRUSTED = ['#2YGJ8U0Q', '#YPY0LGVU', '#2P8UQY2YP', '#2RRRCUVC', '#202JJ9PPJ', '#P0RLVUYU', '#2LCCJQJLY', '#UR9GV2CR',
           '#RQUVJ2JL', '#YCL9UJR', '#20UUL8GCQ', '#VYQPL82Y', '#92G8YPRV', '#20RYP2GQP', '#8VUL0LLR9', '#9UQQCV8Q',
           '#22UPPC29U', '#YLVQUQYJ', '#PRPJCCQ9', '#2VYCLR2P', '#9Y9L0P9V']

RATING_CONFIG = {
    'role': lambda role: 60 if role == 'leader' else 30 if role == 'coLeader' else 10 if role == 'elder' else 0,
    'levelScore': lambda level: (level / 13) * 150,
    'donationScore': lambda donated, received, donations: (donated + received) / (donations + 1) * 500,
    'trusted': lambda trusted: 150 if trusted else 0,
    'trophies': lambda trophies: 160 + (trophies - 4000) / 3 if trophies >= 4000 else 110 + (
            trophies - 3800) / 4 if trophies >= 3800 else 50 + (
            trophies - 3500) / 5 if trophies >= 3500 else 25 if trophies >= 3000 else 10,
    'bestTrophies': lambda trophies, clan_score: 200 ** (trophies / clan_score * 10),
    'wins': lambda wins, looses, wins_three_crown, war_wins, challenge_max: ((wins + wins_three_crown) / (
            looses + wins + wins_three_crown)) * (war_wins * 3 + 1) * (challenge_max + 1),
    'commons': lambda average: 1.75 ** average,
    'rares': lambda average: 2 ** average,
    'epics': lambda average: 4 ** average,
    'legendaries': lambda average: 8.5 ** average
}
