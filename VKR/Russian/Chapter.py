from VKR.Russian.Sentence import Sentence
from VKR.Russian.ExceptAndSeq import ExceptAndSeq
import networkx as nx
import pylab as plt
import pymorphy2
import sqlite3

morph = pymorphy2.MorphAnalyzer()


class Chapter:

    def __init__(self, name, text, actors, artifacts):
        self.name = name
        self.sentences = list()
        noise = ['...', '.', '?', '!', '\n']
        sentens = []
        for n in noise:
            if len(sentens) ==0:
                sentens = text.split(n)
            else:
                sentens1 = []
                for sen in sentens:
                    for s in sen.split(n):
                        sentens1.append(s)
                sentens = sentens1.copy()

        id = 0
        for snt in sentens:
            if len(snt) > 1:
                nouns = self.parse_nouns(snt,actors, artifacts)
                self.sentences.append(Sentence(snt, id, nouns))
                id += 1



    def parse_nouns(self, words, actors, artifacts):
        nouns=[]
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

        # print(words)

        search_for = voc.get_sequences()

        result = []
        for seq in search_for:
            founds = self.search_sequence(types, seq)
            noun_place = seq.index(['NOUN', 0])

            for found in founds:
                res=""
                for word in found:
                    res += word.word + " "

                res = res[:-1]
                # print(res)
                # print(actors)
                for base, names in actors.items():
                    if res in names:
                        if base not in nouns:
                            nouns.append(base)
                for base, names in artifacts.items():
                    if res in names:
                        if base not in nouns:
                            nouns.append(base)

        # print(words, nouns)
        return nouns

    def showGraph(self):
        dict = {}
        for sentense in self.sentences:
            for i in sentense.nouns:
                for j in sentense.nouns[sentense.nouns.index(i):]:
                    if i==j:
                        continue
                    if (i,j) not in dict and (j,i) not in dict:
                        dict[(i,j)] = []
                        dict[(i, j)].append(sentense.id + 1)
                    elif (i,j) in dict:
                        dict[(i, j)].append(sentense.id + 1)
                    else:
                        dict[(j, i)].append(sentense.id + 1)

        G = nx.Graph()
        labels = {}
        for e, p in dict.items():
            G.add_edge(*e)
            labels[e] = str(p)

        pos = nx.spring_layout(G)

        nx.draw(G, pos, with_labels=True, node_size=20,
                             node_color='black',
                             font_size=10,
                             font_color='red'
                )
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)

        plt.show()
    # пошла жара, определяем что где есть)

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
        changes = {}
        for i in range(len(founds)):
            words = {0:[], 1:[]}
            for index in range(len(founds[i])):
                words[sequence[index][1]].append(founds[i][index])

            case = words[0][0].tag.case
            changes[i] = []
            for word in words[0]:
                if word.tag.case!= case and i not in for_delete:
                    for_delete.append(i)
                else:
                    changes[i].append(word)

            if len(words[1]) > 0:
                case = words[1][0].tag.case
                for word in words[1]:
                    if word.tag.case != case and i not in for_delete:
                        for_delete.append(i)

        n=0
        for index in changes.keys():
            for val in changes[index]:
                i = founds[index].index(val)
                founds[index][i] = founds[index][i].inflect({'nomn'})
        # print(sequence)
        # print(founds)
        # print()

        for i in for_delete:
            founds.remove(founds[i-n])
            indexes.remove(indexes[i-n])
            n+=1

        return founds