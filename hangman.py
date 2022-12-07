import pygame
from pygame.locals import *
import random

"""establishes the core visual elements of the game
	Horizontal line: line where the letters are placed
	Hanger: the line drawn hanger
	Wrong letter board: where the incorrect letters will be shown"""

width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
color = (20, 0, 0)
# Changing surface color
screen.fill(color)
pygame.display.flip()

   
pygame.init()
states = "Alabama Alaska Arizona Arkansas California Colorado Connecticut Delaware Florida Georgia Hawaii Idaho Illinois Indiana Iowa Kansas Kentucky Louisiana Maine Maryland Massachusetts Michigan Minnesota Mississippi Missouri Montana Nebraska Nevada NewHampshire NewJersey NewMexico NewYork NorthCarolina NorthDakota Ohio Oregon Oklahoma Pennsylvania RhodeIsland SouthCarolina SouthDakota Tennessee Texas Utah Vermont Virginia Washington WestVirginia Wisconsin Wyoming".split()

class StateName():
    "randomly selects a state name"
    def get_state(wordList):
        state_index = random.randint(0, len(wordList) - 1 )
        return wordList[state_index]

class hint(StateName):
    "Gives you a hint depending on the state"

class letter():
    guess = input('Guess a letter: ')
    "if guess is not a letter in the state name add a part of the stick man"

class wrongletter(letter):
    "letters that are incorrect will be shown in the incorrect box"

class stickman(letter):
		
    """if guess is not a letter in the state name add a part of the stick man
    the stickman has 6 body parts ( 1 head, 2 arms, 2 legs, 1 chest)"""


	
"when the stick man is fully drawn = when theres 6 incorrect guesses"




StateName()
letter()
hint()
