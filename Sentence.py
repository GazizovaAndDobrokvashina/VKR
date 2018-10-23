import pymorphy2
from Word import Word
import numpy as np


class Sentence:

    def __init__(self):
        self.words = list()
        self.mests = list()
        self.NoDefMest = False
        self.lastNoun = Word('')
        self.HasLast = False
        self.podl = ''

    def add_word(self, word):

        if word.pos == 'NPRO':
            self.mests.append(word)
            if self.HasLast:
                word.mestMean = self.try_to_find_meaning(word)
            else:
                self.lastNoun = word
                self.HasLast = True
                self.NoDefMest = True

        if word.pos == 'NOUN':
            if word.case == 'nomn':
                self.podl = word
            self.lastNoun = word
            self.HasLast = True

        self.words.append(word)

    def try_to_find_meaning(self, mest, in_class = True):
        for word in self.words:
            if (word.pos == 'NOUN' or word.pos == 'NPRO') and word.case == mest.case:
                return word

        if in_class:
            self.NoDefMest = True
        return
