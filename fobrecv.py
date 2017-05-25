import socket
import RPi.GPIO as GPIO 
import time  

# Server Side
# Set-up gpio channel
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.OUT, initial=GPIO.HIGH)

#sleeps the script for one minute allowing for interface to start and pull in a signal
time.sleep(30)

# Socket Setup
TCP_IP = "192.168.140.138"
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT)) 
s.listen(1)

# Rceiving the data (int) that translates to on/off for light
conn, addr = s.accept()
print "Linked"
while 1: 
 data = conn.recv(BUFFER_SIZE) 
 data = int(data) 
 GPIO.output(10, data) 
  
 
