import random
import room
import game_play
import player
import mfr

def start_main_gamplay(state):
    state["suvival_rounds"] += 1
    # enter room
    room.enter_room(state["current_room"])

    # MFR events
    state["player_sanity"] = mfr.encounter_mfr(state["player_sanity"])

    if game_play.lose(state["player_sanity"], state["suvival_rounds"]):
        return

    # generate exits
    exits = room.get_random_exits()

    # choose direction
    direction = game_play.choose_direction(exits)

    # go to next room
    if game_play.win(exits, direction, state["win_room"]):
        return

    start_main_gamplay(state)


# game start here
game_play.start_game()
start_main_gamplay({
    "player_sanity": player.get_player_sanity(game_play.get_difficulty()),
    "current_room": random.randint(0, 1),
    "win_room": random.randint(0, len(room.rooms) - 1),
    "suvival_rounds": 0
})