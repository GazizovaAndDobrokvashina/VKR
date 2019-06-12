
class ExceptAndSeq:

    def get_exceptions(self):
        exceptions = {'кость': ['NOUN', 'кость'],
                      'рыжий': ['ADJF', 'рыжий'],
                      'молодой': ['ADJF', 'молодой'],
                      'псов': ['NOUN', 'пёс']}
        return exceptions

    def get_sequences(self):
        search_for = [[['ADJF', 0], ['NOUN', 0]],
                      [['NOUN', 0], ['NOUN', 1]],
                      [['NOUN', 0], ['ADJF', 1], ['NOUN', 1]],
                      [['NOUN', 0], ['PRTF', 1], ['NOUN', 1]],
                      [['ADJF', 0], ['ADJF', 0], ['NOUN', 0]],
                      [['NOUN', 0]]]
        return search_for