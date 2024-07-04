import serial
import time
# 전원 켜는 명령 전송 hex(16진수로 되어있음) 상수를 변수로 선언하고 사용
power_on_command = b'\x7E\x01\xFE\xFE\x00\x0B\x50\x57\x4F\x4E\x02\x00\x00\x00\x00\x00\x00\xFF\xFF\x7E\x00'
power_off_command = b'\x7E\x01\xFE\xFE\x00\x0B\x50\x57\x4F\x4E\x03\x00\x00\x00\x00\x00\x00\xFF\xFF\x7E\x00'

class LED:
    def __init__(self):
        self.port = "/dev/ttyUSB0"
        self.baud = 57600
        self.serial = serial.Serial(self.port, self.baud, timeout=1)

    def turn_on(self):
        self.serial.write(power_on_command)
        print("전광판을 켜라")

    def turn_off(self):
        self.serial.write(power_off_command)
        print("LED 전광판 전원을 껐습니다.")

    def close(self):
        self.serial.close()

LED = LED()
LED.turn_on()
time.sleep(3) # 3초간 대기하라
LED.turn_off()
LED.close()
        