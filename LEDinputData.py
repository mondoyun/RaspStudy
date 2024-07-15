class KoreanSTR:
    def __init__(self):
        pass

    def encodeing(self):
        return self.string.encode('euc-kr')

    def encodedKRstr(self):    
        self.string = input("입력 : ")
        self.InputData = self.string.encode('euc-kr')
        return self.InputData
