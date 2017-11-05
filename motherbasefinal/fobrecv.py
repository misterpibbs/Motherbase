#!/usr/bin/env python

import socket
import RPi.GPIO as GPIO 
import time  

GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)


TCP_IP = "10.0.0.15"
TCP_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT)) 
s.listen(1)
conn, addr = s.accept()
print "Linked"

while True:  
 data = conn.recv(1024)
 data = str(data)

 if data == "bO":
  GPIO.output(10, 0) 

 elif data == "bF": 
  GPIO.output(10, 1)

 elif data == "lO":
  GPIO.output(11, 0)

 elif data == "lF":
  GPIO.output(11, 1)

 elif data == "aO":
  GPIO.output(10, 0)
  GPIO.output(11, 0)

 elif data == "aF":
  GPIO.output(10, 1)
  GPIO.output(11, 1)

else:
 conn.close()
