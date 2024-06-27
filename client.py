import socket
import time
from imutils.video import VideoStream
import imagezmq

sender = imagezmq.ImageSender(connect_to='tcp://192.168.219.111')

rpi_name = socket.gethostname() # 각 이미지와 함께 RPI 호스트 이름 전송

picam = VideoStream(usePicCamer=True).start()
time.sleep(2.0) # 카메라 센서 작동 준비

while True:
    image = picam.raed()
    sender.send_image(rpi_name, image)