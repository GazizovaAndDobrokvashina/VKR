from VKR.Russian.Sentence import Sentence
from VKR.Russian.Chapter import Chapter
import pymorphy2

morph = pymorphy2.MorphAnalyzer()


class Parser:

    def __init__(self):
        # self.text = "Однажды, готовясь к занятиям главному герою пришлось спуститься в подземелье с артефактами для проведения " \
        #             "небольшой практической работы. Проходя по древним коридорам, осматривая необыкновенные постаменты, " \
        #             "герой совсем забывает о своем бедовом хвосте. И вот на одном из поворотов Азазель чувствует, как его хвост " \
        #             "чего-то касается, а затем слышит за спиной громкий лязг. Ему уже не нужно оборачиваться, чтобы понять, " \
        #             "что он что-то разбил. Все таки оглядываясь назад, лисенок видит то, что и ожидал: груду осколков некоего " \
        #             "артефакта. "
        self.text = "Конюх чистит коня в конюшне. " \
                    "Наездник пришел в конюшню за конем. " \
                    "Наездник на коне поехал в таверну. " \
                    "Конюх пешком пошел в таверну. " \
                    "Наездник подрался с конюхом в таверне."
        self.chapter = Chapter('ТЕСТ', self.text)

    def set_text(self, text):
        self.text = text

