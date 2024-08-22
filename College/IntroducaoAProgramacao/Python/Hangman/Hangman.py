import Game as g # Game
import Exercise3 as FH # File handler

def show_menu():
    print("="*30)
    print(" " * 10 + "HANGMAN")
    print("="*30)
    print("\n1 - PLAY")
    print("2 - SCORE")
    print("3 - EXIT")
    print("="*30)
    
file = 'score.txt'
if FH.fileExists(file):
    print("File has been found.")
else:
    print("File doesn't exist.")
    FH.createFile(file)
    
while True:
    show_menu()
    option = int(input('Choose your option (1/2/3): '))
    
    match(option):
        case 1:
            print('Start game!')
            g.play()
        case 2:
            print('SCORE')
            data = FH.listFile('score.txt')
            if not data:
                print('No score')
            else:
                i = 1
                for player in data:
                    print(f"{i} -> {player[0]}, Points: {player[1]:[-1]}")
        case 3:
            print('Exiting game. Goodbye!')
            break
        case _:
            print('Invalid option. Choose another one.')
        
        
        