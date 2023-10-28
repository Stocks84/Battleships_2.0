def game_board():
    """
    Game_board creates the board.
    """
    print("Battleships")
    print(" 0 1 2 3 4 5 6 7")

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