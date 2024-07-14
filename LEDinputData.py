class KoreanSTR:
    def __init__(self, string):
        self.string = string

    def encodeing(self):
        return self.string.encode('euc-kr')
    
