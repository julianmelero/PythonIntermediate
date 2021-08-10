import random, os
def get_word():
    words = open("./files/data.txt", encoding="utf-8").read().splitlines()
    return random.choice(words)    


def print_word(word):
    simbols = ""
    for letter in word:
        simbols = simbols + " _ "
    print(simbols)

def print_aux_word(aux_word):    
    word = ""
    for letter in aux_word:              
        if letter == " _ ":
            word = word + " _ "
        else:
            word = word + letter
    print(word + "\n")



def get_letter():
    letter = input("Enter a letter, please:")
    while (len(letter) >1) or (letter.isnumeric()):
        print("Only one letter and no numbers")
        letter = input("Enter a letter, please:")
    return letter


def is_letter_in_word(word, letter, aux_word):
    for i in range(len(word)):
        if word[i] == letter:
            aux_word[i] = letter            
    return aux_word    


def is_word_guessed(word, aux_word):
    for letter in word:
        if letter not in aux_word:
            return False
    print("You guessed the word!")


def run():
    os.system("clear")
    print("----------------")
    print("WELCOME TO MELERO'S HANGMAN GAME")       
    word = get_word()            
    aux_word = [" _ " for i in range(0, len(word))]
    print(len(aux_word))
    print_word(word)
    print("\n")
    while is_word_guessed(word,aux_word) == False:
        letter = get_letter()
        aux_word = is_letter_in_word(word, letter, aux_word)    
        print_aux_word(aux_word)
    
    





if __name__ == '__main__':
    run()