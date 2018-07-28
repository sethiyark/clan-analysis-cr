from api.clan import get_clan_info
from api.players import get_player_details

if __name__ == '__main__':
    clan_info = get_clan_info()
    player_details = get_player_details()

    print(clan_info)
    print(player_details)
