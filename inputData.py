class KoreanSTR:
    def __init__(self, string):
        self.string = string

    def encodeing(self):
        return self.string.encode('euc-kr')
    
if __name__ == "__main__":
    
    Kstring = input("입력하세요 : ")
    print("한국어 : ",Kstring)
    kstr = KoreanSTR(Kstring)
    encodingByte = kstr.encodeing()
    print("타입 : ", type(encodingByte))
    print("결과 : ", encodingByte)
