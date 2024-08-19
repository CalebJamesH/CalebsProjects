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

    

# Will return whether or not the file exists
file = 'games.txt'
if fileExists(file):
    print("File Found.")
else:
    print("File does not exist")
    createFile(file)

while True:
    print("MENU")
    print("1 - Register new item")
    print("2 - Lister Register")
    print("3 - Exit")
    
    op = valid_int("Pick the desired option: ", 1, 3)
    if (op == 1):
        print("Add new item selected...\n")
        gameName = input("Game's name: ")
        videogameName = input("Videogame's name: ")
        registerGame(file, gameName, videogameName)   
    elif(op == 2):
        print("list registry selected...\n")
        listFile(file)
    elif(op == 3):
        print("leaving program...\n")
        break