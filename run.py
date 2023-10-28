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


def game_board(hit,miss,elim):
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
            elif place in elim:
                ch = " O "
            

            row = row + ch
            place = place + 1
        print(x," ",row)


hit = [21,22]
miss = [20,24,12,13]
elim = [23]

no_double_hit = hit + miss + elim
shot = get_shot(no_double_hit)
game_board(hit,miss,elim)