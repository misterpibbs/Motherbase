import socket
import RPi.GPIO as GPIO 
import time  

# Server Side
# Set-up gpio channel
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.OUT, initial=GPIO.HIGH)

#sleeps the script for one minute allowing for interface to start and pull in a signal
#time.sleep(30)

# Socket Setup
TCP_IP = "10.0.0.140"
TCP_PORT = 5005
BUFFER_SIZE = 1024

while True:
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.bind((TCP_IP, TCP_PORT)) 
 s.listen(1)
 conn, addr = s.accept()
 print "Linked"
 while conn.recv(BUFFER_SIZE): 
  data = conn.recv(BUFFER_SIZE) 
  data = int(data) 
  GPIO.output(10, data) 
  pass
 else:
  conn.close()
