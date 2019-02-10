from VKR.Russian.ExceptAndSeq import ExceptAndSeq
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
                if line == "Персонажи\n":
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
                    names = self.parse_words(line.replace('-',' '))
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
                    names = self.parse_words(line.replace('-', ' '))
                    self.artifacts[base_name] = names

            for key in self.actors:
                self.acDB.add_actor(key, self.actors[key])
            for key in self.artifacts:
                self.arDB.add_artifact(key, self.artifacts[key])

    def parse_words(self, words):
        words = words.split()
        noise = [',', ':', '\n']
        voc = ExceptAndSeq()
        clear_words = []
        for word in words:
            for n in noise:
                word.replace(n, '')
            clear_words.append(word.lower())

        types = [morph.parse(word)[0] for word in clear_words]

        exeptions = voc.get_exceptions()

        for index in range(len(clear_words)):
            if clear_words[index] in exeptions.keys():
                for typ in morph.parse(clear_words[index]):
                    if typ.tag.POS == exeptions[clear_words[index]][0] \
                            and typ.normal_form == exeptions[clear_words[index]][1]:
                        types[index] = typ
                        break

        # print(clear_words)
        # print(types)

        search_for = voc.get_sequences()

        result = []
        for seq in search_for:
            indexes = self.search_sequence(types, seq)
            nums = self.multi_adj(seq)
            noun_place = seq.index(['NOUN', 0])
            for i in indexes:
                name = clear_words[i:i+len(seq)]
                res = ''
                for i in range(len(seq)):
                    res += name[i] + ' '
                res = res[:-1]
                result.append(res)
                if len(nums) > 1:
                    noun =  name[noun_place]
                    result.append(noun)
                    for i in nums:
                        add = name[i] + ' ' + noun
                        result.append(add)

        return result



    def multi_adj(self, sequence):
        nums = []
        for i in range(len(sequence)):
            if sequence[i] == 'ADJF':
                nums.append(i)

        return nums

    def search_sequence(self, sentence, sequence):
        j = 0
        founds = []
        curr = []
        indexes = []
        cur = 0
        for i in range(len(sentence)):
            if sentence[i].tag.POS == sequence[j][0]:
                if j==0:
                    cur = i
                curr.append(sentence[i])
                j += 1
                if j == len(sequence):
                    founds.append(curr)
                    curr = []
                    j = 0
                    indexes.append(cur)
            else:
                if j != 0:
                    j = 0
                    curr = []

        for_delete = []
        for i in range(len(founds)):
            words = {0:[], 1:[]}
            for index in range(len(founds[i])):
                words[sequence[index][1]].append(founds[i][index])

            for word in words[0]:
                if word.tag.case!= 'nomn' and i not in for_delete:
                    for_delete.append(i)

            if len(words[1]) > 0:
                case = words[1][0].tag.case
                for word in words[1]:
                    if word.tag.case != case and i not in for_delete:
                        for_delete.append(i)

        n=0
        for i in for_delete:
            founds.remove(founds[i-n])
            indexes.remove(indexes[i-n])
            n+=1
        # print(sequence)
        # print(founds)
        # print()

        return indexes


