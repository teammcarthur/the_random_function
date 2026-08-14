'''
    Author: Chris M
    Date: 14/07/26
    Version: 1.0
    Description: Guessing Game
'''

#-----Libraries------
import random
#-----Functions------

#-----Main Routine------
if(__name__ == "__main__"):
    contestant = input("Please enter your name") #Gets the user to enter their name and stores it 
    answer = random.randint(1, 10) #Sets the answer to a random number between 1 and 10
    guess = int(0) #initialises the guess as an int
    count = 0