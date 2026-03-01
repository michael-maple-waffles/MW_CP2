#MW_CP2 file handeling --> word counter
import csv
import time
from time_handeling import countingWords, fileUpdates, veiwUpdates

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
        fileUpdates(filepath = file, file_word_count=countingWords(readFile(file)))

def getUserFilepath():
    while True:
        user_file_path = input("\nplease copy the exact file path of your file.\n (input Here): ")
        try:
            with open(user_file_path, 'r') as file:
                exist = file
        except:
            print("\nthis file does not exist, make sure the file does!")
        else:
            return user_file_path

def mainMenu():
    print("This program is ment to change documents, and veiw the updates to them.\n")
    filepath = "/workspaces/MW_CP2/Projects/word counter/file.txt"
    while True:
        print(f"-----Main Menu-----\n\n  Current File: {filepath}")
        choice = choiceInput(['1','2','3','4','5','6'], f"\nPress '1' to set/change the current file that you are editing\nPress '2' to add to the file\nPress '3' to veiw the file\nPress '4' to veiw the files current word and character count\nPress '5' to veiw all the file update history(only applies to updates made using this program)\nPress '6' to exist the program.\n(Input Here): ")
        if choice == '1':
            filepath = getUserFilepath()
            time.sleep(3)
        elif choice == '2':
            appendFile(filepath)
            time.sleep(3)
        elif choice == '3':
            print(readFile(filepath))
            time.sleep(3)
        elif choice == '4':
            words = countingWords(readFile(filepath))
            print(f"word count : {words[1]}, character count : {words[0]}")
            time.sleep(3)
        elif choice == '5':
            veiwUpdates(filepath = filepath)
            time.sleep(3)
        elif choice == '6':
            break


        
