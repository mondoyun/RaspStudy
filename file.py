# LED 객체의 기능
# 기능 : 메세지 전송 

# Windows_Number
# X_POSITION 
# W_WIDTH_PIXELS 
# Y_POSITION 
# H_HEIGHT_PIXELS 
# Action -
# Speed -
# Stay_Seconds -
# Loop_Times -
# Memory_Position 
# Multi_Lines_Disp 
# Align 
# font_Color -
# Reserved_Font_Mode 
# font_ascii 
# font_asian 
# Data -

import serial
import time

class Protocol:
    # 패킷통신 - 시작고정값,고정구조
    def FixedStart(self, HeaderFrame, ScreenID):
        self.HeaderFrame = b'\x7E\x01' 
        self.ScreenID = b'\xFE\xFE'
        self.startFixed = HeaderFrame + ScreenID
        self.FixedStart()
        return self.startFixed

    # 패킷통신 - 끝고정값,고정구조
    def FixedEnd(self, crc, eof):
        self.crc = b'\xFF\xFF'
        self.eof = b'\x7E\x00'
        self.endFixed = crc + eof
        return self.endFixed
    
    # 패킷통신 - 고정구조,가변데이터 : DataLength, CmdEvent, SubCmdID, Length 
    def FixedPacket(self,DataLength = b'\x00\x0B', CmdEvent = b'\x50\x57\x4F\x4E', SubCmdID = b'\x00', Length = b'\x00'):

        self.DataLength = DataLength
        self.CmdEvent = CmdEvent
        self.SubCmdID = SubCmdID
        self.Length = Length
        self.FixData = DataLength + CmdEvent + SubCmdID + Length
        return self.FixData
    
    # LED 전광판 전원 ON
    def PowerOn(self,SubCmdID = b'\x02'):
        self.DataLength = b'\x00\x0B'
        self.CmdEvent = b'\x50\x57\x4F\x4E'
        self.SubCmdID = SubCmdID # 전원 ON
        self.Length = b'\x00'
        self.program_id = b'\x00\x00\x00\x00\x00'
        self.On = self.startFixed + self.FixData + self.program_id + self.endFixed
        return self.On

    # LED 전광판 전원 OFF
    def PowerOFF(self):
        self.DataLength= b'\x00\x0B'
        self.CmdEvent = b'\x50\x57\x4F\x4E'
        self.SubCmdID = b'\x03' # 전원 OFF
        self.Length = b'\x00'
        self.program_id = b'\x00\x00\x00\x00\x00'
        self.OFF = self.startFixed + self.FixData + self.program_id + self.endFixed
        return self.OFF

    # 이벤트 초기화
    def InitEventMemory(self):
        
        self.DataLength = b'\x00\x08'
        self.CmdEvent = b'\x45\x56\x45\x4E'
        self.SubCmdID = b'\x01' # 이벤트 초기화
        self.Length = b'\x02'
        self.program_id = b'\x04\x00'
        self.initMemory = self.startFixed + self.FixData + self.program_id + self.endFixed
        return self.initMemory
    
    # 이벤트텍스트전송 고정값1
    def FixedEventText1(self, Windows_Number, X_POSITION, W_WIDTH_PIXELS,Y_POSITION, H_HEIGHT_PIXELS):
        self.Windows_Number = Windows_Number
        self.X_POSITION = X_POSITION
        self.W_WIDTH_PIXELS = W_WIDTH_PIXELS
        self.Y_POSITION = Y_POSITION
        self.H_HEIGHT_PIXELS = H_HEIGHT_PIXELS
        self.DataFixed = Windows_Number + X_POSITION + W_WIDTH_PIXELS + Y_POSITION + H_HEIGHT_PIXELS
    # 이벤트텍스트전송 가변값
    def sendEventText(self, Action, Speed, StaySeconds, LoopTimes, fontColor, Data):
        #self.data = b'\x7E\x01\xFE\xFE\x00\x2B\x45\x56\x45\x4E\x06\x25\x01\x00\x00\x40\x00\x00\x10\x02\x00\x00\x01\x01\x00\x00\x02\x00\x01\x00\x02\x00\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4\xFF\xFF\x7E\x00'
        self.Action = Action
        self.Speed = Speed
        self.StaySeconds = StaySeconds
        self.LoopTimes = LoopTimes
        self.fontColor = fontColor
        self.Data = Data
    
    # 이벤트텍스트전송 고정값2
    def FixedEventText2(self, MemoryPosition, MultiLinesDisp, Align, ReservedFontMode, FontAscii, FontAsian):
        self.MemoryPosition = MemoryPosition
        self.MultiLinesDisp = MultiLinesDisp 
        self.Align = Align
        self.ReservedFontMode = ReservedFontMode
        self.FontAscii = FontAscii
        self.FontAsian = FontAsian

    # 버퍼 삭제
    def ClearBuffer(self):
        self.DataLength = b'\x00\x07'
        self.CmdEvent = b'\x45\x56\x45\x4E'
        self.SubCmdID = b'\x08' # 버퍼 삭제
        self.Length = b'\x01'
        self.Reserved_Wnd = b'\xFF'
        self.clsBUF = self.startFixed + self.FixData + self.Reserved_Wnd + self.endFixed
        return self.clsBUF
    
    # 화면출력
    def startWindows(self):
        self.DataLength = b'\x00\x08'
        self.CmdEvent = b'\x45\x56\x45\x4E'
        self.SubCmdID = b'\x07' # 화면 출력
        self.Length = b'\x02'
        self.Reserved_Wnd = b'\xFF'
        self.Reserved = b'\x00'
        self.startwindow = self.startFixed + self.FixData + self.Reserved_Wnd + self.Reserved + self.endFixed
        return self.startwindow

