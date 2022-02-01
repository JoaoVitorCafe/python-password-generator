import random
# Import random module to generate random numbers

def getRandomNumber():
    # This function return a random number between 0 and 9
    random.seed()
    return str(random.randint(0 , 9))

def getRandomLower():
    # Generate a lower case letter that is related with a integer number between 97 and 122
    return chr(random.randint(97 ,122)) 

def getRandomUpper():
    # This function uses a function getRandomLower to generate a uppercase letter
    return getRandomLower().upper()

def getRandomSpecial():
    # Generate special characteres
    specials = '!@#$%^&*(){}[]=<>/,.?ç;|'
    return random.choice(specials)

def formatPassword(password , length):
    random.shuffle(password)
    return ''.join(password[0:length])
