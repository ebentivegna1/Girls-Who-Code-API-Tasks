HANGMANPICS = ['''
  
     +---+
     |   |
         |
         |
         |
         |
  =========''', '''
 
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']



word = ["panda","happy","hi","book","pizza","the", "python","socks", "default", "January","december","computer","lab", "box","kitty","chair","table","save","untitled","chocolate","phone","bagel","run","definition"]
import random
a = random.choice(word)
list_of_unique_letters_in_word = set(a)
global wrong_guesses 
wrong_guesses=0
right_guesses = 0
letter_guesses = []
already_right_guesses = []
number_of_letters = len(a)
is_game_going = True

def shown_blanks_for_words():
    for i in range(number_of_letters):
      print "_" 

def guess(letter,wrong_guesses=wrong_guesses):
  if letter.lower() in letter_guesses:
    print "already guessed, guess another letter"
  else:
    if letter not in a:
      wrong_guesses+=1
    letter_guesses.append(letter)
  
  if len(letter)>1:
    print "guess one letter"

  for l in a:
    if l == letter:
      print l
      already_right_guesses.append(l)
      global right_guesses
      right_guesses = right_guesses + 1
    elif l in already_right_guesses:
      print l
    else: 
      print "_"

  print HANGMANPICS[wrong_guesses]
      
      # print letter 

def game():
  shown_blanks_for_words()
  print a
  print number_of_letters

  if wrong_guesses<6:

    while len(already_right_guesses)<number_of_letters:
      letter_guess=raw_input("Please guess a letter:")
      guess(letter_guess)

    print "You win"

  else:
    print "game over"

game()
      # already_right_guesses.append(letter)
  # else letter in already_right_guesses and letter in a:
  #     print letter 
  # else:
  #         print "_"
  #         global wrong_guesses
  #         wrong_guesses = wrong_guesses + 1
  #         over(wrong_guesses)
  #         pictures(wrong_guesses)

