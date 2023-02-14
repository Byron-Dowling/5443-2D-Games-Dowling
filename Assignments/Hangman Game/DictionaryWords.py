"""
    Author:   Byron Dowling
    Class:    5443 2D Python Gaming

"""

import copy
from random import shuffle

"""
    The purpose of this class is to load the potential words
    for the hangman game, turn the words into a list of characters
    for future use, and to generate a random selection for the start
    of a new game.
"""
class HMW:

    def __init__(self):
        self.Words = []

        self.Parse()
        self.Shuffle()


    def Parse(self):
        temp = []
        bool_list = []

        Entry = {"Word": "", "Letters": list(), "Guessed": list()}

        with open ("HMW.txt") as Fin:
            temp = Fin.readlines()

        for t in temp:
            L1 = list(t)

            if L1[-1] == '\n':
                L1.pop()

            Entry["Word"] = t
            Entry["Letters"] = L1

            for i in range(len(L1)):
                bool_list.append(False)
            
            Entry["Guessed"] = bool_list

            self.Words.append(copy.deepcopy(Entry))
            bool_list.clear()

        


    def Visualize(self):
        for word in self.Words:
            print(word)

    def Shuffle(self):
        shuffle(self.Words)

    def SelectWord(self):
        return self.Words[0]



if __name__ == '__main__':
    
    C4 = HMW()

    # C4.Parse()
    # C4.SelectWord()
    # print("Shuffling...")
    # C4.Shuffle()

    entry = C4.SelectWord()
    print(entry)
