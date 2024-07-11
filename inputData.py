class KoreanSTR:
    def __init__(self, string):
        self.string = string

    def encodeing(self):
        return self.string.encode('euc-kr')
    
# 예제 사용
    Kstring = input("입력하세요 : ")
    print("한국어 : ",Kstring)
    encodingByte = Kstring.encode()
    print("타입 : ", type(encodingByte))
    print("결과 : ", encodingByte)
