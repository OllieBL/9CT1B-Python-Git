# this file is the main file for the program
#-----------------------------------------
# import the required modules
import random # import the random module
import time # import the time module

# create constant variables for the program
gameOver = False # create a variable to control the game loop
playerHealth = 100 # eate a variable to store the player's health
playerAttack = 10 # create a variable to store the player's attack power
x = 0 # I use this for while loops 

#----------------------------------------- SET UP THE GAME BOARD -----------------------------------------
#create a 5x5 game board. 0 = empty, 1 = player, 2 = enemy, 3 = treasure, 4 = trap, 5 = exit, 6 = boss, 7=visited
gameBoard = [[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]]


# make the objects non stackable
def checkStacking(object):
    global gameBoard
    objectX = random.randint(0, 4)
    objectY = random.randint(0, 4)
    while gameBoard[objectX][objectY] != 0:
        objectX = random.randint(0, 4)
        objectY = random.randint(0, 4)
    gameBoard[objectX][objectY] = object

# place the player in the middle of the game board
playerX = 2
playerY = 2
gameBoard[playerX][playerY] = 1

# place the exit in a random location
checkStacking(5)

# place an enemy on the map
checkStacking(2)

# place two treasure spots
while x < 2:
    checkStacking(3)
    x += 1

print(gameBoard)

# ----------------------------------------- SET UP THE FUNCTIONS -----------------------------------------
# create the def() functions for the program here
def printBoard():
    for row in gameBoard:
        print(row)

def movePlayer():
    global playerX, playerY
    direction = input('Enter the direction you want to move (N,S,E,W): ')
    direction = direction.lower()
    if direction == 'n':
        if playerX > 0:
            gameBoard[playerX][playerY] = 7
            playerX -= 1
            gameBoard[playerX][playerY] = 1
        else:
            print('You cannot move in that direction')
    elif direction == 's':
        if playerX < 4:
            gameBoard[playerX][playerY] = 7
            playerX += 1
            gameBoard[playerX][playerY] = 1
        else:
            print('You cannot move in that direction')
    elif direction == 'e':
        if playerY < 4:
            gameBoard[playerX][playerY] = 7
            playerY += 1
            gameBoard[playerX][playerY] = 1
        else:
            print('You cannot move in that direction')
    elif direction == 'w':
        if playerY > 0:
            gameBoard[playerX][playerY] = 7
            playerY -= 1
            gameBoard[playerX][playerY] = 1
        else:
            print('You cannot move in that direction')
    else:
        print('I do not understand that direction')
    

#check if the player has reached the exit
def checkExit():
    global gameOver
    if gameBoard[playerX][playerY] == 5:
        print('You have reached the exit')
        gameOver = True

# ----------------------------------------- MAIN LOOP -----------------------------------------
# create the main loop for the program here
while gameOver == False:
    printBoard()
    movePlayer()
    checkExit()
    time.sleep(1)
print('Game over!')