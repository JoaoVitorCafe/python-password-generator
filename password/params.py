import randomFunctions as rd

passwordParams = {
    "hasNumbers" : rd.getRandomNumber,
    "hasUpper" : rd.getRandomUpper,
    "hasLower" : rd.getRandomLower,
    "hasSpecial" : rd.getRandomSpecial,
    "minimum" : 8
}

def getKeys():
    keys = list(passwordParams.keys())
    return keys