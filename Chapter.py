import pymorphy2
from Sentence import Sentence
from Word import Word
import numpy as np


class Chapter:

    def __init__(self, name):
        self.name = name
        self.sentences = list()


    def AddSentence(self, sentence):
        self.sentences.append(sentence)
