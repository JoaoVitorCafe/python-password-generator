import random
import json
import password.params as params
from time import sleep

def validPrefs(prefs):
    if not "y" in prefs:
        return False
    return True

def checkLength(length):
    if(length < params.passwordParams["minimum"]):
        print("Your password has been set to have 8 characteres")
        return params.passwordParams["minimum"]
    return length

def format(password , length):
    random.shuffle(password)
    return ''.join(password[0:length])

def getPreferences(*preferences):
    return list(preferences)

def generatePassword(prefs , length=8):
    keys = params.getKeys()
    passwordParams = params.passwordParams
    finalPassword = []
    
    if(validPrefs(prefs)):
        print("Creating password..")
        sleep(1)
        
        for i in range(0 , length):
            for j in range(0 , len(prefs)):
                if(prefs[j] == 'y'):
                    char = passwordParams[keys[j]]()
                    finalPassword.append(char)
        password = format(finalPassword , length)
        print("Your new password is " + password)
        return password
    
    print("Erro to generate password!")
    print("There's no preferences ")
    return ""


def savePassword(name , password , save):
    user = {
        "name" : name ,
        "password" : password,
    }

    if(save == 'y'):
        print("Saving password...")
        sleep(1)
        try:
            filePassword = open("passwords.json" , "r+")
                    
            # Loads the data of the jsonFile as a dictionary type
            fileData = json.load(filePassword) 

            # Append the user to data 
            fileData.append(user)

            # Sets file's current position at offset.
            filePassword.seek(0)
            
            # Convert the data back to Json     
            jsonData = json.dumps(fileData)
            
            # Write in the file
            filePassword.write(jsonData)
            print("Password saved sucessfully!")
        except:
            print("Error to save your new password!")
        finally:
            filePassword.close()

def showPasswords():
    try:
        filePassword = open("passwords.json" , "r")
        for password in filePassword:
            print(password)
        filePassword.close()
    except:
        print("Error to display passwords") 
