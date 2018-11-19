from textblob import TextBlob
import Pretexts
from SyntaxPart import SyntaxPart
import numpy as np


class TextParser:

    def break_to_parts(self, sentence_original):
        sentence_massive = {SyntaxPart(sentence_original)}
        for syntaxP in sentence_massive:
            for pretext in Pretexts.cause_target:
                if pretext in syntaxP.text:
                    self.split_part(syntaxP, pretext, "cause_target")
            #        part = part.split(pretext)
            #        print(1)
            # for pretext in Pretexts.cause_target:
            #     if word == pretext:
            #         part = part.split(pretext)
            #         print(2)
            #         print(part)
            # for pretext in Pretexts.direction:
            #     if word == pretext:
            #         part = part.split(pretext)
            #         print(3)
            # for pretext in Pretexts.time:
            #     if word == pretext:
            #         part = part.split(pretext)
            #         print(4)

    def split_part(self, part, pretext, type_pretext):
        new_part = SyntaxPart(part.text[part.text.index(pretext):], pretext, type_pretext)
        print(new_part.text)

    def __init__(self, text):
        info = TextBlob(text)
        sentences = info.sentences
        # print(sentences)
        self.break_to_parts(sentences[0])
