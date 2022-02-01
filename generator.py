import randomFunctions as rd

answers = []

paramsPassword = {
    "hasNumbers" : rd.getRandomNumber,
    "hasUpper" : rd.getRandomUpper,
    "hasLower" : rd.getRandomLower,
    "hasSpecial" : rd.getRandomSpecial,
}

keys = list(paramsPassword.keys())
        
name = input("Type your name: ")
print(f"Everything is right , {name}!")
print("We just need to know your preferences for your brand new password.")

length = int(input("What's the length you wish for your password?"))

hasNumbers = input("Do you want numbers in your password? (y/n) ")

answers.append(hasNumbers)

hasUpper = input("Do you want upper case letters in your password? (y/n) ")

answers.append(hasUpper)

hasLower = input("Do you want lower case letters in your password? (y/n) ")

answers.append(hasLower)

hasSpecial = input("Do you want special characters in your password? (y/n) ")

answers.append(hasSpecial)

password = []

for i in range(0 , length):
    for j in range(0 , len(answers)):
        if(answers[j] == 'y'):
            char = paramsPassword[keys[j]]()
            password.append(char)

password = rd.formatPassword(password , length)

print(password)

# Fix the bug - include all params to generate the password
# Include files handling to save passwords
# Look for improvements
# Implement functions to optimize the code




    




