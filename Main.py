from Parser import Parser

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

chapter = Parser()
chapter.ParseToBeuty()
chapter.printIt()



