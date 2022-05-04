from time import sleep
from random import randint
import os
import colorama
from colorama import Fore
colorama.init()

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def import_3list():
    t3lw = []
    with open("words_three_letters.txt","r",encoding="utf8") as f3:
        for word in f3.readlines():
            word = word.strip("\n")
            t3lw.append(word)
            
    return t3lw
    
def import_4list():
    f4lw = []
    with open("words_four_letters.txt","r",encoding="utf8") as f4:
        for word in f4.readlines():
            word = word.strip("\n")
            f4lw.append(word)
    return f4lw

def import_5list():
    f5lw = []
    with open("words_five_letters.txt","r",encoding="utf8") as f5:
        for word in f5.readlines():
            word = word.strip("\n")
            f5lw.append(word)
    return f5lw

def more_words():
    option = 0
    running = True
    words = ""
    print("Which word list would you like to add more words to?")
    while option != "1" or option != "2" or option != "3":
        option = int(input("1. 3 letter words\n2. 4 letter words\n3. 5 letter words\nList: "))
        while running:
            if option == 1:
                with open("words_three_letters.txt","w",encoding="utf8") as f3:
                    new_word = input("What is the new word you would like to add?\nWord: ")
                    while len(new_word) != 3:
                        print("Try again...")
                        new_word = input("Word: ")
                    f3.write(new_word)
            elif option == 2:  
                with open("words_four_letters.txt","w",encoding="utf8") as f4:
                    new_word = input("What is the new word you would like to add?\nWord: ")
                    while len(new_word) != 4:
                        print("Try again...")
                        new_word = input("Word: ")
                    f4.write(new_word)
            elif option == 3:
                with open("words_five_letters.txt","w",encoding="utf8") as f5:
                    new_word = input("What is the new word you would like to add?\nWord: ")
                    while len(new_word) != 5:
                        print("Try again...")
                        new_word = input("Word: ")
                    f5.write(new_word)
                    
            while running:
                    while words.lower() != "y" or words.lower() == "n":  
                        words = input("Would you like to add another word? (y/n)\nInput: ")
                        if words.lower() == "y":
                            continue
                        elif words.lower()== "n":
                            running = False
                        else:
                            print("Something went wrong try again.")
        else:
            print("Try again...\n")

def game_option():
    print("Welcome to Scuffed Wordle!")
    sleep(1.5)
    print("Before we get started we need to figure out what difficulty you want the game to be set to.")
    sleep(1.5)
    print("\nYou will get three options to pick from. 3 letter words, 4 letter words or 5 letter words.")
    sleep(1)
    option = 0
    while option != "1" or option != "2" or option != "3":
        option = int(input("1. 3 letter words\n2. 4 letter words\n3. 5 letter words\nDifficutly: "))
        if option == 1:
            print("You have chosen the 3 letter difficulty.")
            break

        elif option == 2:
            print("You have chosen the 4 letter difficulty.")
            break

        elif option == 3:
            print("You have chosen the 5 letter difficulty.")
            break
        
        else:
            print("Try again...\n")
    
    return option
    
def which_word(letters):
    if letters == 1:
        t3lw = import_3list()
        word = (t3lw[randint(1,((len(t3lw))-1))])
        word = word.lower()
    
    elif letters == 2:
        f4lw = import_4list()
        word = (f4lw[randint(1,((len(f4lw))-1))])
        word = word.lower()
        
    elif letters == 3:
        f5lw = import_5list()
        word = (f5lw[randint(1,((len(f5lw))-1))])
        word = word.lower()
    
    return word

def color_prints(word):
    letter_list = []
    ui_list = []
    guess = 1
    for i in word:
        letter_list.append(i.lower())
    while guess <= 5:
            clearConsole()
            if guess == 1:
                print("Good Luck, Have Fun!")
                print(" _" * (len(word)))  
            else:
                print(" _" * (len(word))) 
                ui_list.append(ui.lower())
                for words in ui_list:
                    counter = 0
                    ic  = 0
                    for letter in words:
                        if letter in letter_list:
                            if words.count(letter) > letter_list.count(letter):
                                x = words.count(letter)
                                counter += 1 
                                if (counter + 2) == x:
                                    if letter == letter_list[ic]:
                                        print(Fore.GREEN, f"{letter.upper()}", end="")
                                    else:
                                        print(Fore.YELLOW, f"{letter.upper()}", end="")
                                        
                                elif counter < x:
                                    if letter == letter_list[ic]:
                                        print(Fore.GREEN, f"{letter.upper()}", end="")
                                    else:
                                        print(Fore.YELLOW, f"{letter.upper()}", end="")

                                elif counter == x:
                                    print(Fore.WHITE, f"{letter.upper()}", end="")
                                
                                else:
                                    print(Fore.WHITE, f"{letter.upper()}", end="")

                            else: 
                                if letter == letter_list[ic]:
                                    print(Fore.GREEN, f"{letter.upper()}", end="")
                                else:
                                    print(Fore.YELLOW, f"{letter.upper()}", end="")

                        else:
                            print(Fore.WHITE, f"{letter.upper()}", end="")
                        ic += 1
                    print(Fore.RESET, "")

            ui = input("")
            while len(ui) != len(word):
                if len(ui) > len(word):
                    print("Sorry your guess has too many letters in it, try again.")
                    ui = input("")
                elif len(ui) < len(word):
                    print("Sorry your guess has too few letters in it, try again.")
                    ui = input("") 
            if ui.lower() == word.lower():
                clearConsole()
                print(f"You guessed correct, the word that was correct was: {word.upper()}!")
                break
            guess += 1
    if ui.lower() != word.lower():
        print(" GAME OVER")
        print(f"Sorry the word that you were looking for was {word.upper()}.")

def main():
    print("All the word list have been loaded, would you like to add more words? (y/n)")
    mw = input("")
    if mw.lower() == "y":
        more_words()
    clearConsole()
    letters = game_option()
    sleep(2)
    word = which_word(letters)
    color_prints(word)

if __name__ == "__main__":
    main()