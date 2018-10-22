from Word import Word
from Sentence import Sentence
from Chapter import Chapter
import pymorphy2

morph = pymorphy2.MorphAnalyzer()


class Parser:

    def __init__(self):
        self.text = "Однажды, готовясь к занятиям главному герою пришлось спуститься в подземелье с артефактами для проведения " \
                    "небольшой практической работы. Проходя по древним коридорам, осматривая необыкновенные постаменты, " \
                    "герой совсем забывает о своем бедовом хвосте. И вот на одном из поворотов Азазель чувствует, как его хвост " \
                    "чего-то касается, а затем слышит за спиной громкий лязг. Ему уже не нужно оборачиваться, чтобы понять, " \
                    "что он что-то разбил. Все таки оглядываясь назад, лисенок видит то, что и ожидал: груду осколков некоего " \
                    "артефакта. "
        self.chapter = Chapter('')

    def setText(self, text):
        self.text = text

    def ParseToBeuty(self):
        self.chapter = Chapter('First')
        sentence = Sentence()
        word = ''
        wordEnd = False
        sentenceEnd = False
        for i in self.text:
            if i == '.':
                sentenceEnd = True
                self.chapter.AddSentence(sentence)
                sentence = Sentence()
            elif i == ' ':
                wordEnd = True
                sentence.addWord(Word(word))
                word = ''
            elif 'PNCT' in morph.parse(i)[0].tag:
                wordEnd = True
                sentence.addWord(Word(word))
                word = ''
                newWord = i
            else:
                word += i


        return self.chapter

    def printIt(self):
        out = ''
        for sentence in self.chapter.sentences:
            for word in sentence.words:
                if 'PNCT' not in word.type.tag:
                    out += ' '
                if word.pos == 'NPRO':
                    out += word.word + '(' + word.mestMean.word + ')'
                else:
                    out += word.word

        print(out)