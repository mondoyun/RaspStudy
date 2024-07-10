<<<<<<< HEAD
# # LED 객체의 기능
# # 기능 : 메세지 전송 

# # Windows_Number -15
# # X_POSITION - 16
# # W_WIDTH_PIXELS - 17
# # Y_POSITION - 18
# # H_HEIGHT_PIXELS - 19
# # Action - 20
# # Speed - 21
# # Stay_Seconds -
# # Loop_Times -
# # Memory_Position 
# # Multi_Lines_Disp 
# # Align 
# # font_Color -
# # Reserved_Font_Mode 
# # font_ascii 
# # font_asian 
# # Data -

# import serial
# import time

# class Protocol:

#     def __init__ (self):
#         self.HeaderFrame = b'\x7E\x01'
#         self.ScreenID = b'\xFE\xFE'
#         self.crc = b'\xFF\xFF'
#         self.eof = b'\x7E\x00'

#     # 패킷통신 - 시작고정값,고정구조
#     def FixedStart(self):
#         return self.HeaderFrame + self.ScreenID
    
#     # 패킷통신 - 끝고정값,고정구조
#     def FixedEnd(self):
#         return self.crc + self.eof
    
#     # LED 전광판 전원 ON
#     def PowerOn(self):
#         self.DataLength = b'\x00\x0B'
#         self.CmdEvent = b'\x50\x57\x4F\x4E'
#         self.SubCmdID = b'\x02' # 전원 ON
#         self.len = b'\x00'
#         self.program_id = b'\x00\x00\x00\x00\x00'
#         self.OnMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.len + self.program_id
#         self.on = self.FixedStart() + self.OnMSG + self.FixedEnd()
#         return self.on

#     # LED 전광판 전원 OFF
#     def PowerOFF(self):
#         self.DataLength= b'\x00\x0B'
#         self.CmdEvent = b'\x50\x57\x4F\x4E'
#         self.SubCmdID = b'\x03' # 전원 OFF
#         self.Length = b'\x00'
#         self.program_id = b'\x00\x00\x00\x00\x00'
#         self.OffMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.len + self.program_id
#         self.OFF = self.FixedStart() + self.OffMSG + self.FixedEnd()
#         return self.OFF

#     # 이벤트 초기화
#     def InitEventMemory(self):
#         self.DataLength = b'\x00\x08'
#         self.CmdEvent = b'\x45\x56\x45\x4E'
#         self.SubCmdID = b'\x01' # 이벤트 초기화
#         self.Length = b'\x02'
#         self.program_id = b'\x04\x00'
#         self.initMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length + self.program_id
#         self.initMemory = self.FixedStart() + self.initMSG + self.FixedEnd()
#         return self.initMemory
    
#     # 이벤트텍스트전송 고정값1
#     def FixedEventText1(self):
#         self.Windows_Number = b'\x01' # 13
#         self.X_POSITION = b'\x00\x00' # 14, 15
#         self.W_WIDTH_PIXELS = b'\x40\x00' # 16, 17
#         self.Y_POSITION = b'\x00' # 18
#         self.H_HEIGHT_PIXELS = b'\x10' # 19
#         self.DataFixed = self.Windows_Number + self.X_POSITION + self.W_WIDTH_PIXELS + self.Y_POSITION + self.H_HEIGHT_PIXELS
#         return self.DataFixed
#     #31부터 b'\x02\x00\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4'
#     #5부터 b'\x00\x2B\x45\x56\x45\x4E\x06\x25\x01\x00\x00\x40\x00\x00\x10\x02\x00\x00\x03\x01\x00\x00\x01\x00\x01\x00\x02\x00\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4'

#     # 이벤트텍스트전송 기능변경
#     def sendEventText(self, Action = b'\x02', Speed = b'\x00', StaySeconds = b'\x00', LoopTimes = b'\x03'):
#         self.Action = Action #20
#         self.Speed = Speed #21
#         self.StaySeconds = StaySeconds #22
#         self.LoopTimes = LoopTimes #23
#         self.testData2 = self.Action + self.Speed + self.StaySeconds + self.LoopTimes
#         return self.testData2
    
#     # 이벤트텍스트전송 고정값2
#     def FixedEventText2(self,fontColor = b'\x01'):
#         self.MemoryPosition = b'\x01' #24
#         self.MultiLinesDisp = b'\x00' #25
#         self.Align = b'\x00' # 26
#         self.testData3 = self.MemoryPosition + self.MultiLinesDisp + self.Align
#         self.fontColor = fontColor # 가변 데이터 #27
#         self.ReservedFontMode = b'\x00' #28
#         self.FontAscii = b'\x01' #29
#         self.FontAsian = b'\x00' #30 
#         self.testData4 = self.testData3 + self.fontColor + self.ReservedFontMode + self.FontAscii + self.FontAsian
#         return self.testData4
    
