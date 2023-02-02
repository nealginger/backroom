import time

def get_difficulty():
    difficulty = input("Type 1-3 to pick a gamemode: \n1 - easy\n2 - normal(default)\n3 - hard\n")
    difficulties = {"1", "2", "3", "i'm a baby duh", "creators only"}
    if not difficulty in difficulties:
        difficulty = "4"
    print(difficulty)
    return difficulty

def start_game():
    print("One day you are happily playing at the park, but when you get pushed down the slide to hard you noclip out of reality")

def lose(player_sanity, suvival_rounds):
    if player_sanity <= 0:
        print("You lost all your sanity")
        time.sleep(1)
        print(".....")
        time.sleep(1)
        print("You lost control of your mind now you are lost forever in backrooms")
        time.sleep(1)
        print("you survived for " + str(suvival_rounds) + " levels")
        return True
    return False

def win(exits, direction, win_room):
    current_room = exits[direction]
    if current_room == win_room:
        print ("Congrats! You have escaped the backroom!!!")
        return True
    return False

def choose_direction(exits):
    # choose direction
    direction = input("")
    if direction in exits.keys():
        return direction
    else:
        print ("There is no such exit here, please choose again")
        return choose_direction(exits)