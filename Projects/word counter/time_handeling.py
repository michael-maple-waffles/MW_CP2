#mw_cp2 date time--> wordcounter

import datetime
import csv

def countingWords(read_file):
    character_count = 0
    word_count = 0
    for character in read_file:
        character_count += 1
        if character == ' ' or character == '\n':
            word_count += 1
            print("+1")
    
    return(character_count, word_count)

def fileupdates(filepath, file_word_count):
    now = datetime.datetime.now()
    try:
        with open(file = "/workspaces/MW_CP2/Projects/word counter/file_changes.csv", mode = 'a') as file_changes:
            writer = csv.writer(file_changes)
            writer.writerow(filepath, now, file_word_count)
    except:
        print("File doesn't exist")
    else:
        pass