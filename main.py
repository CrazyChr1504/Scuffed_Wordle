from time import sleep
from random import randint
import os
import colorama
from colorama import Fore

colorama.init()
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def import_letter_list(option):
    """
    Imports the word list for the chosen amount of letters.

    Args:
        Takes in the option argument and checks the integer associated with the option to choose the text file to read from.

    Returns:
        A list of the words that were in the word text file'.
    """
    path = ""
    if option == 3: path = "words_three_letters.txt"
    elif option == 4: path = "words_four_letters.txt"
    elif option == 5: path = "words_five_letters.txt"

        
    wordlist = []
    with open(path,"r",encoding="utf8") as f3:
        for word in f3.readlines():
            word = word.strip("\n")
            wordlist.append(word)       

    return wordlist

def more_words():
    """
    Adds more words to the chosen word list and checks if the word is the correct length.
    """
    path = ""
    option = 0
    running = True
    words_added = True
    clearConsole()
    print("Which word list would you like to add more words to?")
    while True:
        option = int(input("3. 3 letter words\n4. 4 letter words\n5. 5 letter words\nList: "))
        if option == 3 or option == 4 or option == 5:
            break
        print("Try again...\n")

    if option == 3: path = "words_three_letters.txt"
    elif option == 4: path = "words_four_letters.txt"
    elif option == 5: path = "words_five_letters.txt"
    
    with open(path,"a",encoding="utf8") as f:
        while running:
            clearConsole()
            new_word = input("What is the new word you would like to add?\nWord: ")
            while len(new_word) != option:
                if len(new_word) > option: print("The word was too long.")
                elif len(new_word) < option: print("The word was too short.")
                print(f"The word needs to be {option}letters long.\nTry again...")
                new_word = input("Word: ")
            f.write(f"\n{new_word}")
            f.close()
                    
            words = ""
            while words_added:  
                words = input("Would you like to add another word? (y/n)\nInput: ")
                if words.lower() == "y":
                    break
                elif words.lower()== "n":
                    running = False
                    break
                else:
                    print("Something went wrong try again.")

def game_option():
    """
    Setup for the difficulty of the game.

    Returns:
        The option of chosen amount of letters.
    """
    print("Welcome to Scuffed Wordle!")
    sleep(1.5)
    print("Before we get started we need to figure out what difficulty you want the game to be set to.")
    sleep(1.5)
    print("\nYou will get three options to pick from. 3 letter words, 4 letter words or 5 letter words.")
    sleep(1)
    option = 0
    while True:
        option = int(input("3. 3 letter words\n4. 4 letter words\n5. 5 letter words\nDifficutly: "))
        if option == 3:
            print("You have chosen the 3 letter difficulty.")
            break

        elif option == 4:
            print("You have chosen the 4 letter difficulty.")
            break

        elif option == 5:
            print("You have chosen the 5 letter difficulty.")
            break
        
        else:
            print("Try again...\n")
    
    return option
    
def which_word(option):
    """
    Imports the list of words in a text file and then chooses a random word from the list to use.

    Args:
        Takes in the option of how many letter the word should have and calls for the imported word list with the according word length.

    Returns:
        The randomized word from the chosen word lists.
    """
    word = import_letter_list(option)
    word = (word[randint(1,((len(word))-1))])
    word = word.lower()
    
    return word

def color_prints(word):
    """
    The main function for the program, makes the color prints for each word that was guessed when compared with the random word that was chosen.

    Args:
        Takes in the word that was randomized and uses it as a referance.
    """
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
        clearConsole()
        print("GAME OVER")
        print(f"Sorry the word that you were looking for was {word.upper()}.")

def main():
    """
    The main function to the program.
    """
    print("All the word list have been loaded, would you like to add more words? (y/n)")
    mw = ""
    while mw == "":
        mw = input()
        if mw.lower() == "y":
            more_words()
            break
        elif mw.lower() == "n":
            break
        mw = input("Sorry something went wrong, try again...\n(y/n): ")
    clearConsole()
    option = game_option()
    sleep(2)
    word = which_word(option)
    color_prints(word)

if __name__ == "__main__":
    main()