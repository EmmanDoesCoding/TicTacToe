def game():
    board = [" ", " ", " ",
            " ", " ", " ",
            " ", " ", " "]
    
    while True:
        Choose = input("Which would you like? [O or X]: ").capitalize()

        if Choose == "O":
            User = "O"
            Comp = "X"
            break
        elif Choose == "X":
            User = "X"
            Comp = "O"
            break
        else:
            print("Stupid motherfucker")

    print(\
        f"""
        [{board[0]}] [{board[1]}] [{board[2]}]
        [{board[3]}] [{board[4]}] [{board[5]}]
        [{board[6]}] [{board[7]}] [{board[8]}]
        """
    )

game()