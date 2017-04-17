import socket
import RPi.GPIO as GPIO 
 

# Server Side
# Set-up gpio channel
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)

# Socket Setup
TCP_IP = "10.0.0.151"
TCP_PORT = 5005
BUFFER_SIZE = 1024

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCPI_IP, TCP_PORT)) 
s.listen(1)

# Rceiving the data (int) that translates to on/off for light
conn, addr = s.accept()
print "Linked"
while 1: 
 data = conn.recv(BUFFER_SIZE) 
 if not data: break 
  GPIO.output(11, data) 
  
conn.close() 
