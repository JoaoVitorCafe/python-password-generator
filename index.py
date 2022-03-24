import password.handler as handler
from time import sleep


name = str(input("Type your name: "))
main_password = input("Type a password that will be used to authenticate user and allow you to see saved passwords : ")

print(f"Everything is right , {name}!\n")

print("We just need to know a little bit more about your preferences for your brand new password.\n")

length = int(input("How many characters you want in your password? You password must have more than 8 characters : "))
length = handler.checkLength(length)

hasNumbers = input("Do you want numbers in your password? (y/n)")

hasUpper = input("Do you want upper case letters in your password? (y/n) ")

hasLower = input("Do you want lower case letters in your password? (y/n) ")

hasSpecial = input("Do you want special characters in your password? (y/n) ")

prefs = handler.getPreferences(hasNumbers , hasUpper , hasLower , hasSpecial)

password = handler.generatePassword(prefs , length)

save = input("Do you want to save this password in file? (y/n)")
handler.savePassword(name , password ,save)
sleep(1)

show = input("Wanna see all the passwords saved? (y/n)")
handler.showPasswords(show , main_password)
