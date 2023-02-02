

def get_player_sanity(difficulty):
    player_sanity_difficulty_map = {
        "1": 4200,
        "2": 2100,
        "3": 1001,
        "4": 2.1, 
        "i'm a baby duh": 9223372036854775807999,
        "creators only": 999999999999999999999999999999999999999999999999,
        "MEG explorer": 100001
    }
    player_sanity = player_sanity_difficulty_map[difficulty]
    print("You've got " + str(player_sanity) + " sanity")
    return player_sanity