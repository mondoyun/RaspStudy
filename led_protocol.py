print(__name__)
# b'' = byte 형태 / 데이터 통신에서 사용
# f' = f-string 형태 / 프로그래밍에서 문자열 조립에 유용하게 사용
# 이벤트 초기화 
# packet 고정 구조, 가변 데이터
Data_length = b'\x00\x08'
Cmd_event = b'\x45\x56\x45\x4E'
Sub_Cmd_ID = b'\x06'
len = b'\x02'
Data = b'\x5B\x46\x54\x35\x30\x31\x5D\xBE\xC8\xB3\xE7\xC7\xCF\xBC\xBC\xBF\xE4' # 나머지 구분할 수 없는 hex 값은 Data에 나열

class ProtocolPacket:
    
    def init_event(self, Sub_Cmd_ID = b'\x01',program_id = b'\x04\x00'):
        
        self.Data_length = Data_length
        self.Cmd_event = Cmd_event
        self.Sub_Cmd_ID = Sub_Cmd_ID
        self.len = len
        self.program_id = program_id
        return Data_length + Cmd_event + Sub_Cmd_ID + len + program_id
    
    def send_text(self, Data_length = b'\x00\x2B', Cmd_event = b'\x45\x56\x45\x4E', Sub_Cmd_ID= b'\x06',
                    len= b'\x25', Windows_Number = b'\x01', X_POSITION = b'\x00\x00',W_WIDTH_PIXELS = b'\x40\x00',
                    Y_POSITION = b'\x00', H_HEIGHT_PIXELS = b'\x10', Action = b'\x02', Speed = b'\x00',
                    Stay_Seconds = b'\x00', Loop_Times = b'\x03', Memory_Position = b'\x01', Multi_Lines_Disp = b'\x00',
                    Align = b'\x00', font_Color = b'\x01', Reserved_Font_Mode = b'\x00',
                    font_ascii = b'\x01\x00',font_asian= b'\x02\x00'):
    
        self.Data_length = Data_length
        self.Cmd_event = Cmd_event
        self.Sub_Cmd_ID = Sub_Cmd_ID
        self.len = len
        self.Data = Data
        Full_Data = (Data_length + Cmd_event + Sub_Cmd_ID + len + 
                     Windows_Number + X_POSITION + W_WIDTH_PIXELS + Y_POSITION + H_HEIGHT_PIXELS + 
                     Action + Speed + Stay_Seconds + Loop_Times + Memory_Position + Multi_Lines_Disp + 
                     Align + font_Color + Reserved_Font_Mode + font_ascii + font_asian + Data)
        return Full_Data
    
    def start_windows(self, Sub_Cmd_ID = b'\x07', Reserved_Wnd = b'\xFF', Reserved = b'\x00'):
        
        self.Data_length = Data_length
        self.Cmd_event = Cmd_event
        self.Sub_Cmd_ID = Sub_Cmd_ID
        self.len = len
        self.Reserved_Wnd = Reserved_Wnd
        self.Reserved = Reserved
        return Data_length + Cmd_event + Sub_Cmd_ID + len + Reserved_Wnd + Reserved
           

    