#MW_CP2 password generator


import random
#Variables, one for lower, one for upper, one for special characters, list of all created passwords
lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
special = ["`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","\\","|",";",":","\"","\'","<",",",">",".","?","/"]
numbers = ['1','2','3','4','5','6','7','8','9','0']
passwords = []

#wrong right function to make sure the user isnt being stupid.

#function called chooser that will take in what type of character it is forced to use and it will return a random one
def chooser(type):
    number = ''
    if type == 1:
        number = random.choice(lower)
    elif type == 2:
        number = random.choice(upper)
    elif type == 3:
        number = random.choice(special)
    elif type == 4:
        number = random.choice(numbers)

    return number

#function called peice together, takes in length and what is required for the password Ensures all user requirements happen.
def peiceTogether(length, allowed):
    peices = []
    allowed_covered = []
    for i in allowed:
        allowed_covered.append(i)
    password = []
    while length > 0:
        pick = random.choice(allowed)
        if pick in allowed_covered:
            allowed_covered.remove(pick)
            peices.append(pick)
            length -= 1

        elif allowed_covered == []:
            peices.append(pick)
            length -= 1
        

    for peice in peices:
        password.append(chooser(peice))

    return password

def userInput(prompt = '> '):
    return input(prompt).lower().strip()

def intInput(max = 100000,prompt='> ',min = 0):
    while True:
        num = userInput(prompt)
        try:
            num = int(num)
        except:
            print('Input is not a number!')
            continue
        if num <= max and num >= min:
            return num
        else:
            print('Input is out of range!')

def choiceInput(choices,prompt = '> '):
    while True:
        choice = userInput(prompt)
        if choice in choices:
            return choice
        else:
            print('Please select a valid choice!')
        
def checkingIfUserWants(checking, item):
    possible = choiceInput(choices = ["y", "n"], prompt = f"\nwould you like {item} (press 'y' is yes, and 'n' if no): ") 
    if possible == "y":
        return checking
        
def showPassword(passwords):
    for i in passwords:
        print(f"\n {i}")

#Main menu function allows the user to either create a password, hold a password, veiw a passwords, or leave.
def mainMenu():

        

    print("Hello! This program is built to hold and build passwords for you.\n")
    while True:
        
        choice = choiceInput(choices = ['1','2','3','4'], prompt = "\n\nPress 1 if you would like to veiw all currently saved passwords.\nPress 2 if you would like to input a new saved password.\nPress 3 if you would like to have us generate a password for you.\nPress 4 if you would like to terminate the program.\ninput here:")
        if choice == "4":
            break
    #if they choose to creat they will be asked the given questions: how long? lowercase? uppercase? special? then we will build a password using the peice together function
        elif choice == "3":
            allowed_options = []

            while True:

                allowed_options.append(checkingIfUserWants(1, "lowercase letters"))

                if None in allowed_options:
                    allowed_options.remove(None)

                allowed_options.append(checkingIfUserWants(2, "uppercase letters"))

                if None in allowed_options:
                    allowed_options.remove(None)

                allowed_options.append(checkingIfUserWants(3, "special characters"))

                if None in allowed_options:
                    allowed_options.remove(None)

                allowed_options.append(checkingIfUserWants(4, "numbers"))

                if None in allowed_options:
                    allowed_options.remove(None)

                if allowed_options == []:
                    print("\n\nsomewhere you forgot to give us access to any character options")
                else:
                    break

            length_pass = intInput(max = 30, min = 4, prompt = "How many characters would you like in your password? (max is 30, min is 4): ")

            generated_password = "".join(peiceTogether(length_pass, allowed_options))
            print(f"\n\n your password is: {generated_password}\n\n")
            passwords.append(generated_password)
            

        elif choice == "2":
            while True:
                password = input("Insert your password (character limit is 30):")
                if len(password) > 30:
                    print("over character limit!")
                elif len(password.strip()) < 1:
                    print("please input something for your password")
                else:
                    passwords.append(password)
                    break

        elif choice == '1':
            if passwords == []:
                print("\nYou dont have apassword yet!")
            else:
                showPassword(passwords)

mainMenu() #if they  choose to hold a password, they will input there password and it will be held