print(__name__)
from led_protocol import ProtocolPacket
import serial
# serial 통신 초기값
port = "/dev/ttyUSB0"
baud = 57600
timeout = 1
# packet 통신 고정 구조, 고정 값
Head_of_Frame = b'\x7E\x01'
Screen_ID = b'\xFE\xFE'
crc = b'\xFF\xFF'
eof = b'\x7E\x00'
# LED 전원 ON,OFF 고정 구조
Data_length = b'\x00\x0B'
Cmd_event = b'\x50\x57\x4F\x4E'
Sub_Cmd_ID = b'\x02'
len = b'\x00'
program_id = b'\x00\x00\x00\x00\x00'

class LED:
    def __init__(self):
        self.port = port
        self.baud = baud
        self.timeout = timeout
        self.serial = serial.Serial(self.port, self.baud, timeout=1)

    def packet_start(self):
        self.Head_of_Frame = Head_of_Frame
        self.Screen_ID = Screen_ID
        return Head_of_Frame + Screen_ID

    def packet_end(self):

        self.crc = crc
        self.eof = eof
        return crc + eof    
    
    def power_ondata(self): 
        
        self.Data_length = Data_length
        self.Cmd_event = Cmd_event
        self.Sub_Cmd_ID = Sub_Cmd_ID
        self.program_id = program_id
        return Data_length + Cmd_event + Sub_Cmd_ID + len + program_id
    
    def power_offdata(self,Sub_Cmd_ID = b'\x03'): 
        
        self.Data_length = Data_length
        self.Cmd_event = Cmd_event
        self.Sub_Cmd_ID = Sub_Cmd_ID
        self.len = len
        self.program_id = program_id
        return Data_length + Cmd_event + Sub_Cmd_ID + len + program_id

    def turn_on(self):
        # 전원을 켜는 명령 전송
        led_start = LED.packet_start(self) + LED.power_ondata(self) + LED.packet_end(self)
        self.serial.write(led_start)
        print("LED 전광판 전원을 켰습니다.")

    def message_init(self):
        # 메세지 초기화
        text_init = LED.packet_start(self) + ProtocolPacket.init_event(self) + LED.packet_end(self)
        self.serial.write(text_init)
        print("LED 전광판을 초기화했습니다.")

    def send_message(self):
        # 메세지 보내는 명령 전송
        send_text = ProtocolPacket.packet_start(self) + ProtocolPacket.send_text(self) + ProtocolPacket.packet_end(self)
        self.serial.write(send_text)
        print("LED 전광판 버퍼에 메세지를 보냈습니다.")

    def message_display(self):
        # 메세지 출력
        send_display = LED.packet_start(self) + ProtocolPacket.start_windows(self) + LED.packet_end(self)
        self.serial.write(send_display)
        print("LED 전광판에 메세지를 출력합니다.")

    def turn_off(self):
        # 전원을 끄는 명령 전송
        led_start = LED.packet_start(self) + LED.power_offdata(self) + LED.packet_end(self)
        self.serial.write(led_start)
        print("LED 전광판 전원을 껐습니다.")

    def close(self):
        self.serial.close()

