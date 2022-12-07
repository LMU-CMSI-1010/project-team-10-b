import pygame
from pygame.locals import *
import random
import os

# How fast our game loop runs
clock = pygame.time.Clock()

width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
colorBackground = (0, 0, 0)

# Changing surface color
screen.fill(colorBackground)
pygame.display.flip()
pygame.display.set_caption('The United States of Hangman')

states = "Alabama Alaska Arizona Arkansas California Colorado Connecticut Delaware Florida Georgia Hawaii Idaho Illinois Indiana Iowa Kansas Kentucky Louisiana Maine Maryland Massachusetts Michigan Minnesota Mississippi Missouri Montana Nebraska Nevada NewHampshire NewJersey NewMexico NewYork NorthCarolina NorthDakota Ohio Oregon Oklahoma Pennsylvania RhodeIsland SouthCarolina SouthDakota Tennessee Texas Utah Vermont Virginia Washington WestVirginia Wisconsin Wyoming".split()

class StateName():
    #randomly selects a state name
    def get_state(wordList):
        state_index = random.randint(0, len(wordList) - 1 )
        return wordList[state_index]
StateName()

# hangman body
icon = pygame.image.load('earth.png')
pygame.display.set_icon(icon)
headImg = pygame.image.load('earth.png')
headX = 100
headY = 100
def head():
	screen.blit(headImg, (headX, headY))

X = 410; Y = 200; width = 4; height = 50
b1 = pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
X = 300; Y = 150; width = 5; height = 250
b2 = pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
X = 300; Y = 150; width = 5; height = 250
b3 = pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
X = 300; Y = 150; width = 5; height = 250
b4 = pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
X = 300; Y = 150; width = 5; height = 250
b5 = pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))

body_part = [icon, b1, b2, b3, b4, b5] 
for i in StateName():
	if i == True:
		print(body_part[0]) 
hangman_status = 0


# Game loop
run = True
while run:
	clock.tick()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			print(pos)
    # hang visual
	X = 300; Y = 150; width = 5; height = 250
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	
	X = 250; Y = 400; width = 100; height = 5
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))

	X = 300; Y = 150; width = 110; height = 5
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))

	X = 410; Y = 150; width = 5; height = 20
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))

	#screen.blit(body_parts[hangman_status])

	pygame.display.update()
	clock.tick(30)


pygame.init()

class hint(StateName):
    "Gives you a hint depending on the state"

class letter():
    'j'

class wrongletter(letter):
    "letters that are incorrect will be shown in the incorrect box"




StateName()
letter()
hint()
pygame.quit()
quit()