#     # 최종 보낼 메세지
#     def TotalSendEventText(self, DataLength = b'\x00\x2B', Length = b'\x25', Data = b'\x02\x00\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4'):
#         self.DataLength = DataLength # 가변 데이터 # 5,6
#         self.CmdEvent = b'\x45\x56\x45\x4E' # 7,8,9,10
#         self.SubCmdID = b'\x06' # 이벤트 메세지 전송 # 11
#         self.Length = Length # 가변 데이터 # 12
#         self.testData = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length 
#         self.sendTexts = self.FixedEventText1() + self.sendEventText() + self.FixedEventText2()
#         self.Data = Data # 가변 데이터 #31        
#         return self.FixedStart() + self.testData + self.sendTexts + self.Data + self.FixedEnd()
    
#     # 화면출력
#     def startWindows(self):
#         self.DataLength = b'\x00\x08'
#         self.CmdEvent = b'\x45\x56\x45\x4E'
#         self.SubCmdID = b'\x07' # 화면 출력
#         self.Length = b'\x02'
#         self.Reserved_Wnd = b'\xFF'
#         self.Reserved = b'\x00'
#         self.windowMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length + self.Reserved_Wnd + self.Reserved
#         self.startwindow = self.FixedStart() + self.windowMSG + self.FixedEnd()
#         return self.startwindow
    
#     # 버퍼 삭제
#     def ClearBuffer(self):
#         self.DataLength = b'\x00\x07'
#         self.CmdEvent = b'\x45\x56\x45\x4E'
#         self.SubCmdID = b'\x08' # 버퍼 삭제
#         self.Length = b'\x01'
#         self.Reserved_Wnd = b'\xFF'
#         self.clsBUFMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length + self.Reserved_Wnd
#         self.clsBUF = self.FixedStart() + self.clsBUFMSG + self.FixedEnd()
#         return self.clsBUF

# class LED:
#     # 시리얼 통신 - 번호, 속도, 타임아웃
#     def __init__(self, PortNum = "/dev/ttyUSB0", baud = 57600, timeout = 1):
#         self.portNume = PortNum
#         self.baud = baud
#         self.timeout = timeout
#         self.serial = serial.Serial(self.portNume, self.baud, timeout = 1)
#         self.protocol = Protocol()

#     # 전광판 켜기
#     def PowerON(self):
#         LEDstat = self.protocol.PowerOn()
#         self.serial.write(LEDstat)
#         print("LED 전광판 전원을 켰습니다.")

#     # 전광판 메세지 초기화
#     def MsgInit(self):
#         LEDinit = self.protocol.InitEventMemory()
#         self.serial.write(LEDinit)
#         temp = self.serial.read(20) # 데이터 전송 테스트
#         print(temp)
#         print("LED 전광판을 초기화했습니다.")

#     # 전광판 메세지 전송(버퍼)
#     def sendMsgEvent(self):
#         LEDsendMsgEvent = self.protocol.TotalSendEventText()
#         self.serial.write(LEDsendMsgEvent)
#         temp = self.serial.read(20) # 데이터 전송 테스트
#         print(temp)
#         print("LED 전광판 버퍼에 메세지를 보냈습니다.")

#     # 전광판 메세지 화면출력
#     def startMsgWindow(self):
#         LEDstartWindow = self.protocol.startWindows()
#         self.serial.write(LEDstartWindow)
#         temp = self.serial.read(20) # 데이터 전송 테스트
#         print(temp)
#         print("LED 전광판에 메세지를 출력합니다.")   

#     # 전광판 버퍼 삭제
#     def ClsBUF(self):
#         LEDclsBUF = self.protocol.ClearBuffer()
#         self.serial.write(LEDclsBUF)
#         temp = self.serial.read(20) # 데이터 전송 테스트
#         print(temp)
#         print("LED 전광판 버퍼에 메세지를 삭제했습니다.")

#     # 전광판 끄기
#     def PowerOFF(self):
#         ledOff = self.protocol.PowerOFF()
#         self.serial.write(ledOff)
#         temp = self.serial.read(20) # 데이터 전송 테스트
#         print(temp)
#         print("LED 전광판 전원을 껐습니다.")

#     # 시리얼 포트 닫기
#     def close(self):
#         self.serial.close()
#         print("serial포트를 닫았습니다.")


