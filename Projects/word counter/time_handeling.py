#mw_cp2 date time--> wordcounter

import datetime
import csv

def countingWords(read_file):
    character_count = 0
    word_count = 0
    final_char = ''
    for character in read_file:
        character_count += 1
        if character == ' ' or character == '\n':
            word_count += 1
            final_char = character
    
    if final_char != '\n' and final_char != ' ':
        word_count += 1
    return(character_count, word_count)

def fileUpdates(filepath = "/workspaces/MW_CP2/Projects/word counter/file.txt", file_word_count = (0,0)):
    now = datetime.datetime.now()
    try:
        with open(file = "/workspaces/MW_CP2/Projects/word counter/file_changes.csv", mode = 'a') as file_changes:
            writer = csv.writer(file_changes)
            inputting_row = [filepath, now, file_word_count[1], file_word_count[0]]
            writer.writerow(inputting_row)
    except:
        print("File doesn't exist")
    else:
        pass

def veiwUpdates(filepath):
    try:
        with open(file = "/workspaces/MW_CP2/Projects/word counter/file_changes.csv", mode = 'r') as file_to_veiw:
            reader = csv.reader(file_to_veiw)
            updates = []
            for line in reader:
                if filepath in line:
                    updates.append(line)
    except:
        print("file does not exist")
    else:
        for line in updates:
            print(f"\nfilepath: {line[0]}, date of update: {line[1]}, word count after update: {line[2]}, character count after update: {line[3]}")

