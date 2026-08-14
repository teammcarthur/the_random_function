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
    contestant = input("Please enter your name")
    answer = random.randint(1, 10)
    guess = int(0)
    count = 0