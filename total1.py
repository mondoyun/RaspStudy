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

# # Action - LED 화면 움직임 (20 - 5)
# action_hold = '\x01'    # 고정
# action_rotate = '\x02'  # 좌 <ㅡ 우
# action_rotate_right = '\x03'    # 좌 ㅡ> 우 (text도 좌에서부터 출력됨)
# action_shutter = '\x04'     # 중앙에서부터 사이드로 점차 퍼지면서,,?
# action_snow = '\x05'    # 눈 내리듯이 위에서 아래로
# action_sparkle = '\x06'     # 반짝반짝 사라졌다가 생김
# action_triangle = '\x07'    # 첫 text부터 위에서 아래로 생김
# action_wide = '\x08'    # 좌 <ㅡ 우 는 같은데 늘어졌다가 원래 사이즈로?
# action_roll_left = '\x09'   # 좌 <ㅡ 우 인데 속도가 빠름
# action_roll_right ='\x0A'   # 좌 ㅡ> 우 (text 변경이 되지 않음)
# action_roll_up = '\x0B'     # 아래에서 위로 text 올라옴
# action_roll_down = '\x0C'   # 위에서 아래로 text 내려감
# action_wipe_left = '\x0D'   # 끝 text부터 처음 text까지 순서대로 ? (한 번 생기고 만다)
# action_wipe_right = '\x0E'  # 첫 text부터 끝 text까지 순서대로 (한 번 생기고 만다)
# action_wipe_down = '\x0F'   # text가 상단부터 하단까지??
# action_wipe_up = '\x10'
# action_hold_flash = '\x11'  # 제자리에서 깜빡임

# # Times - 반복 횟수 (23 - 5)
# times_always = '\x00'
# times_one = '\x01'
# times_two = '\x02'
# times_three = '\x03'
# times_four = '\x04'
# times_five = '\x05'
# times_six = '\x06'
# times_seven = '\x07'
# times_eight = '\x08'
# times_nine = '\x09'
# times_ten = '\x0A'

# # Speed - Action 값에 대한 속도값 (숫자가 높아질수록 느린거 같음) (21 - 5)
# speed_fast = '\x00'
# speed_two = '\x01'
# speed_three = '\x02'
# speed_four = '\x03'
# speed_five = '\x04'
# speed_six = '\x05'

# # Font ASIAN - 뭐가 달라지는지 모르겠다 (32 - 5)
# asian_12 = '\x00'
# asian_16 = '\x10'

# # Font ASCII - 글꼴 폰트 + 사이즈 (30 - 5)
# font_sans_7x5 = '\x00'
# font_sans_7x6 = '\x01'
# font_sans_7x7 = '\x02'
# font_efont_12x8 = '\x08'
# font_normal_16x8 = '\x10'
# font_thin_16x8 = '\x11'
# font_thick_16x8 = '\x12'
# font_digit_16x8 = '\x18'
# font_mincho_16x8 = '\x21'
# font_pmincho_14x12 = '\x20'

# # Font Color - 글꼴 색 지정 (27 - 5)
# color_default = '\x00'
# color_red = '\x01'
# color_green = '\x02'
# color_yellow = '\x03'
# color_blue = '\x04'
# color_pink = '\x05'
# color_cyan = '\x06'
# color_white = '\x07'

# # 2.6.2
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
    
    # def send_text(self):
    #     data = b'\x7E\x01\xFE\xFE\x00\x2B\x45\x56\x45\x4E\x06\x25\x01\x00\x00\x40\x00\x00\x10\x02\x00\x00\x01\x01\x00\x00\x02\x00\x01\x00\x02\x00\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4\xFF\xFF\x7E\x00'
    #     return data

    def send_text(self, Windows_Number = b'\x01', X_POSITION = b'\x00\x00',W_WIDTH_PIXELS = b'\x40\x00',
                    Y_POSITION = b'\x00', H_HEIGHT_PIXELS = b'\x10', Action = b'\x02', Speed = b'\x00',
                    Stay_Seconds = b'\x00', Loop_Times = b'\x03', Memory_Position = b'\x01', Multi_Lines_Disp = b'\x00',
                    Align = b'\x00', font_Color = b'\x01', Reserved_Font_Mode = b'\x00',
                    font_ascii = b'\x01\x00', font_asian = b'\x02\x00',
                    Data = b'\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xC7\xCF'):
                  # Data = b'\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4'
    # def send_text(self, Windows_Number, X_POSITION, W_WIDTH_PIXELS, Y_POSITION, H_HEIGHT_PIXELS,
    #                Action, Speed, Stay_Seconds, Loop_Times, Memory_Position, Multi_Lines_Disp, Align,
    #                  font_Color, Reserved_Font_Mode, font_ascii, font_asian, Data):


        Data_length = b'\x00\x26'
        Cmd_event = b'\x45\x56\x45\x4E'
        Sub_Cmd_ID= b'\x06'
        len= b'\x20'
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
        full_Data = (Data_length + Cmd_event + Sub_Cmd_ID +len +
                    Windows_Number + X_POSITION + W_WIDTH_PIXELS + Y_POSITION + H_HEIGHT_PIXELS +
                    Action + Speed + Stay_Seconds + Loop_Times + Memory_Position + Multi_Lines_Disp +
                    Align + font_Color + Reserved_Font_Mode + font_ascii + font_asian + Data)
        Full_Data = self.start_text + full_Data + self.end_text
        return Full_Data
    
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
        # send_text = ProtocolPacket.send_text(self)
        self.serial.write(send_text)
        buff_text = send_text.decode('latin-1')
        print("LED 전광판 버퍼에 메세지를 보냈습니다.", buff_text)
        
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
    
