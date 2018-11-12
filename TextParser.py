from textblob import TextBlob
import Pretexts


class TextParser:

    def break_to_parts(self, sentence):
        part = sentence
        for word in part.split():
            for pretext in Pretexts.place:
                if word == pretext:
                    part = part.split(pretext)
                    print(1)
            for pretext in Pretexts.cause_target:
                if word == pretext:
                    part = part.split(pretext)
                    print(2)
                    print(part)
            for pretext in Pretexts.direction:
                if word == pretext:
                    part = part.split(pretext)
                    print(3)
            for pretext in Pretexts.time:
                if word == pretext:
                    part = part.split(pretext)
                    print(4)
        print(part)

    def __init__(self, text):
        info = TextBlob(text)
        sentences = info.sentences
        # print(sentences)
        self.break_to_parts(sentences[0])
