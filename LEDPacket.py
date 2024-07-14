from LEDinputData import KoreanSTR

class Protocol:
    def __init__ (self):
        self.HeaderFrame = b'\x7E\x01'
        self.ScreenID = b'\xFE\xFE'
        self.crc = b'\xFF\xFF' 
        self.eof = b'\x7E\x00'
        self.DataLength = b'\x00\x0B'
        self.CmdEvent = b'\x50\x57\x4F\x4E'
        self.Length = b'\x00'
        self.program_id = b'\x00\x00\x00\x00\x00'

    # 패킷통신 - 시작고정값,고정구조
    def FixedStart(self):
        return self.HeaderFrame + self.ScreenID
    
    # 패킷통신 - 끝고정값,고정구조
    def FixedEnd(self):
        return self.crc + self.eof
    
    # LED 전광판 전원 ON
    def PowerOn(self):
        self.SubCmdID = b'\x02' # 전원 ON    
        self.OnMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length + self.program_id
        self.on = self.FixedStart() + self.OnMSG + self.FixedEnd()
        return self.on

    # LED 전광판 전원 OFF
    def PowerOFF(self):
        self.SubCmdID = b'\x03' # 전원 OFF
        self.OffMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length + self.program_id
        self.OFF = self.FixedStart() + self.OffMSG + self.FixedEnd()
        return self.OFF

    # 이벤트 초기화
    def InitEventMemory(self):
        self.DataLength = b'\x00\x08'
        self.CmdEvent = b'\x45\x56\x45\x4E'
        self.SubCmdID = b'\x01' # 이벤트 초기화
        self.Length = b'\x02'
        self.program_id = b'\x04\x00'
        self.initMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length + self.program_id
        self.initMemory = self.FixedStart() + self.initMSG + self.FixedEnd()
        return self.initMemory
    
    # 화면출력
    def startWindows(self):
        self.DataLength = b'\x00\x08'
        self.CmdEvent = b'\x45\x56\x45\x4E'
        self.SubCmdID = b'\x07' # 화면 출력
        self.Length = b'\x02'
        self.Reserved_Wnd = b'\xFF'
        self.Reserved = b'\x00'
        self.windowMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length + self.Reserved_Wnd + self.Reserved
        self.startwindow = self.FixedStart() + self.windowMSG + self.FixedEnd()
        return self.startwindow
    
    # 버퍼 삭제
    def ClearBuffer(self):
        self.DataLength = b'\x00\x07'
        self.CmdEvent = b'\x45\x56\x45\x4E'
        self.SubCmdID = b'\x08' # 버퍼 삭제
        self.Length = b'\x01'
        self.Reserved_Wnd = b'\xFF'
        self.clsBUFMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length + self.Reserved_Wnd
        self.clsBUF = self.FixedStart() + self.clsBUFMSG + self.FixedEnd()
        return self.clsBUF
    
class MSGProtocol:
    # 이벤트 전송 메세지 프로토콜의 고정값
    def __init__ (self):
        self.CmdEvent = b'\x45\x56\x45\x4E' # 7,8,9,10
        self.SubCmdID = b'\x06' # 이벤트 메세지 전송 # 11
        self.InputFixData = b'\x5B\x46\x54\x35\x30\x31\x5D' #31
        self.fixed = Protocol()
        UserInputData = KoreanSTR(input("입력하세요 : "))
        # UserInputData = KoreanSTR("기본문구")
        self.UsersendMSG = UserInputData.encodeing() 
    # 이벤트텍스트전송 고정값1
    def FixedEventText1(self):
        self.Windows_Number = b'\x01' # 13
        self.X_POSITION = b'\x00\x00' # 14, 15
        self.W_WIDTH_PIXELS = b'\x40\x00' # 16, 17
        self.Y_POSITION = b'\x00' # 18
        self.H_HEIGHT_PIXELS = b'\x10' # 19
        self.FixedData1 = self.Windows_Number + self.X_POSITION + self.W_WIDTH_PIXELS + self.Y_POSITION + self.H_HEIGHT_PIXELS
        return self.FixedData1

    # 이벤트텍스트전송 기능변경
    def functionEvent(self, Action = b'\x02', Speed = b'\x00', StaySeconds = b'\x00', LoopTimes = b'\x03'):
        self.Action = Action #20
        self.Speed = Speed #21
        self.StaySeconds = StaySeconds #22
        self.LoopTimes = LoopTimes #23
        self.functionData = self.Action + self.Speed + self.StaySeconds + self.LoopTimes
        return self.functionData
    
    # 이벤트텍스트전송 고정값2
    def FixedEventText2(self,fontColor = b'\x02'):
        self.MemoryPosition = b'\x01' #24
        self.MultiLinesDisp = b'\x00' #25
        self.Align = b'\x00' # 26
        self.FixedData2 = self.MemoryPosition + self.MultiLinesDisp + self.Align
        self.fontColor = fontColor # 가변 데이터 #27
        self.ReservedFontMode = b'\x00' #28
        self.FontAscii = b'\x01\x00' #29
        self.FontAsian = b'\x02\x00' #30 
        self.FixedData3 = self.FixedData2 + self.fontColor + self.ReservedFontMode + self.FontAscii + self.FontAsian
        return self.FixedData3
    
    # Length 구하기
    def LengthFind(self):
        self.sendtext = self.FixedEventText1() + self.functionEvent() + self.FixedEventText2()
        Length = self.sendtext + self.InputFixData + self.UsersendMSG
        num1 = len(Length)                                 # Length 길이
        byte2 = num1.to_bytes(1, byteorder='big')
        self.length = byte2                                 # length를 byte2값으로 구함
        return self.length

    # DataLength 구하기
    def DataLengthFind(self):
        DataLength = self.CmdEvent + self.SubCmdID + self.LengthFind() + self.sendtext + self.InputFixData + self.UsersendMSG
        num2 = len(DataLength)                            # DataLength 길이
        byte1 = num2.to_bytes(2, byteorder='big')                  
        self.datalength = byte1                           # datalength를 byte1값으로 구함
        return self.datalength
    
    # 사용자가 보낼 메세지
    def TotalSendEventText(self):
        self.CmdEvent = b'\x45\x56\x45\x4E' # 7,8,9,10
        self.SubCmdID = b'\x06'             # 이벤트 메세지 전송 # 11  
        self.DataLength = self.DataLengthFind()        # 5,6
        self.Length = self.LengthFind()                  # 12
        self.testData = self.CmdEvent + self.SubCmdID + self.Length 
        self.sendtext = self.FixedEventText1() + self.functionEvent() + self.FixedEventText2()
        self.InputFixData = b'\x5B\x46\x54\x35\x30\x31\x5D' #31  
        return self.fixed.FixedStart() + self.DataLength + self.testData + self.sendtext + self.InputFixData + self.UsersendMSG + self.fixed.FixedEnd()