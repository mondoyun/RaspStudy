from LEDinputData import KoreanStringEncoder

class Packet:
    def __init__ (self):
        self.HeaderFrame = b'\x7E\x01'
        self.ScreenID = b'\xFE\xFE'
        self.DataLength = b'\x00\x0B'
        self.CmdEvent = b'\x50\x57\x4F\x4E'
        self.SubCmdID = b'\x02'
        self.Length = b'\x00'
        self.program_id = b'\x00\x00\x00\x00\x00'
        self.crc = b'\xFF\xFF' 
        self.eof = b'\x7E\x00'

    # 패킷통신 - 시작고정값,고정구조
    def FixedStart(self):
        return self.HeaderFrame + self.ScreenID
    
    # 패킷통신 - 끝고정값,고정구조
    def FixedEnd(self):
        return self.crc + self.eof
    
    # LED 전광판 전원 ON
    def PowerOn(self):
        SubCmdID = b'\x02'                             #전원 ON    
        onMSG = self.DataLength + self.CmdEvent + SubCmdID + self.Length + self.program_id
        self.onpacket = self.FixedStart() + onMSG + self.FixedEnd()
        return self.onpacket

    # LED 전광판 전원 OFF
    def PowerOFF(self):
        SubCmdID = b'\x03'                             #전원 OFF
        offMSG = self.DataLength + self.CmdEvent + SubCmdID + self.Length + self.program_id
        self.offpacket = self.FixedStart() + offMSG + self.FixedEnd()
        return self.offpacket

    # 이벤트 초기화
    def InitEventMemory(self):
        DataLength = b'\x00\x08'
        CmdEvent = b'\x45\x56\x45\x4E'
        SubCmdID = b'\x01'                             #이벤트 초기화
        Length = b'\x02'
        program_id = b'\x04\x00'
        initMSG = DataLength + CmdEvent + SubCmdID + Length + program_id
        self.initEventpacket = self.FixedStart() + initMSG + self.FixedEnd()
        return self.initEventpacket
    
    # 화면출력
    def startWindows(self):
        self.DataLength = b'\x00\x08'
        self.CmdEvent = b'\x45\x56\x45\x4E'
        self.SubCmdID = b'\x07'                             #화면 출력
        self.Length = b'\x02'
        self.Reserved_Wnd = b'\xFF'
        self.Reserved = b'\x00'
        self.windowMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length + self.Reserved_Wnd + self.Reserved
        self.printwindowpacket = self.FixedStart() + self.windowMSG + self.FixedEnd()
        return self.printwindowpacket
    
    # 버퍼 삭제
    def ClearBuffer(self):
        DataLength = b'\x00\x07'
        CmdEvent = b'\x45\x56\x45\x4E'
        SubCmdID = b'\x08'                             #버퍼 삭제
        Length = b'\x01'
        Reserved_Wnd = b'\xFF'
        clearBUFMSG = DataLength + CmdEvent + SubCmdID + Length + Reserved_Wnd
        self.clearBUFpacket = self.FixedStart() + clearBUFMSG + self.FixedEnd()
        return self.clearBUFpacket
    
class MSGPacket:
    # 이벤트 전송 메세지 패킷의 고정값
    def __init__ (self):
        self.CmdEvent = b'\x45\x56\x45\x4E'                 #7,8,9,10
        self.SubCmdID = b'\x06'                             #11 #이벤트 메세지 전송 
        self.Windows_Number = b'\x01'                       #13
        self.X_POSITION = b'\x00\x00'                       #14, 15
        self.W_WIDTH_PIXELS = b'\x40\x00'                   #16, 17
        self.Y_POSITION = b'\x00'                           #18
        self.H_HEIGHT_PIXELS = b'\x10'                      #19
        self.MemoryPosition = b'\x01'                       #24
        self.MultiLinesDisp = b'\x00'                       #25
        self.Align = b'\x00'                                #26
        self.ReservedFontMode = b'\x00'                     #28
        self.FontAscii = b'\x01\x00'                        #29
        self.FontAsian = b'\x02\x00'                        #30 
        self.InputKRstring = b'\x5B\x46\x54\x35\x30\x31\x5D' #31 [FT501]
        self.fixed = Packet()
        self.usersendMSG = KoreanStringEncoder().KRstring()
        
    # 이벤트텍스트전송 고정값1
    def FixedEventText1(self):
        self.fixedEVNpacket1 = self.Windows_Number + self.X_POSITION + self.W_WIDTH_PIXELS + self.Y_POSITION + self.H_HEIGHT_PIXELS
        return self.fixedEVNpacket1

    # 이벤트텍스트전송 기능변경
    def functionEvent(self, Action = b'\x02', Speed = b'\x00', StaySeconds = b'\x00', LoopTimes = b'\x02'):
        self.functions = Action + Speed + StaySeconds + LoopTimes
        return self.functions
    
    # 이벤트텍스트전송 고정값2
    def FixedEventText2(self,fontColor = b'\x04'):          
        fixedEVNpacket2 = self.MemoryPosition + self.MultiLinesDisp + self.Align
        self.fixedEVNpacket3 = fixedEVNpacket2 + fontColor + self.ReservedFontMode + self.FontAscii + self.FontAsian
        return self.fixedEVNpacket3
    
    # Length 구하기
    def LengthFind(self):
        num1 = 27 + len(self.usersendMSG)                   # Length 길이
        byte2 = num1.to_bytes(1, byteorder='big')
        self.length = byte2                                 # length를 byte2값으로 구함
        return self.length

    # DataLength 구하기
    def DataLengthFind(self):
        num2 = 32 + len(self.LengthFind()) + len(self.usersendMSG)  # DataLength 길이
        byte1 = num2.to_bytes(2, byteorder='big')                  
        self.datalength = byte1                                     # datalength를 byte1값으로 구함
        return self.datalength
    
    # 사용자가 보낼 메세지
    def SendEventText(self):
        DataLength = self.DataLengthFind()             # 5,6
        CmdEvent = b'\x45\x56\x45\x4E'                 # 7,8,9,10
        SubCmdID = b'\x06'                             # 이벤트 메세지 전송 # 11  
        Length = self.LengthFind()                     # 12
        fixedpacket1 = DataLength + CmdEvent + SubCmdID + Length 
        msgfixedpacket2 = self.FixedEventText1() + self.functionEvent() + self.FixedEventText2()
        return (self.fixed.FixedStart() + fixedpacket1 + msgfixedpacket2 +
                self.InputKRstring + self.usersendMSG + self.fixed.FixedEnd())