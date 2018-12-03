import pymorphy2
morph = pymorphy2.MorphAnalyzer()

class Sentence:

    def __init__(self, text, id):
        self.id = id
        self.words = text.split()
        self.nouns = list()
        noise = [',', ':']
        # print(self.words)
        for word in self.words:
            for n in noise:
                word = word.replace(n, '')
            typ = morph.parse(word)[0]
            pos = typ.tag.POS
            # case = type.tag.case
            if pos == 'NOUN':
                if typ.normal_form == 'кон':
                    self.nouns.append('конь')
                else:
                    self.nouns.append(typ.normal_form)

        print(self.words, id)
        print(self.nouns)
        print()

