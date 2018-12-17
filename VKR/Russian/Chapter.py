from VKR.Russian.Sentence import Sentence
import networkx as nx
import pylab as plt


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
                self.sentences.append(Sentence(snt, id, actors, artifacts))
                id += 1

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

        print(dict.items())

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
