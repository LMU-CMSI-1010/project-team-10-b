import pygame
from pygame.locals import *
import random
import os
import math

pygame.init()

# How fast our game loop runs
clock = pygame.time.Clock()

width, height = 1100, 600
screen = pygame.display.set_mode((width, height))
colorBackground = (0, 0, 0)

# Changing surface color
screen.fill(colorBackground)
pygame.display.flip()
pygame.display.set_caption('The United States of Hangman')

# keyboard variables
radius = 25
gap = 15
A = 65
startx = round((width - (radius * 2 + gap) * 13) / 2)
starty = 475
def keyboard():
	letters = []
	for i in range(26):
		x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
		y = starty + ((i // 13) * (gap + radius * 2))
		letters.append([x, y, chr(A + i), True])
	return letters
letters = keyboard()

# font
pygame.font.init()
LETTER_FONT = pygame.font.SysFont('courier', 30)
WORD_FONT = pygame.font.SysFont('courier', 40)
HINT_FONT = pygame.font.SysFont('courier', 20)

# List of state names
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

hintList = ["Sweet home...",
			"Has Polar Bears",
			"Very Hot",
			"Has the only active diamond mine in the US",
			"The Golden State",
			"Weed",
			"Lobster Roll",
			"Doesn't Exist",
			"Gators",
			"Peaches",
			"Volcanos",
			"Potatoes",
			"Chicago",
			"Basketball",
			"Corn",
			"Tornados",
			"KFC",
			"French",
			"Lobster",
			"Birthplace of the national anthem",
			"One of the original 13 colonies",
			"Has a giant lake named after it",
			"The land of 10,000 lakes",
			"Hard to spell",
			"Gateway arch",
			"Grizzly Bears",
			"Ranches",
			"Gambling",
			"Has the motto, Live free or Die", 
			"Competitive with NY",
			"Was Mexico",
			"Home of the best city in the world",
			"Smokey Mountains",
			"The worse Dakota",
			"College Football",
			"Tornados", 
			"Ducks",
			"Amish",
			"First colony",
			"Sweet Tea",
			"The better Dakota",
			"Nashville",
			"Cowboys",
			"Mormons",
			"Maple Syrup",
			"Known as the birthplace of a nation",
			"Rainy",
			"Take me home... Country road...",
			"Cheese",
			"Jackson Hole"]

# randomly selects a state name
def get_state():
    state_index = random.randint(0, len(wordList) - 1 )
    return state_index
state = wordList[get_state()]
hint = hintList[get_state()]
show_hint = False
# coordinates for hint icon
xhint = 1030
yhint = 10

# load body images
body = []
for i in range(6):
	image = pygame.image.load("hangman/images/hangman" + str(i) + ".png")
	body.append(image)
xbody = [380, 380, 410, 350, 350, 410]
ybody = [165, 225, 225, 225, 285, 285]

indent = -170 

hangman_status = -1
guessed = []

# Game loop variables
run = True
end_game = False

# quit and reset coordinates
xreset = 10
yreset = 80
xquit = 10
yquit = 10

def draw():
	screen.fill((0, 0, 0))
	# hint icon (lightbulb)
	reset = pygame.image.load("hangman/images/idea.png")
	screen.blit(reset, (xhint, yhint))
	# quit and reset buttons
	reset = pygame.image.load("hangman/images/reset.png")
	screen.blit(reset, (xreset, yreset))
	quit = pygame.image.load("hangman/images/quit.png")
	screen.blit(quit, (xquit, yquit))
	# this substitutes the state name for "_"
	# this also makes the letters guessed appear in the black board
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
	
	# draw letters of the keyboard that have not been guessed
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

	X = 410 + indent; Y = 150; width = 5; height = 15
	pygame.draw.rect(screen, (252,252,252), (X, Y, width, height))
	
	for body_part in range(hangman_status + 1):
		screen.blit(body[body_part], (xbody[body_part] + indent, ybody[body_part]))
	# hint letter format and coordinates
	if show_hint:
	   text = HINT_FONT.render(hint, 1, (255,215,0))
	   screen.blit(text, (500, 40))

	pygame.display.update()	
	return display_word

# End message for end game
def end_message(message):
	text = WORD_FONT.render(message, 1, (255, 255, 255))
	screen.blit(text, (450 , 175))
	pygame.display.update()

while run:
	display_word = draw()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		# this code lets us know what coordinate the user has pressed in the game screen
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos_x, pos_y = pygame.mouse.get_pos()
			# check if reset or quit have been clicked
			distance = math.sqrt((xreset + 32 - pos_x) ** 2 + (yreset + 32 - pos_y) ** 2)
			if distance < radius:
				letters = keyboard()
				state = wordList[get_state()]
				hint = hintList[get_state()]
				show_hint = False
				hangman_status = -1
				guessed = []
				end_game = False
			distance = math.sqrt((xquit + 32 - pos_x) ** 2 + (yquit + 32 - pos_y) ** 2)
			if distance < radius:
				pygame.quit()
				quit()
			# check if hint button is pressed
			distance = math.sqrt((xhint + 32 - pos_x) ** 2 + (yhint + 32 - pos_y) ** 2)
			if distance < radius:
			 	show_hint = True
			# check if keyboard is pressed
			if not end_game:
				for letter in letters:
					x, y, ltr, visible = letter
					# if you click a letter it will disapear 
					if visible:
						distance = math.sqrt((x - pos_x) ** 2 + (y - pos_y) ** 2)
						if distance < radius:
							letter[3] = False
							guessed.append(ltr)
							# if you choose the incorrect letter it adds a part of the hangman's body
							if ltr not in state:
								hangman_status += 1
	# End game => Lost
	if hangman_status == 5:
		end_message("YOU LOST!")
		end_game = True
	# End game => Won
	if "_" not in display_word: 
		end_message("YOU WON!")
		end_game = True
	
	clock.tick(30)


