from VKR.Russian.Sentence import Sentence
from VKR.Russian.Chapter import Chapter
from VKR.Russian.Actors import Actors
from VKR.Russian.Artifacts import Artifacts
import pymorphy2
import sqlite3

morph = pymorphy2.MorphAnalyzer()


class Parser:

    def __init__(self, text = 0):

        self.text = text
        self.chapter = Chapter('', '', {}, {})
        self.db = 0
        self.actors = {}
        self.artifacts = {}
        if self.text == 0:
            # self.text = "Конюх чистит коня в конюшне. " \
            #         "Наездник пришел в конюшню за конем. " \
            #         "Наездник на коне поехал в таверну. " \
            #         "Конюх пешком пошел в таверну. " \
            #         "Наездник подрался с конюхом в таверне."
            # self.chapter = Chapter('ТЕСТ', self.text)
            print("NO TEXT ADDED")
        else:
            no_name = True
            next_chapter = False
            next_artifact = False
            next_persons = False
            for line in self.text:
                if no_name:
                    self.conn = sqlite3.connect(line[:-1]+'.db')
                    self.acDB = Actors(self.conn)
                    self.arDB = Artifacts(self.conn)
                    no_name = False
                if line == "Главные герои\n":
                    next_persons = True
                    continue
                elif line == "Артефакты\n":
                    next_persons = False
                    next_chapter = False
                    next_artifact = True
                    continue
                elif line == "Сюжет\n":
                    next_chapter = True
                    next_persons = False
                    next_artifact = False
                    continue
                elif line == "\n":
                    continue
                if next_persons:
                    names = line.split('-')
                    base_name = names[0]
                    noise = [',', ':', '.', '\n']
                    for n in noise:
                        line = line.replace(n, '')
                        base_name = base_name.replace(n, '')
                    names = self.parse_names(line.replace('-',' '))
                    self.actors[base_name] = names
                if next_chapter:
                    self.chapter = Chapter('Сюжет', line, self.actors, self.artifacts)
                    next_chapter = False
                if next_artifact:
                    names = line.split('-')
                    base_name = names[0]
                    noise = [',', ':', '.', '\n']
                    for n in noise:
                        line = line.replace(n, '')
                        base_name = base_name.replace(n, '')
                    names = self.parse_names(line.replace('-', ' '))
                    self.artifacts[base_name] = names

            for key in self.actors:
                self.acDB.add_actor(key, self.actors[key])
            for key in self.artifacts:
                self.arDB.add_artifact(key, self.artifacts[key])

    def parse_names(self, names):
        words = names.split()
        nams = []
        adjectives = []
        nouns = []
        for word in words:

            typ = morph.parse(word)[0]
            pos = typ.tag.POS
            add_case = False
            if word == ' ':
                continue
            if word == "который" or word == "которое" or word == "которая":
                add_case = True
            elif pos == 'ADJF' or pos == 'ADJS' or pos == 'PRTF' or pos == 'PRTS':
                adjectives.append(typ.inflect({'sing', 'nomn'}).word)
            elif pos == 'NOUN' and ((add_case and typ.tag.case == 'ablt') or typ.tag.case == 'nomn' or typ.tag.case == 'gent'):
                nouns.append(typ.normal_form)
            elif pos == 'NOUN' and typ.tag.case == 'nomn':
                nouns.append(typ.normal_form)
                add_case = True
            elif typ.tag == morph.parse("Азазель.")[0].tag or word.lower() == "кость" and word.lower() not in nams:
                nams.append(word.lower())
                add_case = True
        # print(adjectives)
        # print(nouns)
        for noun in nouns:
            nams.append(noun)
        for adj in adjectives:
            for noun in nouns:
                nams.append(adj + ' ' + noun)

        return nams

    



