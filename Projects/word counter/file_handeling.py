#MW_CP2 file handeling --> word counter
import csv

def userInput(prompt = '> '):
    return input(prompt).lower().strip()

def intInput(max = 100000,prompt='> ',min = 0):
    while True:
        num = userInput(prompt)
        try:
            num = int(num)
        except:
            print('\nInput is not a number!')
            continue
        if num <= max and num >= min:
            return num
        else:
            print('\nInput is out of range!')

def floatInput(max = 100000.00,prompt='> ',min = 0.00):
    while True:
        num = userInput(prompt)
        try:
            num = float(num)
        except:
            print('\nInput is not a number!')
            continue
        if num <= max and num >= min:
            return num
        else:
            print('\nInput is out of range!')

def choiceInput(choices,prompt = '> '):
    while True:
        choice = userInput(prompt)
        if choice in choices:
            return choice
        else:
            print('\nPlease select a valid choice!')



def readFile(file = "/workspaces/MW_CP2/Projects/word counter/file.txt"):
    try:
        with open(file, mode = 'r') as reading_file:
            content = f"{reading_file.read()}"
    except:
        print(f"\n file does not exist\n")
    else:
        return content
    



def appendFile(file = "/workspaces/MW_CP2/Projects/word counter/file.txt"):
    try:
        with open(file, 'a') as untouched_file:
            new_information = f'\n{input("what is the new information you would like to add to the file?\n(Insert Here): ")}'
            untouched_file.write(new_information)
    except:
        print("file doesn't exist")
    else:
        print("File has been updated.")
        file



def mainMenu():
    print("This program is ment to check word and character count.\n\n")

    choice = choiceInput(['1','2','3'])


        
