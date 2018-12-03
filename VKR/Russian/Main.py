from VKR.Russian.Parser import Parser

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

chapter = Parser()
chapter.chapter.showGraph()
# chapter.parse_to_beuty()
# chapter.print_it()



