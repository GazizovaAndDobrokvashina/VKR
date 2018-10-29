import pymorphy2
morph = pymorphy2.MorphAnalyzer()


class Word:

    def __init__(self, word):
        self.word = word
        self.type = morph.parse(word)[0]
        self.pos = self.type.tag.POS
        self.case = self.type.tag.case
        self.mestMean = ''


