from VKR.Russian.Sentence import Sentence
import networkx as nx
import matplotlib.pyplot as plt


class Chapter:

    def __init__(self, name, text):
        self.name = name
        self.sentences = list()
        noise = ['...', '.', '?', '!']
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
                self.sentences.append(Sentence(snt, id))
                id += 1

    def showGraph(self):
        dict = {
            'yellow': {}}
        for sentense in self.sentences:
            for i in sentense.nouns:
                for j in sentense.nouns[sentense.nouns.index(i):]:
                    if i==j:
                        continue
                    if (i,j) not in dict['yellow'] and (j,i) not in dict['yellow']:
                        dict['yellow'][(i,j)] = []
                        dict['yellow'][(i, j)].append(sentense.id + 1)
                    elif (i,j) in dict['yellow']:
                        dict['yellow'][(i, j)].append(sentense.id + 1)
                    else:
                        dict['yellow'][(j, i)].append(sentense.id + 1)

        print(dict.values())
        g = nx.DiGraph()
        for slovar in dict.values():
            for e, p in slovar.items():
                g.add_edge(*e, weight=p, edge_label=str(e))
            nx.draw_circular(g,
                             with_labels=True,
                             node_size=50,
                             node_color='r',
                             node_shape='.',
                             font_size=14,
                             font_color='b',
                             font_family='monospace',
                             font_weight='book',
                             horizontalalignment='left',
                             verticalalignment='center'
                             )
            # pos = nx.spring_layout(g)
            pos = nx.spring_layout(g, weight=None)
            # edge_labels = {i[0:2]: '${}'.format(i[2]['weight']) for i in g.edges(data=True)}
            # nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=edge_labels)
            # nx.draw_networkx_edge_labels(g, )

            plt.show()