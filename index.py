import randomFunctions as rd
import password.handle as handle
from time import sleep

name = str(input("Type your name: "))

print(f"Everything is right , {name}!\n")

print("We just need to know a little bit more about your preferences for your brand new password.\n")

length = int(input("What's the length you wish for your password?"))

hasNumbers = input("Do you want numbers in your password? (y/n)")

hasUpper = input("Do you want upper case letters in your password? (y/n) ")

hasLower = input("Do you want lower case letters in your password? (y/n) ")

hasSpecial = input("Do you want special characters in your password? (y/n) ")

prefs = handle.getPreferences(hasNumbers , hasUpper , hasLower , hasSpecial)

password = handle.generatePassword(prefs , length)

print("Creating password..")
sleep(1)
print("Your new password is " + password)