# if __name__ == "__main__":

#     Led = LED() # LED 전광판 객체 생성

#     Led.PowerON() # 전광판 켜기
#     time.sleep(2) # 2초 대기

#     Led.MsgInit() # 메세지 초기화
#     time.sleep(2) # 2초 대기

#     Led.sendMsgEvent() #메세지 버퍼에 전송
#     time.sleep(2) # 2초 대기

#     Led.startMsgWindow() # 메세지 출력
#     time.sleep(2) # 2초 대기

#     Led.ClsBUF() # 버퍼 삭제
#     time.sleep(2) # 2초 대기

#     Led.PowerOFF() # LED 전원 끄기
#     time.sleep(2) # 2초 대기

#     Led.close() # 시리얼 포트 닫기
=======
>>>>>>> 6092cdeca1a422f3ddfaf1b95f2dcfdd2881bbca
# LED 객체의 기능
# 기능 : 메세지 전송 

# Windows_Number -15
# X_POSITION - 16
# W_WIDTH_PIXELS - 17
# Y_POSITION - 18
# H_HEIGHT_PIXELS - 19
# Action - 20
# Speed - 21
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

    def __init__ (self):
        self.HeaderFrame = b'\x7E\x01'
        self.ScreenID = b'\xFE\xFE'
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
        self.DataLength = b'\x00\x0B'
        self.CmdEvent = b'\x50\x57\x4F\x4E'
        self.SubCmdID = b'\x02' # 전원 ON
        self.len = b'\x00'
        self.program_id = b'\x00\x00\x00\x00\x00'
        self.OnMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.len + self.program_id
        self.on = self.FixedStart() + self.OnMSG + self.FixedEnd()
        return self.on

    # LED 전광판 전원 OFF
    def PowerOFF(self):
        self.DataLength= b'\x00\x0B'
        self.CmdEvent = b'\x50\x57\x4F\x4E'
        self.SubCmdID = b'\x03' # 전원 OFF
        self.Length = b'\x00'
        self.program_id = b'\x00\x00\x00\x00\x00'
        self.OffMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.len + self.program_id
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
    
    # 이벤트텍스트전송 고정값1
    def FixedEventText1(self):
        self.Windows_Number = b'\x01' # 13
        self.X_POSITION = b'\x00\x00' # 14, 15
        self.W_WIDTH_PIXELS = b'\x40\x00' # 16, 17
        self.Y_POSITION = b'\x00' # 18
        self.H_HEIGHT_PIXELS = b'\x10' # 19
        self.DataFixed = self.Windows_Number + self.X_POSITION + self.W_WIDTH_PIXELS + self.Y_POSITION + self.H_HEIGHT_PIXELS
        return self.DataFixed
    #31부터 b'\x02\x00\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4'
    #5부터 b'\x00\x2B\x45\x56\x45\x4E\x06\x25\x01\x00\x00\x40\x00\x00\x10\x02\x00\x00\x03\x01\x00\x00\x01\x00\x01\x00\x02\x00\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4'

    # 이벤트텍스트전송 기능변경
    def sendEventText(self, Action = b'\x02', Speed = b'\x00', StaySeconds = b'\x00', LoopTimes = b'\x03'):
        self.Action = Action #20
        self.Speed = Speed #21
        self.StaySeconds = StaySeconds #22
        self.LoopTimes = LoopTimes #23
        self.testData2 = self.Action + self.Speed + self.StaySeconds + self.LoopTimes
        return self.testData2
    
    # 이벤트텍스트전송 고정값2
    def FixedEventText2(self,fontColor = b'\x01'):
        self.MemoryPosition = b'\x01' #24
        self.MultiLinesDisp = b'\x00' #25
        self.Align = b'\x00' # 26
        self.testData3 = self.MemoryPosition + self.MultiLinesDisp + self.Align
        self.fontColor = fontColor # 가변 데이터 #27
        self.ReservedFontMode = b'\x00' #28
        self.FontAscii = b'\x01' #29
        self.FontAsian = b'\x00' #30 
        self.testData4 = self.testData3 + self.fontColor + self.ReservedFontMode + self.FontAscii + self.FontAsian
        return self.testData4
    
    # 최종 보낼 메세지
    def TotalSendEventText(self, DataLength = b'\x00\x2B', Length = b'\x25', Data = b'\x02\x00\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4'):
