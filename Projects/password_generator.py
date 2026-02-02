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

def yesNo(inserted, type, amount):
    if type == 1:
        if inserted in ['yes', 'Yes', 'y', 'Y','sure', 'Sure']:
            return (True, True)
        elif inserted in ['N', 'n', 'No', 'no']:
            return (True, False)
        else:
            return (False, "Make sure you are inputting a Y/N")
        
    elif type == 2:
        if inserted.isDigit:
            if int(inserted) in range(amount):
                return (True, False)
            else:
                return (False, "Make sure your number is in the range 1 -", amount)
        else:
            return(False, "Make sure you are inputting a digit.")

#Main menu function allows the user to either create a password, hold a password, veiw a passwords, or leave.
def mainMenu():
    print("Hello! This program is built to hold and build passwords for you.\n")
    while True:
        while yesNo(choice, 2, 4) == False:
            choice = input("Press 1 if you would like to veiw all currently saved passwords.\nPress 2 if you would like to input a new saved password.\nPress 3 if you would like to have aus generate a password for you.\nPress 4 if you would like to terminate the program.")
        if choice == "4":
            break
    #if they choose to creat they will be asked the given questions: how long? lowercase? uppercase? special? then we will build a password using the peice together function
        elif choice == "3":
            while yesNo(check1, 1, False)[1] == False:
                check1 = input("Would you like lowercase letters? (Y/N)")
            
            while yesNo(check2, 1, False)[1] == False:
                check2 = input("would you like uppercase letters? (Y/N)")

            while yesNo(check3, 1, False)[1] == False:
                check3 = input("would you like special characters? (Y/N)")

            if check1 == 
    #if they  choose to hold a password, they will input there password and it will be held