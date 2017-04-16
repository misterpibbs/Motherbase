import socket 
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BOARD) 
GPIO.setup( , GPIO.OUT)

UDP_IP = ""
UDP_PORT = "" 

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT)) 

GPIO.output( , False) 

while True:
  data, addr = sock.recvfrom(1024)
  data = int(data)
  GRPIO.output(data, True)
