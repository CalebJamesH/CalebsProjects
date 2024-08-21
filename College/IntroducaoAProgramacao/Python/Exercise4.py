import random
index = ("Rock", "Paper", "Scissors")
computer_wins = 0
player_wins = 0 
draws = 0

random_index = random.randint(0, 2)

while True:
    play = input("Would you like to play? ")
    if (play.lower() == 'no'):
        break
    while True:
        player_choice = input("Select Rock, Paper, or Scissors: ")
        while True:
            if player_choice in index:
                break
            else: 
                player_choice = input("What you put is invalid. Select Rock, Paper, or Scissors: ")
        computer_choice = index[random_index]
        if (computer_choice == index[0] and player_choice == index[2] or computer_choice == index[1] and player_choice == index[0] or computer_choice == index[2] and player_choice == index[1]):
            computer_wins += 1
            print(f"You chose {player_choice} and computer chose {computer_choice}. You lost this round. Wins = {player_wins}, losses = {computer_wins}, draws = {draws}")
        elif (player_choice == index[0] and computer_choice == index[2] or player_choice == index[1] and computer_choice == index[0] or player_choice == index[2] and computer_choice == index[1]):
            player_wins += 1
            print(f"You chose {player_choice} and computer chose {computer_choice}. You won this round. Wins = {player_wins}, losses = {computer_wins}, draws = {draws}")
        else:
            draws += 1
            print(f"You chose {player_choice} and computer chose {computer_choice}. You tied this round. Wins = {player_wins}, losses = {computer_wins}, draws = {draws}")
        
        if (player_wins == 3 or computer_wins == 3):
            break
        
    if (computer_wins == 3):
        print(f"Sorry, you lose. Wins: {player_wins}, losses: {computer_wins}, draws: {draws}")
        break
    else: 
        print(f"Good job, you won! Wins: {player_wins}, losses: {computer_wins}, draws: {draws}")