class LED:
    # 시리얼 통신 - 번호, 속도, 타임아웃
    def __init__(self, PortNum = "/dev/ttyUSB0", baud = 57600, timeout = 1):
        self.portNume = PortNum
        self.baud = baud
        self.timeout = timeout
        self.serial = serial.Serial(self.portNume, self.baud, timeout = 1)
    
    # 전광판 켜기
    def open(self):
        self.serial.write(Protocol.PowerOn(self))
        print("LED 전광판 전원을 켰습니다.")

    # 전광판 메세지 초기화
    def MsgInit(self):
        self.serial.write(Protocol.InitEventMemory)
        print("LED 전광판을 초기화했습니다.")

    # 전광판 메세지 전송(버퍼)
    def sendMsgEvent(self):
        self.serial.write(Protocol.sendEventText)
        print("LED 전광판 버퍼에 메세지를 보냈습니다.")
    
    # 전광판 메세지 화면출력
    def startMsgWindow(self):
        self.serial.write(Protocol.startWindows)
        print("LED 전광판에 메세지를 출력합니다.")

    # 전광판 끄기
    def close(self):
        self.serial.close()
        print("LED 전광판 전원을 껐습니다.")


if __name__ == "__main__":

    # LED 전광판 객체 생성
    Led = LED()

    Led.open()  # 전광판 켜기
    time.sleep(2) # 2초 대기

    Led.MsgInit()
    time.sleep(2) # 2초 대기

    Led.sendMsgEvent()
    time.sleep(2) # 2초 대기

    Led.startMsgWindow()
    time.sleep(2) # 2초 대기

    # LED 전원 끄기
    Led.close()

    # 시리얼 포트 닫기

    # LED 전원 켜기
    #LED.PowerOn()
    #time.sleep(1) # 1초 대기

    # 메세지 초기화
    #LED.message_init()
    #time.sleep(1) # 1초 대기

    # 메세지 보내는 명령 전송
    #LED.send_message()
    #time.sleep(1) # 1초 대기

    # 메세지 출력
    #LED.message_display()
    #print("LED 전광판에 메세지를 출력합니다.")
    #time.sleep(2) # 2초 대기

    # LED 전원 끄기
    #LED.PowerOFF()

    # 시리얼 포트 닫기




    
    
    

