import random
def BoardLayout(Board):
    print(\
        f"""
        [{Board[0]}] [{Board[1]}] [{Board[2]}]
        [{Board[3]}] [{Board[4]}] [{Board[5]}]
        [{Board[6]}] [{Board[7]}] [{Board[8]}] """
    )

def Win(Board):
    # All 8 ways to win
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]

    for condition in win_conditions:
        # Check if all three positions in the condition are the same and NOT empty
        if Board[condition[0]] == Board[condition[1]] == Board[condition[2]] != " ":
            return Board[condition[0]]  # Returns 'X' or 'O' as the winner

    return None  # No winner yet

def game():
    Board = [" ", " ", " ",
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
            print("Stupid motherfucker, Wrong icon")

    print("Game Start!")
    BoardLayout(Board)
    
    GameRun = True

    while GameRun:
        #User turn
        spot(Board, User, Comp)
        if Win(Board):
            print("User wins!")
            GameRun = False
            break
        
        if " " not in Board:
            print("It's a DRAW!")
            break

        enemyspot(Board, User, Comp, location)
        if Win(Board):
            print("AI wins!")
            GameRun = False
            break


def spot(Board, User, Comp):
    while True:
        global location
        location = int(input("Where do you want to place your piece? "))
        if location in range(0, 8):
            if Board[location] == " ":
                Board[location] = User
                BoardLayout(Board)
                break
            else:
                print("Choose another number")
        else:
            print("Stupid motherfucker")
            

def enemyspot(Board, User, Comp, location):
    if " " in Board:
        while True:
            enemy = random.randint(0,8)

            if Board[enemy] == " ":
                Board[enemy] = Comp
                BoardLayout(Board)
                break
    else:
        Win()

game()
