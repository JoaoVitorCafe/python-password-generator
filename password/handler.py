import random
import json
import password.params as params
from time import sleep
import os

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
    if(save == 'y' and password):
        
        user = {
            "name" : name ,
            "password" : password,
        }

        print("Saving password...")
        sleep(1)
        
        if not (os.path.isfile('./passwords.json')):
            try:
                filePassword = open("passwords.json" , "w")
                users = json.dumps([])
                filePassword.write(users)
                filePassword.close()
            except:
                print("Error creating file to save passwords...")
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
            
            filePassword.close()
        except:
            print("Error to save your new password!")

def showPasswords(show):
    if(show == 'y'):
        try:
            filePassword = open("passwords.json" , "r")
            users = json.load(filePassword)
            for user in users:
                print(user) 
            filePassword.close()
        except:
            print("Error to display passwords") 

    
