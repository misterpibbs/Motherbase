import RPi.GPIO as GPIO 
import socket 

TCP_IP = "10.0.0.10"
TCP_PORT = 5005
BUFFER_SIZE = 1024
CMD = "0"
CMDOFF = "1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((TCP_IP, TCP_PORT))

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(13, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(32, GPIO.OUT) 

GPIO.add_event_detect(13, GPIO.RISING)
GPIO.add_event_detect(16, GPIO.RISING) 

while True: 

 GPIO.event_detected(13)
 GPIO.event_detected(16)

 if GPIO.event_detected(16):
  s.send(CMDOFF) 

 if GPIO.event_detected(13): 
  s.send(CMD) 
  
