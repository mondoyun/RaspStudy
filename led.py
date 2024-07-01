import serial
import time

class LED_Power_ON:
    def __init__(self):

        self.port = "/dev/ttyUSB0"
        self.baud = 57600
        self.serial = serial.Serial(self.port, self.baud, timeout=1)

    # Manual Event function
    # init_event = b'\x7E\x01\xFE\xFE\x00\x08\x45\x56\x45\x4E\x01\x02\x04\x00\xFF\xFF\x7E\x00'
    # start_windows = b'\x7E\x01\xFE\xFE\x00\x08\x45\x56\x45\x4E\x07\x02\xFF\x00\xFF\xFF\x7E\x00'
    # exit_event = b'\x7E\x01\xFE\xFE\x00\x06\x45\x56\x45\x4E\x00\x00\xFF\xFF\x7E\x00'
    # clear_buff = b'\x7E\x01\xFE\xFE\x00\x07\x45\x56\x45\x4E\x08\x01\xFF\xFF\xFF\x7E\x00'

    # be fixed Text
    # fixed_start_text = b'\x7E\x01\xFE\xFE\x00' # 첫 시작 [:4] 고정값
    # fixed_end_text = b'\xFF\xFF\x7E\x00' # 끝 부분 [-4:] 고정값

    def turn_on(self):
        # 전원을 켜는 명령 전송
        power_on_command = b'\x7E\x01\xFE\xFE\x00\x0B\x50\x57\x4F\x4E\x02\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\x7E\x00'
        self.serial.write(power_on_command)
        print("LED 전광판 전원을 켰습니다.")

    def turn_off(self):
        # 전원을 끄는 명령 전송
        power_off_command = b'\x7E\x01\xFE\xFE\x00\x0B\x50\x57\x4F\x4E\x03\x00\x00\x00\x00\x00\x00\xFF\xFF\x7E\x00'
        self.serial.write(power_off_command)
        print("LED 전광판 전원을 껐습니다.")

    def close(self):
        self.serial.close()        
# LED 전광판 객체 생성    
LED = LED_Power_ON()

# LED 전원 켜기
LED.turn_on()
time.sleep(1)  # 예시로 1초 대기

# LED 전원 끄기
LED.turn_off()

# 시리얼 포트 닫기
LED.close()
