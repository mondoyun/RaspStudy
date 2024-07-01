import serial
import time

class LED_Power_ON:
    port = "COM3"
    baud = 57600

    serial = serial.Serial(port, baud, timeout=1,parity=0)

    
