from resources import Three_Letter_Words, Four_Letter_Words, Five_Letter_Words, import_3list, import_4list, import_5list
from time import sleep
from random import randint

def game_option():
    print("Welcome to Scuffed Wordle!")
    sleep(1.5)
    print("Before we get started we need to figure out what difficulty you want the game to be set to.")
    sleep(0.75)
    print()
    sleep(0.75)
    print("You will get three options to pick from. 3 letter words, 4 letter words or 5 letter words.")
    sleep(1)
    
    option = int(input("1. 3 letter words\n2. 4 letter words\n3. 5 letter words\nDifficutly: "))
    if option == 1:
        print("You have chosen the 3 letter difficulty.")

    elif option == 2:
        print("You have chosen the 4 letter difficulty.")
    
    elif option == 3:
        print("You have chosen the 5 letter difficulty.")

    else:
        print("Something went wrong, you will be playing on the 5 letter difficulty.")
        option = 3
    
    return option
    
def play_game(letters):
    sleep(2)
    if letters == 1:
        t3lw = import_3list()
        word = (t3lw[randint(1,((len(t3lw))-1))])
        print("\n"*12)
        print("GL HF")
        print("_ " * (len(word)))
        ui = input("")
        print("\n"*12)
        print("_ " * (len(word)))
        for i in ui:
            print(f"{i} ", end="",)

        


    elif letters == 2:
        f4lw = import_4list()
    elif letters == 3:
        f5lw = import_5list()
    else: print("How did we get to this point with this setting?")

def main():
    letters = game_option()
    play_game(letters)

if __name__ == "__main__":
    main()