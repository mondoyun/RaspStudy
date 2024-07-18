class KoreanStringEncoder:
    def __init__(self): 
        pass
    
    def KRstring(self):   # __ private 
        # 사용자가 문자열을 입력하고 인코딩하여 반환하는 메서드
        string = input("입력 : ")
        self.InputData = string.encode('euc-kr')
        return self.InputData


