import random
import randomFunctions as rdfunc
import password.params as params

def format(password , length):
    random.shuffle(password)
    return ''.join(password[0:length])

def getPreferences(*preferences):
    return list(preferences)

def generatePassword(prefs , length=8):
    keys = params.getKeys()
    passwordParams = params.passwordParams
    finalPassword = []
    
    for i in range(0 , length):
        for j in range(0 , len(prefs)):
            if(prefs[j] == 'y'):
                char = passwordParams[keys[j]]()
                finalPassword.append(char)
    
    return format(finalPassword , length)