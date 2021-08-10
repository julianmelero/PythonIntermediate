import random, os
def get_word():
    words = open("./files/data.txt", encoding="utf-8").read().splitlines()
    return random.choice(words)    


def print_word(word):
    simbols = ""
    for letter in word:
        simbols = simbols + " _ "
    print(simbols)


def get_letter():
    letter = input("Enter a letter, please:")
    while (len(letter) >1) or (letter.isnumeric()):
        print("Only one letter and no numbers")
        letter = input("Enter a letter, please:")
    return letter


    




def run():
    os.system("clear")
    print("----------------")
    print("Welcome to Melero's Hangman Game")       
    word = get_word()        
    print_word(word)
    print("\n")
    get_letter()
    
    





if __name__ == '__main__':
    run()