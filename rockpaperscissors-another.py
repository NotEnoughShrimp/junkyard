import random, re 

win_con = {
    "rock":"scissors",
    "paper":"rock",
    "scissors":"paper"
}

def winner(player,computer):
    if player == computer:
        return "It's a draw"
    elif win_con[player] == computer:
        return "player wins"
    else:
        return "computer wins"
    
player_score = 0
computer_score = 0

while True:
    player = input("enter rock, paper, scissors: ")
    computer = random.choice(list(win_con.keys()))
    print(f"computer: {computer}")

    results = winner(player,computer)
    print(results)

    if re.search('computer',results):
        computer_score += 1
    elif re.search('player',results):
        player_score += 1
    restart = input("play again? 'y' to restart 'n' to quit\n")
    if restart != 'y':
        print(f"finale score:\nPlayer: {player_score}\nComputer: {computer_score}")
        break
