blanks_to_fill = ["___1___", "___2___", "___3___", "___4___"]

sample_1 = '''When you ride your ___1___, you should always wear an ___2___ to protect
your ___3___. ___2____s must respect very strict ___4___ and controls in order to be considered safe. '''

answer_sample_1 = ['bicycle', 'helmet', 'head', 'regulations']

sample_2= '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

answer_sample_2 = ['function', 'parameters', 'outputs', 'lists']

sample_3 = '''Are you considered an ___1___ ? Do you love listening to music,
any kind of music? Music has played an important role in cultural, traditions and societies for ___2___.
But, was this wonderful sound first ___3___ and become one of largest ___4___ grossing industries in America?
In 1877 the U.S. inventor Thomas Alva Edison heard "Mary had a little lamb"'''

answer_sample_3 = ['audiophile', 'centuries', 'emit', 'capital']

sample_chosen = ""
answers_chosen = []
user_attempts = 0

questionIndex = 1
guesses = 5

def choose_level():
	global user_attempts
	user_attempts += 1
	print "Welcome to Federico's fill in the blanks game. "
	level = raw_input("Choose a level between easy, medium or hard: ")
	if level == 'easy':
		sample_chosen = sample_1
		answers_chosen = answer_sample_1
	elif level == 'medium':
		sample_chosen = sample_2
		answers_chosen = answer_sample_2
	elif level == 'hard':
		sample_chosen = sample_3
		answers_chosen = answer_sample_2

	#in case the user choose a level that is not available, I want to rerun the choose level function
	else:
		print "The level you have chosen is not available. Please choose another level"
		if user_attempts < 4:
			return choose_level()
		else:
			print "As you are unable to choose a level, I doubt you could solve the quiz. Goodbye!"

	print " "
	print "You've chosen %s!" % level
	print "You will get 5 guesses per problem"
	print " "
	play_game(sample_chosen, answers_chosen)


def update_sample(sample, correctAnsw, blank):
    replaced = []
    # your code here
    sample = sample.split()
    for word in sample:
        if blank in word:
            if blank == word:
                replaced.append(correctAnsw)
            else:
                punctuation = word[len(word) - 1]
                replaced.append(correctAnsw + punctuation)

        else:
            replaced.append(word)
    return " ".join(replaced)

def ask(n):
	return raw_input("What should be substituted in for __%s__? " % n)

def play_game(sample, answers):
	global questionIndex
	global guesses

	if guesses != 0 and questionIndex < len(answers ):
		print ""
		print "The current paragraph reads as such:"
		print sample
		print ""
		userInput = ask(questionIndex)
		if userInput == answers[questionIndex - 1]:
			sample = update_sample(sample, userInput, "___%s___" % questionIndex)
			questionIndex += 1
			print ""
			print "Congrats !!!"
		else:
			guesses -= 1
			print ""
			print "Sorry ... that's wrong. Please try again."
			print "you have got %s guesses left" % guesses

	elif guesses == 0:
		print ""
		print "Game over !!!"
		return
	elif questionIndex == 5:
		print ""
		print "You won !!!"
		return
	return play_game(sample, answers)

choose_level()
