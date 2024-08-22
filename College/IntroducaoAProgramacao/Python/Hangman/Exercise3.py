# Make sure that the person selects a valid input of 1-3
def valid_int(question, min, max):
    x = int(input(question))
    while((x < min) or (x > max)):
        x = int(input(question))
    return x

# Checking to see if the File Exists by opening it then closing it.
def fileExists(fileName):
    try:
        a = open(fileName, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True
    
# Creating the file if the file does not exists
def createFile(fileName):
    try:
        a = open(fileName, 'wt+')
        a.close()
    except:
        print("Error creating file")
    else: 
        print(f"File {fileName} created with success.")
        

# Function to register a game     
def registerGame(fileName, gameName, videogameName):
    try:
        a = open(fileName, "at")
    except:
        print("Error")
    else: 
        a.write(f"{gameName};{videogameName}\n")
    finally:
        a.close()
    
      
def listFile(fileName):
    try:
        a = open(fileName, "rt")
    except:
        print("Error")
    else:
        print(a.read())
        data = a.readlines()
    finally:
        a.close()
        return data
        
#These function is used for Hangman
def insert_score(fileName, playerName, score):
    try:
        a = open(fileName, 'at')
    except:
        print('Error opening the file')
    else:
        a.write('{}:{}\n'.format(playerName, score))
    finally:
        a.close()
        

def openFileForReading(fileName):
    try: 
        a = open(fileName, 'r')
    except:
        print("Couldn't open the file to read.")
    else: 
        print(f"File {fileName} opened successfully!\n")
        return a

