print(__name__)
from led_module import LED
import serial
import time
        
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
        time.sleep(2) # 2초 대기

        # LED 전원 끄기
        LED.turn_off()

        # 시리얼 포트 닫기
        LED.close()
 

    
