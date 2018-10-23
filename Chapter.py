import pymorphy2
from Sentence import Sentence
from Word import Word
import numpy as np


class Chapter:

    def __init__(self, name):
        self.name = name
        self.sentences = list()

    def add_sentence(self, sentence):
        self.sentences.append(sentence)
        if sentence.NoDefMest:
            self.find_defs_for_mests(sentence)
        sentence.chapter = self

    def find_defs_for_mests(self, sentence):
        global salvation
        for mest in sentence.mests:
            if mest.mestMean == '':
                found = False
                while not found:
                    if self.get_previous(sentence) != 0:
                        salvation = self.get_previous(sentence).podl
                        if salvation is not None:
                            print(salvation.word)
                            found = True
                    found = True
                if salvation is not None:
                    mest.mestMean = salvation

            elif mest.mestMean is not None and mest.mestMean.pos == 'NPRO':
                deep_mest = mest.mestMean.mestMean
                while deep_mest != '' and deep_mest == 'NPRO':
                    deep_mest = deep_mest.mestMean

                if deep_mest != '':
                    mests = mest.mestMean
                    while mests == 'NPRO':
                        mesta = mests.mestMean
                        mests = deep_mest
                        mests = mesta

        return

    def get_previous(self, sentence):
        print(self.sentences.index(sentence))
        print()
        if self.sentences.index(sentence) - 1 > -1:
            return self.sentences[self.sentences.index(sentence) - 1]
        else:
            return
