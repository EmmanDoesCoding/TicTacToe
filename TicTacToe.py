import random
import time
from IPython.display import clear_output

AIScore = 0
UserScore = 0
 
def clear():
  time.sleep(1)
  clear_output()

def playagain():
  while True:
    again = input("Want to play again? [Y/N]: ").capitalize()
    if again == "Y":
      clear()
      print("Game Restart!")
      clear()
      game()
      break
    elif again == "N":
      clear()
      print("Thanks for playing")
      break
    else:
      clear()
      print("Really?")

def BoardLayout(Board):
    print(\
f"""
\t [{Board[0]}] [{Board[1]}] [{Board[2]}]
\t [{Board[3]}] [{Board[4]}] [{Board[5]}]
\t [{Board[6]}] [{Board[7]}] [{Board[8]}]
"""
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
  global UserScore
  global AIScore

  Board = [" ", " ", " ",
            " ", " ", " ",
            " ", " ", " "]
    
  while True:
      Choose = input("Which would you like? [O or X]: ").capitalize()

      if Choose == "O":
          User = "⭕"
          Comp = "✖️"
          clear()
          break
      elif Choose == "X":
          User = "✖️"
          Comp = "⭕"
          clear()
          break
      else:
          print("Stupid motherfucker, Wrong icon")

  print("Game Start!")
  clear()
  BoardLayout(Board)
    
  GameRun = True

  while GameRun:
      #User turn
      spot(Board, User, Comp)
      if Win(Board):
        UserScore += 1
        print("User wins!")
        print(f"USER: {UserScore}")
        print(f"AI: {AIScore}")
        GameRun = False
        playagain()
        break
        
      if " " not in Board:
        print("It's a DRAW!")
        break

      enemyspot(Board, User, Comp, location)
      if Win(Board):
        AIScore += 1
        print("AI wins!")
        print(f"USER: {UserScore}")
        print(f"AI: {AIScore}")
        GameRun = False
        playagain()
        break


def spot(Board, User, Comp):
    while True:
        global location
        location = int(input("Where do you want to place your piece? "))
        if location in range(0, 9):
            if Board[location] == " ":
                clear()
                Board[location] = User
                BoardLayout(Board)
                clear()
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
                clear()
                BoardLayout(Board)
                break
    else:
        Win()

game()
