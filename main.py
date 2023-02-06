import random
import room
import game_play
from player import Player
import mfr

def start_main_gamplay(state):
    state["player"].survival_rounds += 1
    # enter room
    room.enter_room(state["player"].current_room)

    # MFR events
    mfr.encounter_mfr(state["player"])

    if game_play.lose(state["player"]):
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
    "player": Player(),
    "win_room": random.randint(0, len(room.rooms) - 1),
})