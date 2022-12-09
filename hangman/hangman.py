import pygame
from pygame.locals import *
import random
import os
import math

# How fast our game loop runs
clock = pygame.time.Clock()

width, height = 1100, 600
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
LETTER_FONT = pygame.font.SysFont('courier', 30)
WORD_FONT = pygame.font.SysFont('courier', 40)

wordList = ["ALABAMA", 
		  "ALASKA",
		  "ARIZONA",
		  "ARKANSAS", 
		  "CALIFORNIA",
		  "COLORADO", 
		  "CONNECTICUT", 
		  "DELAWARE", 
		  "FLORIDA", 
		  "GEORGIA",
		  "HAWAII", 
		  "IDAHO", 
		  "ILLINOIS", 
		  "INDIANA", 
		  "IOWA", 
		  "KANSAS", 
		  "KENTUCKY", 
		  "LOUISIANA", 
		  "MAINE", 
		  "MARYLAND", 
		  "MASSACHUSETTS", 
		  "MICHIGAN", 
		  "MINNESOTA", 
		  "MISSISSIPPI", 
		  "MISSOURI", 
		  "MONTANA", 
		  "NEBRASKA", 
		  "NEVADA", 
		  "NEW HAMPSHIRE", 
		  "NEW JERSEY", 
		  "NEW MEXICO", 
		  "NEW YORK", 
		  "NORTH CAROLINA", 
		  "NORTH DAKOTA", 
		  "OHIO", 
		  "OREGON", 
		  "OKLAHOMA", 
		  "PENNSYLVANIA", 
		  "RHODE ISLAND", 
		  "SOUTH CAROLINA", 
		  "SOUTH DAKOTA", 
		  "TENNESSEE", 
		  "TEXAS", 
		  "UTAH", 
		  "VERMONT", 
		  "VIRGINIA", 
		  "WASHINGTON", 
		  "WEST VIRGINIA", 
		  "WISCONSIN", 
		  "WYOMING"]

    #randomly selects a state name
def get_state(wordList):
    state_index = random.randint(0, len(wordList) - 1 )
    return wordList[state_index]
state = get_state(wordList)

hangman_status = 0 

guessed = []
# Game loop
run = True

def draw():
	screen.fill((0, 0, 0))
	indent = -170 
	#draw statename
	display_word = ""
	for letter in state:
		if letter in guessed:
			display_word += letter + " "
		elif letter == " ":
			display_word += "  "
		else:
			display_word += "_ "

	text = WORD_FONT.render(display_word, 1, (255, 255, 255))
	screen.blit(text, (550 + indent, 340))
	
	#letters 
	for letter in letters:
		x, y, ltr, visible = letter
		if visible:
			pygame.draw.circle(screen, (255, 255, 255), (x, y), radius, 3)
			text = LETTER_FONT.render(ltr, 1, (255, 255, 255))
			screen.blit(text, (x - text.get_width() / 2, y - text.get_width() / 2 - 5))
	
	# hang visual
	X = 300 + indent; Y = 150; width = 5; height = 250
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	
	X = 250 + indent; Y = 400; width = 100; height = 5
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))

	X = 300 + indent; Y = 150; width = 110; height = 5
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))

	X = 410 + indent; Y = 150; width = 5; height = 20
	#head
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	head = pygame.image.load("hangman/images/earth.png").convert()
	screen.blit(head, (380 + indent, 165))
	# Torso
	X = 410 + indent; Y = 230; width = 4; height = 80
	torso = pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	#legs
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	rightleg = pygame.image.load("hangman/images/rightleg.png").convert()
	screen.blit(rightleg, (410 + indent, 310))
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	leftleg = pygame.image.load("hangman/images/leftleg.png").convert()
	screen.blit(leftleg, (350 + indent, 310))
	#arms
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	rightarm = pygame.image.load("hangman/images/rightarm.png").convert()
	screen.blit(rightarm, (415 + indent, 250))
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	leftarm = pygame.image.load("hangman/images/leftarm.png").convert()
	screen.blit(leftarm, (345 + indent, 250))

	
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
						guessed.append(ltr)

	
	clock.tick(30)


pygame.init()
pygame.quit()
quit()
