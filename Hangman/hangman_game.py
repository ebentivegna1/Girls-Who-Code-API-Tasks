from hangman import HANGMANPICS
import random

#Define letter guessing
def guess(letter,word,correct_guesses):
    for char in word:
             if char in correct_guesses:
                     print char
             elif char==letter:
                     print char
                     correct_guesses.append(letter)
             else:
                     print "_"

#Define actual game play
def game():
	WORD_LIST=["animal","beaver","container","docker","elephant","fickle","giving","handler","icicle",
	"jigsaw","koala","lemonade","marathon"]

	random.shuffle(WORD_LIST)
	word=WORD_LIST.pop()
	letters_in_word=len(set(word))
	correct_guesses=[]
	strike_count=0
	max_strikes=6

	while len(correct_guesses)<letters_in_word and strike_count<max_strikes:
		letter_guess = raw_input("Please guess a letter: ") 
		guess(letter_guess,word,correct_guesses) 
		if letter_guess not in word:
			strike_count+=1

		print HANGMANPICS[strike_count]

		if len(correct_guesses)==letters_in_word:
			print "You win!"

		if strike_count==max_strikes:
			print "Hangman!"

#Execute game
game()

