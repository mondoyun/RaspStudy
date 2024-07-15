from LEDSerial import LED
import time
import cv2

if __name__ == "__main__":
    Led = LED("/dev/ttyUSB0", 57600, 1) # LED 전광판 객체 생성

    Led.PowerONandMsgInit()             # 전광판 켜기
    time.sleep(1)                       # 2초 대기

    while(1):
        Led.InputMSG()                      # 메세지 입력
        time.sleep(3)                       # 2초 대기   

        if Led.eventMSG.UsersendMSG[0] == ord('q'):
            break
        
        Led.startdisplay()                  # 메세지 출력
        time.sleep(3)                       # 2초 대기 

    Led.ClsBUFandOFF()                  # 버퍼 삭제 및 종료
    time.sleep(1)                       # 2초 대기

    Led.close()                         # 시리얼 포트 닫기