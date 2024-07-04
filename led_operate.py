print(__name__)
from led_protocol import ProtocolPacket
import serial

class LED:
    def __init__(self, port = "/dev/ttyUSB0", baud=57600, timeout=1):
        self.port = port
        self.baud = baud
        self.timeout = timeout
        self.serial = serial.Serial(self.port, self.baud, timeout=1)

    def turn_on(self):
        # 전원을 켜는 명령 전송
        led_start = ProtocolPacket.packet_start(self) + ProtocolPacket.power_ondata(self) + ProtocolPacket.packet_end(self)
        self.serial.write(led_start)
        print("LED 전광판 전원을 켰습니다.")

    def turn_off(self):
        # 전원을 끄는 명령 전송
        led_start = ProtocolPacket.packet_start(self) + ProtocolPacket.power_offdata(self) + ProtocolPacket.packet_end(self)
        self.serial.write(led_start)
        print("LED 전광판 전원을 껐습니다.")

    def close(self):
        self.serial.close() 
