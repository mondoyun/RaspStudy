import serial
import time
class KoreanSTR:
    def __init__(self): 
        pass
    
    def KRstring(self):    
        # 사용자가 문자열을 입력하고 인코딩하여 반환하는 메서드
        self.string = input("입력 : ")
        self.InputData = self.string.encode('euc-kr')
        return self.InputData


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
        self.SubCmdID = b'\x02'                             #전원 ON    
        self.onMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length + self.program_id
        self.on = self.FixedStart() + self.onMSG + self.FixedEnd()
        return self.on

    # LED 전광판 전원 OFF
    def PowerOFF(self):
        self.SubCmdID = b'\x03'                             #전원 OFF
        self.offMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length + self.program_id
        self.off = self.FixedStart() + self.offMSG + self.FixedEnd()
        return self.off

    # 이벤트 초기화
    def InitEventMemory(self):
        self.DataLength = b'\x00\x08'
        self.CmdEvent = b'\x45\x56\x45\x4E'
        self.SubCmdID = b'\x01'                             #이벤트 초기화
        self.Length = b'\x02'
        self.program_id = b'\x04\x00'
        self.initMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length + self.program_id
        self.initpacket = self.FixedStart() + self.initMSG + self.FixedEnd()
        return self.initpacket
    
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
        self.DataLength = b'\x00\x07'
        self.CmdEvent = b'\x45\x56\x45\x4E'
        self.SubCmdID = b'\x08'                             #버퍼 삭제
        self.Length = b'\x01'
        self.Reserved_Wnd = b'\xFF'
        self.clsBUFMSG = self.DataLength + self.CmdEvent + self.SubCmdID + self.Length + self.Reserved_Wnd
        self.clsBUFpacket = self.FixedStart() + self.clsBUFMSG + self.FixedEnd()
        return self.clsBUFpacket
    
class MSGPacket:
    # 이벤트 전송 메세지 프로토콜의 고정값
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
        self.InputFixData = b'\x5B\x46\x54\x35\x30\x31\x5D' #31
        self.fixed = Packet()
        self.usersendMSG = KoreanSTR().KRstring()
    # 이벤트텍스트전송 고정값1
    def FixedEventText1(self):
        self.fixedEVNpacket1 = self.Windows_Number + self.X_POSITION + self.W_WIDTH_PIXELS + self.Y_POSITION + self.H_HEIGHT_PIXELS
        return self.fixedEVNpacket1

    # 이벤트텍스트전송 기능변경
    def functionEvent(self, Action = b'\x02', Speed = b'\x00', StaySeconds = b'\x00', LoopTimes = b'\x01'):
        self.Action = Action                                #20
        self.Speed = Speed                                  #21
        self.StaySeconds = StaySeconds                      #22
        self.LoopTimes = LoopTimes                          #23
        self.functions = self.Action + self.Speed + self.StaySeconds + self.LoopTimes
        return self.functions
    
    # 이벤트텍스트전송 고정값2
    def FixedEventText2(self,fontColor = b'\x04'):          
        self.fixedEVNpacket2 = self.MemoryPosition + self.MultiLinesDisp + self.Align
        self.fontColor = fontColor                          #27 #가변 데이터 
        self.fixedEVNpacket3 = self.fixedEVNpacket2 + self.fontColor + self.ReservedFontMode + self.FontAscii + self.FontAsian
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
        self.DataLength = self.DataLengthFind()             # 5,6
        self.CmdEvent = b'\x45\x56\x45\x4E'                 # 7,8,9,10
        self.SubCmdID = b'\x06'                             # 이벤트 메세지 전송 # 11  
        self.Length = self.LengthFind()                     # 12
        self.fixedpacket1 = self.CmdEvent + self.SubCmdID + self.Length 
        self.fixedpacket2 = self.FixedEventText1() + self.functionEvent() + self.FixedEventText2()
        return (self.fixed.FixedStart() + self.DataLength + self.fixedpacket1 + self.fixedpacket2 +
                self.InputFixData + self.usersendMSG + self.fixed.FixedEnd())

class LED:
    # 시리얼 통신 - 번호, 속도, 타임아웃 "/dev/ttyUSB0"
    def __init__(self, PortNume = "/dev/ttyUSB0", baud = 57600, timeout = 1):
        self.portNume = PortNume
        self.baud = baud
        self.timeout = timeout
        self.serial = serial.Serial(self.portNume, self.baud, timeout = 1)
        self.protocol = Packet()
        
    # 전광판 켜고 초기화
    def PowerOnMsgInit(self):
        powerONMsgInit = self.protocol.PowerOn() + self.protocol.InitEventMemory()
        self.serial.write(powerONMsgInit)
        print("LED 전광판 전원ON 및 초기화")
        
    # 메세지 입력    
    def InputMSG(self):
        self.eventMSG = MSGPacket()
        inputMSG = self.eventMSG.SendEventText()
        self.serial.write(inputMSG)
        print("LED 전광판 버퍼에 메세지가 전송됩니다.")

    # 전광판 메세지 출력
    def startdisplay(self):
        display = self.protocol.startWindows()
        self.serial.write(display)
        print("LED 전광판 메세지 출력")

    # 전광판 버퍼 삭제 및 종료
    def ClearbufPoweroff(self):
        clearbufPoweroff = self.protocol.ClearBuffer() + self.protocol.PowerOFF()
        self.serial.write(clearbufPoweroff)
        print("LED 전광판 버퍼에 메세지를 삭제 후 종료")

    # 시리얼 포트 닫기
    def Close(self):
        self.serial.close()
        print("serial포트를 닫았습니다.")

if __name__ == "__main__":

    Led = LED("/dev/ttyUSB0", 57600, 1) # LED 전광판 객체 생성

    Led.PowerOnMsgInit()                # 전광판 켜기
    time.sleep(1)                       # 1초 대기

    while(1):
        Led.InputMSG()                  # 메세지 입력
        time.sleep(3)                   # 3초 대기   
 
        Led.startdisplay()              # 메세지 출력
        time.sleep(3)                   # 3초 대기 

        user_input = input("종료 명령('q'누르면 종료) : ")
        if user_input == 'q':
            print("프로그램을 종료합니다")
            break
        else:
            print("잘못입력하셨습니다. 다시눌러주세요.")

    Led.ClearbufPoweroff()              # 버퍼 삭제 및 종료
    time.sleep(1)                       # 1초 대기

    Led.Close()                         # 시리얼 포트 닫기