# come back and change print and input messages
def get_shot(no_double_hit):
    """
    """
    ok = "n"
    while ok == "n":
        try:
            shot = input("please enter your guess")
            shot = int(shot)
            if shot < 0 or shot> 63:
                print("incorrect number, please try again")
            elif shot in no_double_hit:
                print("NO double hits")
            else:
                ok == "y"
                break
        except:
            print("incorrect, try again")

    return shot


def game_board(hit,miss,sunk):
    """
    Game_board creates the board.
    """
    print("       Battleships\n")
    print("     0  1  2  3  4  5  6  7")

    place = 0
    for x in range(8):
        row = ""
        for y in range(8):
            ch = " _ "
            if place in miss:
                ch = " x "
            elif place in hit:
                ch = " o "
            elif place in sunk:
                ch = " O "
            

            row = row + ch
            place = place + 1
        print(x," ",row)


def check_shot(shot,boat1,boat2,hit,miss,sunk):
    """
    """
    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
        else:
            sunk.append(shot)

    elif shot in boat2:
        boat2.remove(shot)
        if len(boat2) > 0:
            hit.append(shot)
        else:
            sunk.append(shot)
    else:
        miss.append(shot)

    return boat1,boat2,hit,miss,sunk

boat1 = [45,46,47]
boat2 = [5,6,7]
hit = []
miss = []
sunk = []

for i in range(10):
    no_double_hit = hit + miss + sunk
    shot = get_shot(no_double_hit)
    boat1,boat2,hit,miss,sunk = check_shot(shot,boat1,boat2,hit,miss,sunk)
    game_board(hit,miss,sunk)

    if len(boat1) < 1 and len(boat2) < 1:
        print("Winner")
        break
print("game over")