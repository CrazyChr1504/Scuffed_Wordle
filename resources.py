# Imports
# Classes
class Word_lists:
    def __init__(self, three_letters : list, four_letters : list, five_letters : list):
        self.three_letters = three_letters
        self.four_letters = four_letters
        self.five_letters = five_letters
        
    def get_three_letter(self):
        return self.three_letters
    
    def get_four_letter(self):
        return self.four_letters

    def get_five_letter(self):
        return self.five_letters
# Functions
def import_lists():
    
    with open("words_three_letters.txt","r",encoding="utf8") as f3:
        t3lw = []
        for word in f3.readlines():
            t3lw.append(word)
    
    with open("words_four_letters.txt","r",encoding="utf8") as f4:
        f4lw = []
        for word in f4.readlines():
            f4lw.append(word)
    
    with open("words_five_letters.txt","r",encoding="utf8") as f5:
        f5lw = []
        for word in f5.readlines():
            f5lw.append(word)
        
    Word_lists(t3lw,f4lw,f5lw)