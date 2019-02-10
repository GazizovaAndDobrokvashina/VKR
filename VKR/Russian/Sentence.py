import pymorphy2
morph = pymorphy2.MorphAnalyzer()

class Sentence:

    def __init__(self, text, id, nouns):
        self.id = id
        self.words = text.split()
        self.nouns = nouns
        noise = [',', ':', '\n']
        # print(self.words)
        for word in self.words:
            for n in noise:
                word = word.replace(n, '')
        #     typ = morph.parse(word)[0]
        #     pos = typ.tag.POS
        #     # case = type.tag.case
        #     if pos == 'NOUN' or word.lower() == 'кость':
        #         # if typ.normal_form == 'кон':
        #         #     self.nouns.append('конь')
        #         # else:
        #         #     self.nouns.append(typ.normal_form)
        #         flag = False
        #         for key in actors:
        #             if not flag:
        #                 for val in actors[key]:
        #                     if typ.normal_form == val and key not in self.nouns:
        #                         self.nouns.append(key)
        #                         flag = True
        #         for key in artifacts:
        #             if not flag:
        #                 for val in artifacts[key]:
        #                     if (typ.normal_form == val or word.lower() == 'кость' == val) and key not in self.nouns:
        #                         self.nouns.append(key)
        #                         flag = True


        # print(self.words, id)
        # print(self.nouns)
        # print()
