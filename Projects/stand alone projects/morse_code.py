#MW_CP2 morse code

#variable  called charcters and a variable called morse_characters
characters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ".", ",", "?", ' ')
morse_characters = ('.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----', '.-.-.-', '--..--', '..--..', '/')
characters_not_in_morse = ('\'', '"', '\\', ';', ':', "<", ">", "/", "[", "]", "{", "}", "|", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")","_", "-", "=", "+")
#variable that translates one to the other this will work by iterating over a string and finding indexes to switch it over to the other matching index.
def translate(mode, statement, english, morse):
    if mode == 1:
        translation = ""
        for character in statement:
            if character != ' ':
                index = english.index(character)
                translation = translation + f"{morse[index]}"
            else:
                translation = translation + '/'

        return translation
    
    elif mode == 2:
        translation = ''
        current_set = ''
        for character in statement:
            if character == ' ':
                if current_set in morse:
                    index = morse.index[current_set]
                    translation = f'{translation}{english[index]}'
                    current_set = ''
                else:
                    if '[FAULTY CHARACTER]' in current_set:
                        translation = f'{translation}[FAULTY CHARACTER]'
                        current_set = ''
                    else:
                        translation = f'{translation}[NOT A LETTER IN MORSE]'
                        current_set = ''
            elif character == '/':
                if current_set in morse:
                    index = morse.index[current_set]
                    translation = f'{translation}{english[index]} '
                    current_set = ''
                else:
                    if '[FAULTY CHARACTER]' in current_set:
                        translation = f'{translation}[FAULTY CHARACTER] '
                        current_set = ''
                    else:
                        translation = f'{translation}[NOT A LETTER IN MORSE] '
                        current_set = ''
            else:
                if character == '.' or '-':
                    current_set = f'{current_set}{character}'
                else:
                    curent_set = f'{current_set}[FUALTY CHARACTER]'





#variable to translate english-->morse  uses the translate variable in mode 1/

#variable to translate  morse-->english uses the translate variable in mode 2/ it gets this informaion by asking for the morse code item.

#main menu function