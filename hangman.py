
class visual():
    """establishes the core visual elements of the game
	Horizontal line: line where the letters are placed
	Hanger: the line drawn hanger
	Wrong letter board: where the incorrect letters will be shown"""

class statename():
    "computer chooses a random state in the state bank"

class hint(statename):
    "Gives you a hint depending on the state"

class letter():
    guess = input('Guess a letter: ')
    "if guess is not a letter in the state name add a part of the stick man"

class wrongletter(letter):
    "letters that are incorrect will be shown in the incorrect box"

class stickman(letter):
    """if guess is not a letter in the state name add a part of the stick man
    the stickman has 6 body parts ( 1 head, 2 arms, 2 legs, 1 chest)"""

class endgame():
    "when the stick man is fully drawn = when theres 6 incorrect guesses"



visual()
statename()
letter()
hint()
endgame()
