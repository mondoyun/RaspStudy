print(__name__)
from led_operate import LED
import serial
import time
        
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

    
