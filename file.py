# LED 객체의 기능,속성
# 기능 : 전원 on,off / 이벤트초기화 / 메세지 전송 / 화면 출력 
# 속성 : serial통신 포트번호, 속도, timeout
# packet 통신 구조 - Header, screen ID, crc, eof
# Data_length, Cmd_event, Sub_Cmd_ID, length 
# Windows_Number
# X_POSITION 
# W_WIDTH_PIXELS 
# Y_POSITION 
# H_HEIGHT_PIXELS 
# Action 
# Speed 
# Stay_Seconds 
# Loop_Times 
# Memory_Position 
# Multi_Lines_Disp 
# Align 
# font_Color 
# Reserved_Font_Mode 
# font_ascii 
# font_asian 
# Data 

import serial
import time

class Protocol:
    # 시리얼 통신 - 번호, 속도, 타임아웃
    def __init__(self, PortNum = "/dev/ttyUSB0", baud = 57600, timeout = 1):
        self.portNume = PortNum
        self.baud = baud
        self.timeout = timeout
        self.serial = serial.Serial(self.portNume, self.baud, timeout = 1)
        
    # 패킷통신 - 시작고정값,고정구조
    def FixedStart(self, HeaderFrame = b'\x7E\x01',ScreenID = b'\xFE\xFE'):
        self.HeaderFrame = HeaderFrame 
        self.ScreenID = ScreenID
        self.startFixed = HeaderFrame + ScreenID
        return self.startFixed

    # 패킷통신 - 끝고정값
    def FixedEnd(self, crc = b'\xFF\xFF', eof = b'\x7E\x00'):
        self.crc = crc
        self.eof = eof
        self.endFixed = crc + eof
        return self.endFixed
    
    # 가변데이터 - DataLength, CmdEvent, SubCmdID, Length 
    def FixedPacket(self,DataLength, CmdEvent, SubCmdID, Length):

        self.DataLength = DataLength
        self.CmdEvent = CmdEvent
        self.SubCmdID = SubCmdID
        self.Length = Length
        self.FixData = DataLength + CmdEvent + SubCmdID + Length
        return self.FixData
    
    # LED 전광판 전원 ON
    def PowerOn(self):
        self.DataLength= b'\x00\x0B'
        self.CmdEvent = b'\x50\x57\x4F\x4E'
        self.SubCmdID = b'\x02' # 전원 ON
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
    
    # 이벤트텍스트전송 - sendEventText
    # clear buffer

    # 화면 출력
    def startWindows(self):
        self.DataLength = b'\x00\x08'
        self.CmdEvent = b'\x45\x56\x45\x4E'
        self.SubCmdID = b'\x07' # 화면 출력
        self.Length = b'\x02'
        self.Reserved_Wnd = b'\xFF'
        self.Reserved = b'\x00'
        self.startwindow = self.startFixed + self.FixData + self.Reserved_Wnd + self.Reserved + self.endFixed
        return self.startwindow

if __name__ == "__main__":
    # LED 전광판 객체 생성 
    Protocol.PowerOn  
    time.sleep(2)
    Protocol.PowerOFF 
    #LED = Protocol()

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




    
    
    

