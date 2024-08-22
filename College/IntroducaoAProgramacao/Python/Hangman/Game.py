import designs as ds
import Exercise3 as FH
from random import choice

def play():
    word_list = list()
    file = FH.openFileForReading('words.txt')
    for line in file:
        word = line.strip()
        word_list.append(word)
        
    random_word = choice(word_list)

    for x in range(50):
        print()
        
    typed = []
    correct_guesses = []
    errors = 0

    name = input('Who is playing? ')

    while True:
        guess = ds.print_secret_word(random_word, correct_guesses)
        
        
        if guess == random_word:
            print("You win!")
            break
        
        
        tries = input("\nType a letter:").lower().strip()
        if tries in typed:
            print("You already used this letter.")
            continue
        else: 
            typed += tries
            if tries in random_word:
                correct_guesses += tries
            else: 
                errors += 1
                print("You got it wrong.")
                
        score = ds.draw_noose(errors)

        if errors == 6:
            print("You were hanged!")
            print(f"The correct word was {random_word}")
            break
        
    FH.insert_score("score.txt", name, score)    
    
    
    
    
    
    
    