import serial
import threading
import time
import string

class LED_TEST :

    port = "COM3"
    baud = 57600

    ser = serial.Serial(port, baud, timeout=1)
    # 2.1 = 18 이벤트 초기화
    # 2.2 = 16 이벤트 나가기
    # 2.3 = 23 
    # X POSITION = 00 00
    # W WIDTH PIXELS = 40 00 
    # Y POSITION = 00
    # H HEIGHT PIXELS = 10
    # Memory Position = 00

    # 2.4 Display from Memory B = 24 
    # X POSITION = 00 00
    # W WIDTH PIXELS = 40 00
    # Y POSITION = 00
    # H HEIGHT PIXELS = 10
    # Reserved = 00
    # Display Action = 02
    # 2.4 Roll Memory B to Display Memory = 19
    # Move Pixels = 10
    # Use Buffer Data? = 01
    # Roll Direction = 01
    # 2.5 = 12 + 6 + 6 = 24 
    # X POSITION = 00 00
    # W WIDTH PIXELS = 40 00
    # Y POSITION = 00
    # H HEIGHT PIXELS  = 10
    # 2.6.1  Print Text to Display Area = 63
    # Reserved = 00
    # X POSITION = 00 00
    # W WIDTH PIXELS = 40 00
    # Y POSITION = 00
    # H HEIGHT PIXELS = 10
    # What Memory area = 00
    # Rotate Speed = 00
    # Stay Time = 00
    # Loop Times = 00
    # Reserved = 01
    # Multi-Line Display = 00
    # Align = 00
    # Default Color = 00
    # Reserved(FontMode) = 00
    # Western Font ID = 01 00 
    # Asian Font ID = 02 00
    # 5B 43 48 38 5D 41 42 5B
    # 43 52 5D 43 44 5B 46 43
    # 30 31 5D 5B 46 54 31 30
    # Display Message = 31 5D 62
    # 2.6.2 Print Text to Windows = 63
    # Windows Number = 02
    # X POSITION = 40 00
    # W WIDTH PIXELS = 40 00
    # Y POSITION = 00 
    # H HEIGHT PIXELS = 10
    # Action = 01 
    # Speed of Rotate = 00
    # Stay Seconds = 00
    # Loop Times = 00
    # Memory Position = 01
    # Multi Lines Disp = 00
    # Align = 00
    # Default Color = 00
    # Reserved(Font Mode) = 00
    # English Font ID = 01 00
    # Asian Font ID = 02 00
    # 5B 43 48 38 5D 41 42 5B
    # 43 52 5D 43 44 5B 46 43 
    # 30 31 5D 5B 46 54 31 30
    # Display Text = 31 5D 62
    # 2.7 Start to Run All Windows from Back Windows = 18
    # Reserved(Wnd#) = FF
    # Reserved = 00
    # 2.8 Clear all data in Back Windows = 17
    # Reserved(Wnd#) = FF
    # 2.9 LINK to an Existed Program = 6 + 53 + 4 = 63
    # 6 + 26 + 4 = 36
    # Windows Number = 01
    # X POSITION = 00 00
    # W WIDTH PIXELS = 40 00
    # Y POSITION = 00
    # H HEIGHT PIXELS = 10
    # x = 01 
    # x = 00 
    # x = 00 
    # x = 00 
    # x = 01 
    # x = 00 
    # x = 00 
    # x = 00
    # x = 00
    # LinkPgm = 00 C8
    # x(Wnd) = 00
    # x(Msg) = 00
    # 2.10 = 
    
    # 버퍼 화면에 텍스트 넣기
    '\x7E\x01\xFE\xFE\x00\x25\x45\x56\x45\x4E\x06\x1F\x01\x00\x00\x40\x00\x00\x10\x01\x00\x00\x00\x01\x00\x00\x01\x00\x01\x00\x02\x00\x68\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64\xFF\xFF\x7E\x00'
    # Manual Event function 
    # 이벤트 초기화 2.1
    init_event = b'\x7E\x01\xFE\xFE\x00\x08\x45\x56\x45\x4E\x01\x02\x04\x00\xFF\xFF\x7E\x00'

    # 이벤트 나가기 2.2
    exit_event = b'\x7E\x01\xFE\xFE\x00\x06\x45\x56\x45\x4E\x00\x00\xFF\xFF\x7E\x00'

    # 화면에 출력하기 2.7
    start_windows = b'\x7E\x01\xFE\xFE\x00\x08\x45\x56\x45\x4E\x07\x02\xFF\x00\xFF\xFF\x7E\x00'

    # 버퍼 지우기 2.8
    clear_buff = b'\x7E\x01\xFE\xFE\x00\x07\x45\x56\x45\x4E\x08\x01\xFF\xFF\xFF\x7E\x00'

    # be fixed Text
    fixed_start_text = b'\x7E\x01\xFE\xFE\x00' # 첫 시작 [:4] 고정값
    fixed_end_text = b'\xFF\xFF\x7E\x00' # 끝 부분 [-4:] 고정값

    # Times - 반복 횟수 (23 - 5)
    times_always = '\x00'
    times_one = '\x01'
    times_two = '\x02'
    times_three = '\x03'
    times_four = '\x04'
    times_five = '\x05'
    times_six = '\x06'
    times_seven = '\x07'
    times_eight = '\x08'
    times_nine = '\x09'
    times_ten = '\x0A'

    # Action - LED 화면 움직임 (20 - 5)
    action_hold = '\x01'    # 고정
    action_rotate = '\x02'  # 좌 <ㅡ 우
    action_rotate_right = '\x03'    # 좌 ㅡ> 우 (text도 좌에서부터 출력됨)
    action_shutter = '\x04'     # 중앙에서부터 사이드로 점차 퍼지면서,,?
    action_snow = '\x05'    # 눈 내리듯이 위에서 아래로
    action_sparkle = '\x06'     # 반짝반짝 사라졌다가 생김
    action_triangle = '\x07'    # 첫 text부터 위에서 아래로 생김
    action_wide = '\x08'    # 좌 <ㅡ 우 는 같은데 늘어졌다가 원래 사이즈로?
    action_roll_left = '\x09'   # 좌 <ㅡ 우 인데 속도가 빠름
    action_roll_right ='\x0A'   # 좌 ㅡ> 우 (text 변경이 되지 않음)
    action_roll_up = '\x0B'     # 아래에서 위로 text 올라옴
    action_roll_down = '\x0C'   # 위에서 아래로 text 내려감
    action_wipe_left = '\x0D'   # 끝 text부터 처음 text까지 순서대로 ? (한 번 생기고 만다)
    action_wipe_right = '\x0E'  # 첫 text부터 끝 text까지 순서대로 (한 번 생기고 만다)
    action_wipe_down = '\x0F'   # text가 상단부터 하단까지??
    action_wipe_up = '\x10'
    action_hold_flash = '\x11'  # 제자리에서 깜빡임

    # Speed - Action 값에 대한 속도값 (숫자가 높아질수록 느린거 같음) (21 - 5)
    speed_fast = '\x00'
    speed_two = '\x01'
    speed_three = '\x02'
    speed_four = '\x03'
    speed_five = '\x04'
    speed_six = '\x05'

    # Font ASIAN - 뭐가 달라지는지 모르겠다 (32 - 5)
    asian_12 = '\x00'
    asian_16 = '\x10'

    # Font ASCII - 글꼴 폰트 + 사이즈 (30 - 5)
    font_sans_7x5 = '\x00'
    font_sans_7x6 = '\x01'
    font_sans_7x7 = '\x02'
    font_efont_12x8 = '\x08'
    font_normal_16x8 = '\x10'
    font_thin_16x8 = '\x11'
    font_thick_16x8 = '\x12'
    font_digit_16x8 = '\x18'
    font_mincho_16x8 = '\x21'
    font_pmincho_14x12 = '\x20'

    # Font Color - 글꼴 색 지정 (27 - 5)
    color_default = '\x00'
    color_red = '\x01'
    color_green = '\x02'
    color_yellow = '\x03'
    color_blue = '\x04'
    color_pink = '\x05'
    color_cyan = '\x06'
    color_white = '\x07'

    def __init__(self) :
        # Manual Event
        self.send_text = None

    def Send_TXT(self, times, action, speed, font_asian, font_ascii, font_color) :
        # 47
        data = f'\x25\x45\x56\x45\x4E\x06\x1F\x01\x00\x00\x40\x00\x00\x10{action}{speed}\x00{times}\x01\x00\x00{font_color}\x00\x01{font_ascii}\x02{font_asian}\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7'
        buff_data = bytes(data, encoding='latin-1')

        print(buff_data)

        self.send_text = self.fixed_start_text + buff_data + self.fixed_end_text
        return self.send_text

    def Maual_Event(self, send):

        self.ser.write(bytearray(self.init_event))
        time.sleep(0.1)
        self.ser.write(bytearray(send))
        time.sleep(0.1)
        self.ser.write(bytearray(self.start_windows))
        time.sleep(0.1)

    def run(self) :

        self.Maual_Event(self.Send_TXT(self.times_always, self.action_snow, self.speed_two, self.asian_12, self.font_sans_7x5, self.color_red))

LED = LED_TEST()
LED.run()