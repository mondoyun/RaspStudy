from LEDSerial import LED
import time

if __name__ == "__main__":

    Led = LED("/dev/ttyUSB0", 57600, 1) # LED 전광판 객체 생성

    Led.PowerOnMsgInit()                # 전광판 켜기
    time.sleep(1)                       # 1초 대기

    while(1):
        Led.InputMSG()                  # 메세지 입력
        time.sleep(3)                   # 3초 대기   
 
        Led.startdisplay()              # 메세지 출력
        time.sleep(3)                   # 3초 대기 
        user_input = input("종료 명령('q'누르면 종료) : ")
        if user_input == 'q':
            print("프로그램을 종료합니다")
            break
        else:
            print("기존문자열을 출력합니다.")

    Led.ClearbufPoweroff()                # 버퍼 삭제 및 종료
    time.sleep(1)                       # 1초 대기

    Led.Close()                         # 시리얼 포트 닫기