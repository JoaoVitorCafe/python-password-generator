import random
import string
# Import random module to generate random numbers

def getRandomNumber():
    # This function return a random number between 0 and 9
    return str(random.randint(0 , 9))

def getRandomLower():
    # Generate a lower case letter that is related with a integer number between 97 and 122
    return chr(random.randint(97 ,122)) 

def getRandomUpper():
    # This function uses a function getRandomLower to generate a uppercase letter
    return getRandomLower().upper()

def getRandomSpecial():
    # Generate special characteres
    special = string.punctuation
    return random.choice(special)
