import serial
import threading
import time
import string

# COM4

port = "COM11"
baud = 57600
ser = serial.Serial(port, baud, timeout=1)

initial_func = b'\x7E\x01\xFE\xFE\x00\x08\x45\x56\x45\x4E\x01\x02\x04\x00\xFF\xFF\x7E\x00'
start_windows = b'\x7E\x01\xFE\xFE\x00\x08\x45\x56\x45\x4E\x07\x02\xFF\x00\xFF\xFF\x7E\x00'


def Maual_Event(send_text) :

    ser.write(bytearray(initial_func))

    time.sleep(0.1)

    ser.write(bytearray(send_text))

    time.sleep(0.1)

    ser.write(bytearray(start_windows))


def readthread() :

    while True :
        if ser.readable() :
            res = ser.readline()

readthread()