<<<<<<< HEAD
        b'\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4'
        self.DataLength = bytes([self.CmdEvent + self.SubCmdID + self.Length + self.sendTexts + self.Data]) # 가변 데이터 # 5,6
        self.CmdEvent = b'\x45\x56\x45\x4E' # 7,8,9,10
        self.SubCmdID = b'\x06' # 이벤트 메세지 전송 # 11
        self.Length = bytes([self.sendTexts + self.Data]) # 가변 데이터 # 12
        self.testData = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length 
        self.sendTexts = self.FixedEventText1() + self.sendEventText() + self.FixedEventText2()
        self.Data = Data # 가변 데이터 #31        
        return self.FixedStart() + self.DataLength + self.CmdEvent + self.SubCmdID + self.Length + self.sendTexts + self.Data + self.FixedEnd()
=======
        self.DataLength = DataLength # 가변 데이터 # 5,6
        self.CmdEvent = b'\x45\x56\x45\x4E' # 7,8,9,10
        self.SubCmdID = b'\x06' # 이벤트 메세지 전송 # 11
        self.Length = Length # 가변 데이터 # 12
        self.testData = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length 
        self.sendTexts = self.FixedEventText1() + self.sendEventText() + self.FixedEventText2()
        self.Data = Data # 가변 데이터 #31        
        return self.FixedStart() + self.testData + self.sendTexts + self.Data + self.FixedEnd()
>>>>>>> 6092cdeca1a422f3ddfaf1b95f2dcfdd2881bbca
    
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

class LED:
    # 시리얼 통신 - 번호, 속도, 타임아웃
    def __init__(self, PortNum = "/dev/ttyUSB0", baud = 57600, timeout = 1):
        self.portNume = PortNum
        self.baud = baud
        self.timeout = timeout
        self.serial = serial.Serial(self.portNume, self.baud, timeout = 1)
        self.protocol = Protocol()

    # 전광판 켜기
    def PowerON(self):
        LEDstat = self.protocol.PowerOn()
        self.serial.write(LEDstat)
        print("LED 전광판 전원을 켰습니다.")

    # 전광판 메세지 초기화
    def MsgInit(self):
        LEDinit = self.protocol.InitEventMemory()
        self.serial.write(LEDinit)
        temp = self.serial.read(20) # 데이터 전송 테스트
        print(temp)
        print("LED 전광판을 초기화했습니다.")

    # 전광판 메세지 전송(버퍼)
    def sendMsgEvent(self):
        LEDsendMsgEvent = self.protocol.TotalSendEventText()
        self.serial.write(LEDsendMsgEvent)
        temp = self.serial.read(20) # 데이터 전송 테스트
        print(temp)
        print("LED 전광판 버퍼에 메세지를 보냈습니다.")

    # 전광판 메세지 화면출력
    def startMsgWindow(self):
        LEDstartWindow = self.protocol.startWindows()
        self.serial.write(LEDstartWindow)
        temp = self.serial.read(20) # 데이터 전송 테스트
        print(temp)
        print("LED 전광판에 메세지를 출력합니다.")   

    # 전광판 버퍼 삭제
    def ClsBUF(self):
        LEDclsBUF = self.protocol.ClearBuffer()
        self.serial.write(LEDclsBUF)
        temp = self.serial.read(20) # 데이터 전송 테스트
        print(temp)
        print("LED 전광판 버퍼에 메세지를 삭제했습니다.")

    # 전광판 끄기
    def PowerOFF(self):
        ledOff = self.protocol.PowerOFF()
        self.serial.write(ledOff)
        temp = self.serial.read(20) # 데이터 전송 테스트
        print(temp)
        print("LED 전광판 전원을 껐습니다.")

    # 시리얼 포트 닫기
    def close(self):
        self.serial.close()
        print("serial포트를 닫았습니다.")


if __name__ == "__main__":

    Led = LED() # LED 전광판 객체 생성

    Led.PowerON() # 전광판 켜기
    time.sleep(2) # 2초 대기

    Led.MsgInit() # 메세지 초기화
    time.sleep(2) # 2초 대기

    Led.sendMsgEvent() #메세지 버퍼에 전송
    time.sleep(2) # 2초 대기

    Led.startMsgWindow() # 메세지 출력
    time.sleep(2) # 2초 대기

    Led.ClsBUF() # 버퍼 삭제
    time.sleep(2) # 2초 대기

    Led.PowerOFF() # LED 전원 끄기
    time.sleep(2) # 2초 대기

    Led.close() # 시리얼 포트 닫기




    
    
    

<<<<<<< HEAD





    
    
    

=======
>>>>>>> 6092cdeca1a422f3ddfaf1b95f2dcfdd2881bbca
