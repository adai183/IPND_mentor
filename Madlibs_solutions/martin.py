##############################################
### PSEUDOCODE FOR P2 - CODE YOUR OWN QUIZ ###
##############################################

# define text for different levels
easy_text = "__1__ is a small country in Europe, that is know for its past music, __2__, and the capital, Vienna. Maybe also for a movie, called 'The __3__ of music'."
medium_text = "Grass is __1__, and water is __2__ and sometimes also your phone is __3__ on the inside, but that's usually a problem."
hard_text = "Today I mixed a __1__ and some __2__ with __3__ and had a very good morning drink."

# define answers for different levels
easy_answers = ["Austria", "mountains", "sound"]
medium_answers = ["wet", "wet", "wet"]
hard_answers = ["banana", "raspberries", "milk"]

# define how the blanks look like
blanks = ["__1__", "__2__", "__3__"]

# start game by saying hi and asking the player if they want to play
def start_game():
	choice = raw_input("Wanna play the quizzy Quiz? (y/n): ").lower()
	if choice == "n":
		print "Alright then! Have a great day!"
		exit()
	elif choice == "y":
		return select_level()
	else:
		print "that's confusing... Please focus!"
		return start_game()

def select_level():
	good_choices = ["easy", "medium", "hard"]
	level = raw_input("Please choose your difficulty (type 'easy', 'medium', or 'hard'): ").lower()
	# start game in the selected difficulty
	# take care to account for wrong inputs of the user
	if level in good_choices:
		print "\nYou chose the %s version! Here we go:" %(level)
		if level == "easy":
			return ask_questions(easy_text, easy_answers)
		elif level == "medium":
			return ask_questions(medium_text, medium_answers)
		elif level == "hard":
			return ask_questions(hard_text, hard_answers)
	else:
		print "That's not a valid input."
		return select_level()

# display appropriate paragraph
def ask_questions(text, answers):
	index = 0
	for blank in blanks:

# (OPTIONAL: show how many tries left)

		# and show what is the next blank
		print "\n" + text + "\n"
		player_answer = get_answer()
		# keeps the player here until they get it right
		while player_answer != answers[index]:
			print "Whoops, that's not correct. Please try again!"
			print "\n" + text + "\n"
			player_answer = get_answer()
		# if the answer is correct, breaks from the loop
		# congratulate
		print "Yay! That's correct!"
		# fill the text with the correct word
		text = text.replace(blank, player_answer)
		index += 1
	# when all answers are correctly filled,
	# show the full text
	print "\n" + text + "\n"
	# and say a hearty congratulations!
	print "Congratulations! You've correctly filled all the blanks!\n"
	return start_game()

def get_answer():
	# prompt for answer to the first blank
	player_answer = raw_input("What word goes into the first blank from the left: ")
	return player_answer



# (OPTIONAL: if all tries are used up)
# (end game with message, and ask if the user wants to try again)


start_game()
