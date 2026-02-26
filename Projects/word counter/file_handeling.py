#MW_CP2 word counter program

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



def readFile(file = "Projects\\word counter\\file.txt"):
    try:
        with open(file, mode = 'r') as file:
            content = f"{file}"
    except:
        print(f"\n file does not exist\n")
    else:
        return content
    
def countingWords(read_file):
    character_count = 0
    word_count = 0
    for character in read_file:
        character_count += 1
        if character == ' ' or '\n':
            word_count += 1
    
    return(character_count, word_count)


def appendFile(file):
    try:
        with open(file, 'a') as untouched_file:
            untouched_file = 




def mainMenu():
    print("This program is ment to check word and character count.\n\n")

    choice = choiceInput(['1','2','3'])


        
