class KoreanSTR:
    def __init__(self, string = ""):
        # 빈 문자열 설정
        self.string = string 

    def Encodeing(self):
        # 설정된 문자열을 euc-kr로 인코딩하여 반환하는 메서드
        return self.string.encode('euc-kr')

    def set_string(self, string):
        # 문자열을 설정하는 메서드
        self.string = string

    def encode_string(self):
        # 설정된 문자열을 euc-kr로 인코딩하여 반환하는 메서드
        return self.string.encode('euc-kr')
    
    def KRstring(self):    
        # 사용자가 문자열을 입력하고 인코딩하여 반환하는 메서드
        self.string = "기본문구"
        self.InputData = self.string.encode('euc-kr')
        return self.InputData
