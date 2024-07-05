import serial
import threading
import time

class SerialCommunication:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.serial = None
        self.thread = None
        self.is_reading = False
        
    def connect(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"Connected to {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            print(f"Failed to connect to {self.port}: {e}")
            return False
        return True
    
    def start_reading(self):
        self.is_reading = True
        self.thread = threading.Thread(target=self.read_serial)
        self.thread.start()
    
    def read_serial(self):
        while self.is_reading:
            if self.serial.in_waiting > 0:
                data = self.serial.readline().decode().strip()
                print(f"Received data: {data}")
                self.handle_data(data)
            time.sleep(0.1)  # 잠시 대기해서 다시 확인
            
    def handle_data(self, data):
        # 데이터 처리 로직을 여기에 구현합니다.
        # 예시로 받은 데이터를 출력하는 것으로 대체합니다.
        print(f"Handling data: {data}")
        
    def stop_reading(self):
        self.is_reading = False
        if self.thread:
            self.thread.join()
        if self.serial and self.serial.is_open:
            self.serial.close()
            print(f"Disconnected from {self.port}.")
    
    def send_data(self, data):
        if self.serial and self.serial.is_open:
            self.serial.write(data.encode())
            print(f"Sent data: {data}")
        else:
            print("Serial port is not open.")
            
# 시리얼 포트와 보드레이트 설정
port = "/dev/ttyUSB0"  # 예시로 리눅스에서의 시리얼 포트
baudrate = 9600

# 시리얼 통신 객체 생성
serial_comm = SerialCommunication(port, baudrate)

# 시리얼 연결
if serial_comm.connect():
    # 이벤트 드리븐 방식으로 데이터 읽기 시작
    serial_comm.start_reading()
    
    try:
        # 사용자 입력을 받아서 시리얼 포트로 데이터 전송
        while True:
            user_input = input("Enter data to send (q to quit): ")
            if user_input.lower() == 'q':
                break
            serial_comm.send_data(user_input)
            
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt. Exiting...")
    
    finally:
        # 종료 시 시리얼 통신 종료
        serial_comm.stop_reading()

