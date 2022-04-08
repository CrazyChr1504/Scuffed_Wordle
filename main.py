from resources import Three_Letter_Words, Four_Letter_Words, Five_Letter_Words, import_3list, import_4list, import_5list
from time import sleep

def game_option():
    print("Welcome to Scuffed Wordle!")
    sleep(1)
    print("Before we get started we need to figure out what difficulty you want the game to be set to.")
    sleep(1)
    print("You will get three optionsv to pick from. 3 letter words, 4 letter words or 5 letter words.")
    sleep(0.5)
    
    option = int(input("1. 3 letter words\n2. 4 letter words\n 3. 5 letter words\nDifficutly: "))
    if option == 1:
        print("You have chosen the 3 letter difficulty.")
        return option

    elif option == 2:
        print("You have chosen the 4 letter difficulty.")
        return option
    
    elif option == 3:
        print("You have chosen the 5 letter difficulty.")
        return option
    
    else:
        print("Something went wrong, you will be playing on the 5 letter difficulty.")
        option = 3
        return option
    
def play_game():
    pass

def main():
    t3lw = import_3list()
    f4lw = import_4list()
    f5lw = import_5list()
    letters = game_option()


if __name__ == "__main__":
    main()