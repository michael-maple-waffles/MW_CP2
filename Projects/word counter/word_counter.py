#MW_CP2 word counter program

def readFile(file = "Projects\\word counter\\file.txt"):
    try:
        with open(file, 'r') as file:
            content = f"{file}"
    except:
        print(f"\n file does not exist\n")
    else:
        return content
    
def countingWords(read_file):
    count = 0
    for character in read_file:
        if character.isAlpha() == False:
            count += 1
        else:
            pass