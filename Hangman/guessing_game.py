#This imports a library called random that lets us use functions that randomly select numbers
import random

#Set the variable strike count to an initial value of 0 (the user will start with no strikes)
strike_count=0

#Let this represent the max amount of strikes you will allow the user to get, set max_strikes variable
max_strikes=3

#Num will be a different variable each time the code runs, this is going to randomly pick a number from 1-10 to set num to
num = random.randint(1,10)

#Here we define a function called guessing_game, note that I have to pass in strike_count and max_strikes as parameters 
#I would just copy this syntax-- we can discuss in person why we have to pass the variables in as parameters
def guessing_game(strike_count=strike_count,num=num):

	#I set a while loop that only runs while strike_count is less than max_strikes, once the user hits max_strikes, the user loses
	while strike_count<max_strikes:

		#Solicit input from the users
		guess = raw_input("Please guess a number 1-10: ")
		
		#Test if the guess is equal to the random number
		if str(guess)==str(num):
			#If the guess is equal to the actual value print "you are correct"
			print "you are correct"
			break
		else:
			#If the guess is not equal to the actual value print "you are wrong"
			print "you are wrong"
			strike_count= strike_count + 1
			print "you have " + str(strike_count)  + " strikes"

	#This code will only happen once the while loop is finished (meaning the user has hit maximum strikes or won)
	print "game over"


#Above I just defined the function, here I actually call the function
guessing_game()
