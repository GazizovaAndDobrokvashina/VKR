import pymorphy2
from Word import Word
import numpy as np

class Sentence:

    def __init__(self):
        self.words = list()
        self.mests = list()
        # self.lastMest = Word('')
        self.NoDefMest = False
        self.lastNoun = Word('')
        self.HasLast = False

    def addWord(self, word):
        self.words.append(word)

        if word.pos == 'NPRO':
            if self.HasLast:
                word.mestMean = self.lastNoun
            else:
                self.HasLast = True

        if word.pos == 'NOUN':
            self.lastNoun = word
            self.HasLast = True

    def gat2Last(self):
        count = self.words.shape
        return self.words[count-1], self.words[count-2]









