import cv2
import imagezemq

image_hub = imagezemq.ImageHub()

while True:
    rpi_name, image = image_hub.recv_image()

    cv2.imshow(rpi_name, image)
    if cv2.waitKey(1) == ord('q'):
        break

    image_hub.send_reply(b'ok')