import pygame
from pygame.locals import *
import random
import os
import math

# How fast our game loop runs
clock = pygame.time.Clock()

width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
colorBackground = (0, 0, 0)

# Changing surface color
screen.fill(colorBackground)
pygame.display.flip()
pygame.display.set_caption('The United States of Hangman')

# button variables
radius = 25
gap = 15
letters = []
A = 65
startx = round((width - (radius * 2 + gap) * 13) / 2)
starty = 475
for i in range(26):
	x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
	y = starty + ((i // 13) * (gap + radius * 2))
	letters.append([x, y, chr(A + i), True])

# font
pygame.font.init()
LETTER_FONT = pygame.font.SysFont('arial', 30)
WORD_FONT = pygame.font.SysFont('arial', 30)

#states = "Alabama Alaska Arizona Arkansas California Colorado Connecticut Delaware Florida Georgia Hawaii Idaho Illinois Indiana Iowa Kansas Kentucky Louisiana Maine Maryland Massachusetts Michigan Minnesota Mississippi Missouri Montana Nebraska Nevada NewHampshire NewJersey NewMexico NewYork NorthCarolina NorthDakota Ohio Oregon Oklahoma Pennsylvania RhodeIsland SouthCarolina SouthDakota Tennessee Texas Utah Vermont Virginia Washington WestVirginia Wisconsin Wyoming".split()

#class StateName():
    #randomly selects a state name
    #def get_state(wordList):
        #state_index = random.randint(0, len(wordList) - 1 )
        #return wordList[state_index]
#state_name = StateName()
state = "CALIFORNIA "
guessed = []
# Game loop
run = True

def draw():
	screen.fill((0, 0, 0))
	#draw statename
	display_word = ""
	for letter in state:
		if letter in guessed:
			display_word += letter + " "
		else:
			display_word += "_ "

	text = WORD_FONT.render(display_word, 1, (0, 0, 0))
	screen.blit(text, (500, 200))
	
	#letters 
	for letter in letters:
		x, y, ltr, visible = letter
		if visible:
			pygame.draw.circle(screen, (255, 255, 255), (x, y), radius, 3)
			text = LETTER_FONT.render(ltr, 1, (255, 255, 255))
			screen.blit(text, (x - text.get_width() / 2, y - text.get_width() / 2))

	# hang visual
	X = 300; Y = 150; width = 5; height = 250
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	
	X = 250; Y = 400; width = 100; height = 5
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))

	X = 300; Y = 150; width = 110; height = 5
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))

	X = 410; Y = 150; width = 5; height = 20
	#head
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	head = pygame.image.load("images/earth.png").convert()
	screen.blit(head, (380, 165))
	# Torso
	X = 410; Y = 230; width = 4; height = 80
	b1 = pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	#legs
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	head = pygame.image.load("images/rightleg.png").convert()
	screen.blit(head, (410, 310))
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	head = pygame.image.load("images/leftleg.png").convert()
	screen.blit(head, (350, 310))
	#arms
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	head = pygame.image.load("images/rightarm.png").convert()
	screen.blit(head, (415, 250))
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	head = pygame.image.load("images/leftarm.png").convert()
	screen.blit(head, (345, 250))

	
	pygame.display.update()

# this code lets us know what coordinate the user has pressed in the game screen
while run:
	clock.tick()
	draw()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos_x, pos_y = pygame.mouse.get_pos()
			for letter in letters:
				x, y, ltr, visible = letter 
				if visible:
					distance = math.sqrt((x - pos_x) ** 2 + (y - pos_y) ** 2)
					if distance < radius:
						letter[3] = False

	
	clock.tick(30)


pygame.init()



pygame.quit()
quit()
