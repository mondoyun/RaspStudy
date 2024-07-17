import serial
from LEDserial import Packet 
from LEDserial import MSGPacket
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