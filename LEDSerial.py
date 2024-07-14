import serial
from LEDPacket import Protocol 
from LEDPacket import MSGProtocol

class LED:
    # 시리얼 통신 - 번호, 속도, 타임아웃 "/dev/ttyUSB0"
    def __init__(self, PortNum = "COM3", baud = 57600, timeout = 1):
        self.portNume = PortNum
        self.baud = baud
        self.timeout = timeout
        self.serial = serial.Serial(self.portNume, self.baud, timeout = 1)
        self.protocol = Protocol()
        self.EVNMSG = MSGProtocol()
    # 전광판 켜기
    def PowerON(self):
        LEDstat = self.protocol.PowerOn()
        self.serial.write(LEDstat)
        print("LED 전광판 전원을 켰습니다.")

    # 전광판 메세지 초기화
    def MsgInit(self):
        LEDinit = self.protocol.InitEventMemory()
        self.serial.write(LEDinit)
        print("LED 전광판을 초기화했습니다.")

    # 전광판 메세지 전송(버퍼)
    def sendMsgEvent(self):
        LEDsendMsgEvent = self.EVNMSG.TotalSendEventText()
        self.serial.write(LEDsendMsgEvent)
        print("LED 전광판 버퍼에 메세지를 보냈습니다.")

    # 전광판 메세지 화면출력
    def startMsgWindow(self):
        LEDstartWindow = self.protocol.startWindows()
        self.serial.write(LEDstartWindow)
        print("LED 전광판에 메세지를 출력합니다.")   

    # 전광판 버퍼 삭제
    def ClsBUF(self):
        LEDclsBUF = self.protocol.ClearBuffer()
        self.serial.write(LEDclsBUF)
        print("LED 전광판 버퍼에 메세지를 삭제했습니다.")

    # 전광판 끄기
    def PowerOFF(self):
        ledOff = self.protocol.PowerOFF()
        self.serial.write(ledOff)
        print("LED 전광판 전원을 껐습니다.")

    # 시리얼 포트 닫기
    def close(self):
        self.serial.close()
        print("serial포트를 닫았습니다.")