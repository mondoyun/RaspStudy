import serial
from LEDpacket import Packet 
from LEDpacket import MSGPacket
class LEDdisplay:
    # 시리얼 통신 - 번호, 속도, 타임아웃 "/dev/ttyUSB0"
    def __init__(self, PortNume = "/dev/ttyUSB0", baud = 57600, timeout = 1):
        self.portNume = PortNume
        self.baud = baud
        self.timeout = timeout
        self.serial = serial.Serial(self.portNume, self.baud, timeout = 1)
        self.packet = Packet()
        
    # 전광판 켜고 이벤트메세지 초기화
    def PowerOnMsgInit(self):
        self.packet.InitEventMemory()
        self.packet.PowerOn()
        powerONMsgInit = self.packet.onpacket + self.packet.initEventpacket
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
        self.packet.startWindows()
        self.serial.write(self.packet.printwindowpacket)
        print("LED 전광판 메세지 출력")

    # 전광판 버퍼 삭제 및 종료
    def ClearbufPoweroff(self):
        self.packet.ClearBuffer()
        self.packet.PowerOFF()
        clearbufPoweroff = self.packet.clearBUFpacket + self.packet.offpacket
        self.serial.write(clearbufPoweroff)
        print("LED 전광판 버퍼에 메세지를 삭제 후 종료")

    # 시리얼 포트 닫기
    def Close(self):
        self.serial.close()
        print("serial포트를 닫았습니다.")