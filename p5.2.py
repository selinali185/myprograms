# snakes and ladders
square = 1
while True: 
    roll = int(input("enter dice roll data: "))

    if square + roll == 100:
        print(f"you are now on sqaure {square+roll}")
        print("you win")
        break
    elif square + roll < 100:
        new_position = square + roll
        game_dict = {
            9:34,
            54:19,
            40:64,
            90:48,
            67:86,
            99:77
        }
        if new_position in game_dict:
            square = game_dict[new_position]
        else: 
            square + roll

