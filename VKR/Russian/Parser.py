from Russian.Word import Word
from Russian.Sentence import Sentence
from Russian.Chapter import Chapter
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

    def set_text(self, text):
        self.text = text

    def parse_to_beuty(self):
        self.chapter = Chapter('First')
        sentence = Sentence()
        word = ''
        new_word = ''
        word_end = False
        sentence_end = False
        for i in self.text:
            if sentence_end:
                if i == ('.' or '!' or '?'):
                    word += i
                else:
                    sentence.add_word(Word(word))
                    self.chapter.add_sentence(sentence)
                    sentence = Sentence()
                    word = ''
                    sentence_end = False
                    continue

            if word_end:
                if not i == ' ':
                    word += new_word
                else:
                    sentence.add_word(Word(word))
                    word = new_word
                word_end = False

            if i == ('.' or '!' or '?'):
                sentence_end = True
                sentence.add_word(Word(word))
                word = i
            elif i == ' ':
                sentence.add_word(Word(word))
                word = ''
            elif 'PNCT' in morph.parse(i)[0].tag:
                word_end = True
                new_word = i
            else:
                word += i

        return self.chapter

    def print_it(self):
        out = ''
        for sentence in self.chapter.sentences:
            for word in sentence.words:
                if 'PNCT' not in word.type.tag:
                    out += ' '
                if word.pos == 'NPRO':
                    if not word.mestMean == '':
                        out += word.word + '(1)'# + word.mestMean.word + ')'
                    else:
                        out += word.word + '()'
                else:
                    out += word.word

        print(out)
