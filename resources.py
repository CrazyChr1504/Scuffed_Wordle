# Imports

# Classes

class Three_Letter_Words:
    def __init__(self, word_list3 : list):
        self.word_list3 = word_list3

    def get_word_list3(self):
        return self.word_list3
        
    def add_words3(self):
        print("How many words would you like to add to the word list?")
        amount = input("Amount: ")
        for _ in range(amount):
            word = input("\nWhat word would you like to add?\nWord: ")
            self.word_list3.append(word)
        return self.word_list3

class Four_Letter_Words:
    def __init__(self, word_list4 : list):
        self.word_list4 = word_list4

    def get_word_list4(self):
        return self.word_list4
        
    def add_words3(self):
        print("How many words would you like to add to the word list?")
        amount = input("Amount: ")
        for _ in range(amount):
            word = input("\nWhat word would you like to add?\nWord: ")
            self.word_list4.append(word)
        return self.word_list4

class Five_Letter_Words:
    def __init__(self, word_list5 : list):
        self.word_list5 = word_list5

    def get_word_list3(self):
        return self.word_list5
        
    def add_words3(self):
        print("How many words would you like to add to the word list?")
        amount = input("Amount: ")
        for _ in range(amount):
            word = input("\nWhat word would you like to add?\nWord: ")
            self.word_list5.append(word)
    
# Functions
def import_3list():
    t3lw = []
    with open("words_three_letters.txt","r",encoding="utf8") as f3:
        for word in f3.readlines():
            t3lw.append(word)
    return t3lw
    
def import_4list():
    f4lw = []
    with open("words_four_letters.txt","r",encoding="utf8") as f4:
        for word in f4.readlines():
            f4lw.append(word)
    return f4lw

def import_5list():
    f5lw = []
    with open("words_five_letters.txt","r",encoding="utf8") as f5:
        for word in f5.readlines():
            f5lw.append(word)
    return f5lw
