class KoreanSTR:
    def __init__(self, string):
        string = input("입력하세요 : ")
        self.string = string

    def encodeing(self):
        return self.string.encode('euc-kr')

    def encodedKRstr(self):    
        str = self.string.encode('euc-kr')
        self.InputData = str
        return self.InputData
