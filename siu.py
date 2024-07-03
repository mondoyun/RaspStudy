import serial
import time

class ProtocolPacket:
    def start(self, Head_of_Frame = b'\x7E\x01', Screen_ID = b'\xFE\xFE'):
        self.Head_of_Frame = Head_of_Frame
        self.Screen_ID = Screen_ID
        return Head_of_Frame + Screen_ID

    def end(self, crc = b'\xFF\xFF', eof = b'\x7E\x00'):
        
        self.crc = crc
        self.eof = eof
    
        return crc + eof

    def data(self, Data_length = b'\x00\x0B', Cmd_event = b'\x50\x57\x4F\x4E',
              Sub_Cmd_ID = b'\x02', len = b'\x00', program_id = b'\x00\x00\x00\x00\x00'): 
        
        self.Data_length = Data_length
        self.Cmd_event = Cmd_event
        self.Sub_Cmd_ID = Sub_Cmd_ID
        self.len = len
        self.program_id = program_id
        return Data_length + Cmd_event + Sub_Cmd_ID + program_id
    
    def data2(self, Data_length = b'\x00\x0B', Cmd_event = b'\x50\x57\x4F\x4E',
              Sub_Cmd_ID = b'\x03', len = b'\x00', program_id = b'\x00\x00\x00\x00\x00'): 
        self.Data_length = Data_length
        self.Cmd_event = Cmd_event
        self.Sub_Cmd_ID = Sub_Cmd_ID
        self.len = len
        self.program_id = program_id
        return Data_length + Cmd_event + Sub_Cmd_ID + program_id
    
class LED:
    def __init__(self, port = "/dev/ttyUSB0", baud=57600, timeout=1):

        self.port = port
        self.baud = baud
        self.timeout = timeout
        self.serial = None
        self.serial = port,baud,timeout 
        self.serial = serial.Serial(self.port, self.baud, timeout=1)
    def turn_on(self):
        # 전원을 켜는 명령 전송
        led_start = ProtocolPacket.start(self) + ProtocolPacket.data(self) + ProtocolPacket.end(self)
        self.serial.write(led_start)
        print("LED 전광판 전원을 켰습니다.")

    def turn_off(self):
        # 전원을 끄는 명령 전송
        # self.serial.write(power_off_command)
        print("LED 전광판 전원을 껐습니다.")

    def close(self):
        self.serial.close() 

if __name__ == "__main__":
        # LED 전광판 객체 생성    
        LED = LED()

        # LED 전원 켜기
        LED.turn_on()
        time.sleep(4) # 4초 대기

        # LED 전원 끄기
        LED.turn_off()

        # 시리얼 포트 닫기
        LED.close()
    
