#MW_CP2 password generator


import random
#Variables, one for lower, one for upper, one for special characters, list of all created passwords
lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
special = ["`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","\\","|",";",":","\"","\'","<",",",">",".","?","/"]
passwords = []

#wrong right function to make sure the user isnt being stupid.

#function called chooser that will take in what type of character it is forced to use and it will return a random one
def chooser(type):
    if type == 1:
        number = random.choice(lower)
    elif type == 2:
        number = random.choice(upper)
    elif type == 3:
        number = random.choice(special)

    return number

#function called peice together, takes in length and what is required for the password Ensures all user requirements happen.
def peiceTogether(length, allowed):
    peices = []
    allowed_covered = allowed
    password = []
    while length > 0:
        pick = random.choice(allowed)
        if pick in allowed_covered:
            allowed_covered.remove(pick)
            peices += pick
            length -= 1

        elif allowed_covered == []:
            peices += pick
            length -= 1
        

    for peice in peices:
        password += chooser(peice)

    return password
#function called clear that sets held passwords to 0

#Main menu function allows the user to either create a password, hold a password, veiw a passwords, or leave.

    #if they choose to creat they will be asked the given questions: how long? lowercase? uppercase? special? then we will build a password using the peice together function

    #if they choose to hold a password, they will input there password and it will be held