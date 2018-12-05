from VKR.Russian.Parser import Parser
from VKR.Russian.Reader import Reader

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

reader = Reader("test.txt")
parser = Parser(reader.get_text())
parser.chapter.showGraph()

# print(parser.actors)
# print(parser.db.get_actors())




