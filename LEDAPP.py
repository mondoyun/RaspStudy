from LEDSerial import LED
import time

if __name__ == "__main__":
    Led = LED() # LED 전광판 객체 생성
    Led.PowerON() # 전광판 켜기
    time.sleep(1) # 2초 대기

    Led.MsgInit() # 메세지 초기화
    time.sleep(1) # 2초 대기

    Led.sendMsgEvent() # 메세지 버퍼에 전송
    time.sleep(3) # 2초 대기

    Led.startMsgWindow() # 메세지 출력
    time.sleep(3) # 2초 대기

    Led.ClsBUF() # 버퍼 삭제
    time.sleep(1) # 2초 대기

    Led.PowerOFF() # LED 전원 끄기
    time.sleep(1) # 2초 대기

    Led.close() # 시리얼 포트 닫기