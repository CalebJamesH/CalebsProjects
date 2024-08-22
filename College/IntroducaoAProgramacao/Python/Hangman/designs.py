def print_secret_word(word, correct_guesses):
    guess = ""
    for letter in word:
        if letter in correct_guesses:
            guess += letter
        else:
            guess += '\u2588'
    print(f"GUESS ({len(word)} letters): ")
    for letter in guess:
        print(f"{letter} ", end='')
    print()

    return guess
    
def draw_noose(errors):
    score = 1000
    
    print("X==:==")
    print("X  :  ")
    if errors >= 1:
        print('X  0  ')
        score = 800
    else:
        print('X')

    line2 = ''
    if errors == 2:
        line2 = '  | '
        score = 600
    elif errors == 3:
        line2 = " /| "    
        score = 400
    elif errors >= 4:
        line2 = " /|\ "
        score = 200
    print(f"X{line2}")
    
    line3 = ''
    if errors == 5:
        line3 += " / "
        score = 100
    elif errors >= 6:
        line3 += " / \ "
        score = 0 
    print(f"X{line3}")

    print(f"x\n=======")

    return score
        
            
        
    