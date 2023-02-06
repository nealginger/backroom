import game_play
import random

class Player:
    sanity = 0
    current_room = 0
    survival_rounds = 0

    def __init__(self):
        difficulty = game_play.get_difficulty()
        self.sanity = self.get_player_sanity(difficulty)
        self.current_room = random.randint(0, 1)

    def get_player_sanity(self, difficulty):
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