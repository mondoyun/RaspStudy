import serial
import time

# serial 통신 초기값
port = "/dev/ttyUSB0"
baud = 57600
timeout = 1

# packet 통신 고정 구조, 고정 값
Head_of_Frame = b'\x7E\x01'
Screen_ID = b'\xFE\xFE'
crc = b'\xFF\xFF'
eof = b'\x7E\x00'

# 전원 ON, OFF 고정값
Data_length = b'\x00\x0B'
Cmd_event = b'\x50\x57\x4F\x4E'
len = b'\x00'
program_id = b'\x00\x00\x00\x00\x00'

class ProtocolPacket:

    def __init__(self, Data_length, Cmd_event, Sub_Cmd_ID, len):
        self.Data_length = Data_length
        self.Cmd_event = Cmd_event
        self.Sub_Cmd_ID = Sub_Cmd_ID
        self.len = len
    
    def packet_start(self):
        self.Head_of_Frame = Head_of_Frame
        self.Screen_ID = Screen_ID
        self.start_text = Head_of_Frame + Screen_ID
        return self.start_text

    def packet_end(self):
        self.crc = crc
        self.eof = eof
        self.end_text = crc + eof
        return self.end_text    
    
    def power_ondata(self):
        Sub_Cmd_ID = b'\x02'   
        self.program_id = program_id
        self.on_text = Data_length + Cmd_event + Sub_Cmd_ID + len + program_id
        return self.on_text
    
    def power_offdata(self): 
        Sub_Cmd_ID = b'\x03'
        self.program_id = program_id
        self.off_text = Data_length + Cmd_event + Sub_Cmd_ID + len + program_id
        return self.off_text
    
    def init_event(self, program_id = b'\x04\x00'):
        Data_length = b'\x00\x08'
        Cmd_event = b'\x45\x56\x45\x4E'
        Sub_Cmd_ID = b'\x01'
        len = b'\x02'
        self.program_id = program_id
        self.init_text = Data_length + Cmd_event + Sub_Cmd_ID + len + program_id
        return self.init_text
    
    def send_text(self, Windows_Number = b'\x01', X_POSITION = b'\x00\x00',W_WIDTH_PIXELS = b'\x40\x00',
                    Y_POSITION = b'\x00', H_HEIGHT_PIXELS = b'\x10', Action = b'\x02', Speed = b'\x00',
                    Stay_Seconds = b'\x00', Loop_Times = b'\x03', Memory_Position = b'\x01', Multi_Lines_Disp = b'\x00',
                    Align = b'\x00', font_Color = b'\x01', Reserved_Font_Mode = b'\x00',
                    font_ascii = b'\x01\x00', font_asian = b'\x02\x00',
                    Data = b'\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4'):
        user_data = input("문자를 입력하세요 : ")

    # def send_text(self):
    #     byte_data = b'\x7E\x01\xFE\xFE\x00\x2B\x45\x56\x45\x4E\x06\x25\x01\x00\x00\x40\x00\x00\x10\x02\x00\x00\x01\x01\x00\x00\x02\x00\x01\x00\x02\x00\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4\xFF\xFF\x7E\x00'    
    #     return byte_data

        # # UTF-8 인코딩으로 바이트로 변환
        # try:
        #     byte_data = user_input.encode('utf-8')
        # except UnicodeEncodeError as e:
        #     print(f"UnicodeEncodeError: {e}")
        # return
        # # 바이트 데이터를 문자열로 변환하여 출력
        # try:
        #     decoded_string = byte_data.decode('utf-8')
        #     print("Decoded string:", decoded_string)
        # except UnicodeDecodeError as e:
        #     print(f"UnicodeDecodeError: {e}")
        # Windows_Number = b'\x01'
        # X_POSITION = b'\x00\x00'
        # W_WIDTH_PIXELS = b'\x40\x00'
        # Y_POSITION = b'\x00'
        # H_HEIGHT_PIXELS = b'\x10'
        # Action = b'\x02'
        # Speed = b'\x00'
        # Stay_Seconds = b'\x00'
        # Loop_Times = b'\x03'
        # Memory_Position = b'\x01'
        # Multi_Lines_Disp = b'\x00'
        # Align = b'\x00'
        # font_Color = b'\x01'
        # Reserved_Font_Mode = b'\x00'
        # font_ascii = b'\x01\x00'
        # font_asian = b'\x02\x00'
        # Data = b'\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4'

        # \x7E\x01\xFE\xFE\x00\x2B\x45\x56\x45\x4E\x06\x25\x01\x00\x00\x40\x00\x00\x10\x02\x00\x00\x01\x01\x00\x00\x02\x00\x01\x00\x02\x00\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4\xFF\xFF\x7E\x00

        Data_length = b'\x00\x2B'
        Cmd_event = b'\x45\x56\x45\x4E'
        Sub_Cmd_ID= b'\x06'
        len= b'\x25'
        self.Windows_Number = Windows_Number
        self.X_POSITION = X_POSITION
        self.W_WIDTH_PIXELS = W_WIDTH_PIXELS
        self.Y_POSITION = Y_POSITION
        self.H_HEIGHT_PIXELS = H_HEIGHT_PIXELS
        self.Action = Action
        self.Speed = Speed
        self.Stay_Seconds = Stay_Seconds
        self.Loop_Times = Loop_Times
        self.Memory_Position = Memory_Position
        self.Multi_Lines_Disp = Multi_Lines_Disp
        self.Align = Align
        self.font_Color = font_Color
        self.Reserved_Font_Mode = Reserved_Font_Mode
        self.font_ascii = font_ascii
        self.font_asian = font_asian
        self.Data = Data
        self.user_data = bytes(user_data, 'utf-8')
        Full_Data = (Data_length + Cmd_event + Sub_Cmd_ID + len + Windows_Number +
                     X_POSITION + W_WIDTH_PIXELS + Y_POSITION + H_HEIGHT_PIXELS + 
                     Action + Speed + Stay_Seconds + Loop_Times + Memory_Position + Multi_Lines_Disp + 
                     Align + font_Color + Reserved_Font_Mode + font_ascii + font_asian + self.user_data)
        return Full_Data

        # buff_data = bytes(Full_Data, encoding ='utf-8')
    
    def print_windows(self, Reserved_Wnd = b'\xFF', Reserved = b'\x00'):

        Data_length = b'\x00\x08'
        Cmd_event = b'\x45\x56\x45\x4E'
        Sub_Cmd_ID = b'\x07'
        len = b'\x02'

        self.Reserved_Wnd = Reserved_Wnd
        self.Reserved = Reserved
        self.window_text = Data_length + Cmd_event + Sub_Cmd_ID + len + Reserved_Wnd + Reserved
        return self.window_text
    
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
        buff_text = send_text.decode('latin-1')
        print("LED 전광판 버퍼에 메세지를 보냈습니다.", buff_text)
        return buff_text
        
    def message_display(self):
        # 메세지 출력
        send_display = ProtocolPacket.packet_start(self) + ProtocolPacket.print_windows(self) + ProtocolPacket.packet_end(self)
        self.serial.write(send_display)
        

    def turn_off(self):
        # 전원을 끄는 명령 전송
        led_start = ProtocolPacket.packet_start(self) + ProtocolPacket.power_offdata(self) + ProtocolPacket.packet_end(self)
        self.serial.write(led_start)
        print("LED 전광판 전원을 껐습니다.")

    def close(self):
        self.serial.close() 

if __name__ == "__main__":
        # LED 전광판 객체 생성    
        LED = LED()

        # LED 전원 켜기
        LED.turn_on()
        time.sleep(1) # 1초 대기

        # 메세지 초기화
        LED.message_init()
        time.sleep(1) # 1초 대기

        # 메세지 보내는 명령 전송
        LED.send_message()
        time.sleep(1) # 1초 대기

        # 메세지 출력
        LED.message_display()
        print("LED 전광판에 메세지를 출력합니다.")
        time.sleep(2) # 2초 대기

        # LED 전원 끄기
        LED.turn_off()

        # 시리얼 포트 닫기
        LED.close()
    
