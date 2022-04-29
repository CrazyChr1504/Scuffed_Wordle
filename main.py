from resources import import_3list, import_4list, import_5list, more_words
from time import sleep
from random import randint
import os
import colorama
from colorama import Fore
colorama.init()

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def game_option():
    print("Welcome to Scuffed Wordle!")
    sleep(1.5)
    print("Before we get started we need to figure out what difficulty you want the game to be set to.")
    sleep(0.75)
    print()
    sleep(0.75)
    print("You will get three options to pick from. 3 letter words, 4 letter words or 5 letter words.")
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
    
def play_game(letters):
    letter_list = []
    ui_list = []
    guess = 0

    sleep(2)
    if letters == 1:
        t3lw = import_3list()
        word = (t3lw[randint(1,((len(t3lw))-1))])
        word = word.lower()
        for i in word:
            letter_list.append(i.lower())

        while guess <= 4:
            clearConsole()
            ic = 0
            if guess == 0:
                print("GL HF")
                print(" _" * (len(word)))  
            else:
                print(" _" * (len(word))) 
                ui_list.append(ui.lower())
                for words in ui_list:
                    for letter in words:
                        if letter in letter_list:
                            if letter == letter_list[ic]:
                                print(Fore.GREEN, f"{letter.upper()}", end="")
                            else:
                                print(Fore.YELLOW, f"{letter.upper()}", end="")
                        else:
                            print(Fore.WHITE, f"{letter.upper()}", end="")
                        ic += 1
                        if ic == 3: 
                            ic = 0
                    print(Fore.RESET, "")

            ui = input("")
            if ui.lower() == word.lower():
                clearConsole()
                print(f"You guessed correct, the word that was correct was: {word.upper()}!")
                break
            while len(ui) != len(word):
                if len(ui) > len(word):
                    print("Sorry your guess has too many letters in it, try again.")
                    ui = input("")
                elif len(ui) < len(word):
                    print("Sorry your guess has too few letters in it, try again.")
                    ui = input("") 
            guess += 1
        if ui.lower() != word.lower():
            print(" GAME OVER")
            print(f"Sorry the word that you were looking for was {word.upper()}.")
    elif letters == 2:
        f4lw = import_4list()
        word = (f4lw[randint(1,((len(f4lw))-1))])
        word = word.lower()
        for i in word:
            letter_list.append(i.lower())
        while guess <= 4:
            clearConsole()
            ic = 0
            
            if guess == 0:
                print("GL HF")
                print(" _" * (len(word)))  
            else:
                print(" _" * (len(word))) 
                ui_list.append(ui.lower())
                for words in ui_list:
                    for letter in words:
                        if letter in letter_list:
                            if letter == letter_list[ic]:
                                print(Fore.GREEN, f"{letter.upper()}", end="")
                            else:
                                print(Fore.YELLOW, f"{letter.upper()}", end="")
                        else:
                            print(Fore.WHITE, f"{letter.upper()}", end="")
                        ic += 1
                        if ic == 4: 
                            ic = 0
                    print(Fore.RESET, "")

            ui = input("")
            if ui.lower() == word.lower():
                clearConsole()
                print(f"You guessed correct, the word that was correct was: {word.upper()}!")
                break
            while len(ui) != len(word):
                if len(ui) > len(word):
                    print("Sorry your guess has too many letters in it, try again.")
                    ui = input("")
                elif len(ui) < len(word):
                    print("Sorry your guess has too few letters in it, try again.")
                    ui = input("") 
            guess += 1
        if ui.lower() != word.lower():
            print(" GAME OVER")
            print(f"Sorry the word that you were looking for was {word.upper()}.")
    elif letters == 3:
        f5lw = import_5list()
        word = (f5lw[randint(1,((len(f5lw))-1))])
        word = word.lower()
        for i in word:
            letter_list.append(i.lower())
        while guess <= 4:
            clearConsole()
            ic = 0
            
            if guess == 0:
                print("GL HF")
                print(" _" * (len(word)))  
            else:
                print(" _" * (len(word))) 
                ui_list.append(ui.lower())
                for words in ui_list:
                    for letter in words:
                        if letter in letter_list:
                            if letter == letter_list[ic]:
                                print(Fore.GREEN, f"{letter.upper()}", end="")
                            else:
                                print(Fore.YELLOW, f"{letter.upper()}", end="")
                        else:
                            print(Fore.WHITE, f"{letter.upper()}", end="")
                        ic += 1
                        if ic == 5: 
                            ic = 0
                    print(Fore.RESET, "")

            ui = input("")
            if ui.lower() == word.lower():
                clearConsole()
                print(f"You guessed correct, the word that was correct was: {word.upper()}!")
                break
            while len(ui) != len(word):
                if len(ui) > len(word):
                    print("Sorry your guess has too many letters in it, try again.")
                    ui = input("")
                elif len(ui) < len(word):
                    print("Sorry your guess has too few letters in it, try again.")
                    ui = input("") 
            guess += 1
        if ui.lower() != word.lower():
            print(" GAME OVER")
            print(f"Sorry the word that you were looking for was {word.upper()}.")
    else: print("How did we get to this point with this setting?")

def main():
    print("All the word list have been loaded, would you like to add more words? (y/n)")
    mw = input("")
    if mw.lower() == "y":
        more_words()
    letters = game_option()
    play_game(letters)

if __name__ == "__main__":
    main()