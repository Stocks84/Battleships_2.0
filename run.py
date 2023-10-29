from random import randrange


def check_ok(boat, taken):
    """
    """
    for i in range(len(boat)):
        num = boat[i]
        if num in taken:
            boat = [- 1]
            break
        elif num < 0 or num > 99:
            boat = [- 1]
            break
        elif num % 10 == 9 and i < len(boat) - 1:
            if boat[i + 1] % 10 == 0:
                boat = [- 1]
            break

    return boat


def check_boat(b, start, direct, taken):
    """
    """
    boat = []
    if direct == 1:
        for i in range(b):
            boat.append(start - i * 10)
            boat = check_ok(boat, taken)
    elif direct == 2:
        for i in range(b):
            boat.append(start + i)
            boat = check_ok(boat, taken)
    elif direct == 3:
        for i in range(b):
            boat.append(start + i * 10)
            boat = check_ok(boat, taken)
    elif direct == 4:
        for i in range(b):
            boat.append(start - i)
            boat = check_ok(boat, taken)
    return boat


def create_boats():
    taken = []
    ships = []
    boats = [4,3,3,2,1]
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1,4)
            print(b, boat_start, boat_direction)
            boat = check_boat(b, boat_start, boat_direction, taken)
        ships.append(boat)
        taken = taken + boat
        print(ships)

    return ships, taken

def game_board(taken):
    """
    Game_board creates the board.
    """
    print("       Battleships\n")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in taken:
                ch = " x "
            row = row + ch
            place = place + 1
        print(x," ",row)

boats, taken = create_boats()
game_board(taken)
# come back and change print and input messages
# def get_shot(no_double_hit):
#     """
#     """
#     ok = "n"
#     while ok == "n":
#         try:
#             shot = input("please enter your guess")
#             shot = int(shot)
#             if shot < 0 or shot> 99:
#                 print("incorrect number, please try again")
#             elif shot in no_double_hit:
#                 print("NO double hits")
#             else:
#                 ok == "y"
#                 break
#         except:
#             print("incorrect, try again")

#     return shot


# def game_board(hit, miss, sunk):
#     """
#     Game_board creates the board.
#     """
#     print("       Battleships\n")
#     print("     0  1  2  3  4  5  6  7  8  9")

#     place = 0
#     for x in range(10):
#         row = ""
#         for y in range(10):
#             ch = " _ "
#             if place in miss:
#                 ch = " x "
#             elif place in hit:
#                 ch = " o "
#             elif place in sunk:
#                 ch = " O "
            

#             row = row + ch
#             place = place + 1
#         print(x," ",row)


# def check_shot(shot, boat1, boat2, hit, miss, sunk):
#     """
#     """
#     if shot in boat1:
#         boat1.remove(shot)
#         if len(boat1) > 0:
#             hit.append(shot)
#         else:
#             sunk.append(shot)

#     elif shot in boat2:
#         boat2.remove(shot)
#         if len(boat2) > 0:
#             hit.append(shot)
#         else:
#             sunk.append(shot)
#     else:
#         miss.append(shot)

#     return boat1, boat2, hit, miss, sunk

# boat1 = [45,46,47]
# boat2 = [5,6,7]
# hit = []
# miss = []
# sunk = []

# for i in range(10):
#     no_double_hit = hit + miss + sunk
#     shot = get_shot(no_double_hit)
#     boat1,boat2,hit,miss,sunk = check_shot(shot, boat1, boat2, hit, miss, sunk)
#     game_board(hit, miss, sunk)

#     if len(boat1) < 1 and len(boat2) < 1:
#         print("Winner")
#         break
# print("game over")