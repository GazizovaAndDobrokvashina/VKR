class Reader:

    def __init__(self, filename):
        self.filename = filename
        try:
            f = open(self.filename)
            f.close()
        except IOError:
            print ("К сожалению файл не найден")

    def get_text(self):
        try:
            f = open(self.filename, encoding='utf-8')
            text = f.readlines()
        except IOError:
            print("Ошибка в считвании")
            text = -1

        return text
