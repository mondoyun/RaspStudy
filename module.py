print(__name__)
from protocol import ProtocolPacket
import serial

# serial 통신 초기값
port = "/dev/ttyUSB0"
baud=57600
timeout=1
class LED:

    def __init__(self):

        self.port = port
        self.baud = baud
        self.timeout = timeout
        self.serial = serial.Serial(self.port, self.baud, timeout=1)

    def turn_on(self):
        # 전원을 켜는 명령 전송
        led_start = ProtocolPacket.packet_start(self) + ProtocolPacket.power_ondata(self) + ProtocolPacket.packet_end(self)
        self.serial.write(led_start)
        print("LED 전광판 전원을 켰습니다.")

    def message_init(self):
        # 메세지 초기화
        text_init = ProtocolPacket.packet_start(self) + ProtocolPacket.init_event(self) + ProtocolPacket.packet_end(self)
        self.serial.write(text_init)
        print("LED 전광판을 초기화했습니다.")

    def send_message(self):
        # 메세지 보내는 명령 전송
        send_text = ProtocolPacket.packet_start(self) + ProtocolPacket.send_text(self) + ProtocolPacket.packet_end(self)
        self.serial.write(send_text)
        print("LED 전광판 버퍼에 메세지를 보냈습니다.")
    

    def message_display(self):
        # 메세지 출력
        send_display = ProtocolPacket.packet_start(self) + ProtocolPacket.print_windows(self) + ProtocolPacket.packet_end(self)
        self.serial.write(send_display)
        print("LED 전광판에 메세지를 출력합니다.")
    

    def turn_off(self):
        # 전원을 끄는 명령 전송
        led_start = ProtocolPacket.packet_start(self) + ProtocolPacket.power_offdata(self) + ProtocolPacket.packet_end(self)
        self.serial.write(led_start)
        print("LED 전광판 전원을 껐습니다.")

    def close(self):
        self.serial.close()

