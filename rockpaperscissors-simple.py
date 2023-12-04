import random

"""
rock - 1, paper - 2, scissors - 3
- player enters an int input, computer uses a random.choice method to pick from selection.
- if player input and random choice are equal = "draw"
- else if player input and random choice: (1 == 2, 2 == 3,
or 3 == 1) = "player loss"
- else = "player win"

uses 
"""

selection = [1,2,3]

player_choice = int(input("Rock [1] Paper [2] Scissors [3]\n> "))
computer = random.choice(selection)

if player_choice == computer:
    print(f"player: [{player_choice}] computer: [{computer}]")
    print("draw")
elif (player_choice == 1 and computer == 2) or\
     (player_choice == 2 and computer == 3) or\
     (player_choice == 3 and computer == 1):
        print(f"player: [{player_choice}] computer: [{computer}]")
        print("you lose")
else:
    print(f"player: [{player_choice}] computer: [{computer}]")
    print("you win")

