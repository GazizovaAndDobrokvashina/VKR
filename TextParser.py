from textblob import TextBlob


class TextParser:

    def __init__(self, text):
        info = TextBlob(text)
        sentences = info.sentences
        print(sentences)
