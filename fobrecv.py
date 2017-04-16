import socket
import RPi.GPIO as GPIO 

# Client side
# Set-up gpio channel
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)

# Socket Setup
UDP_IP = "10.0.0.151"
UDP_PORT = 5005
# Some dead ass wrong code that I wrote. Still trying to figure out how to recv both the pin and output from motherbase.
while True:
  socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  socket.bind((UDP_IP, UDP_PORT)) 
  data, addr = socket.recvfrom(1024) 
  print "Incoming" 
  data = int(data) 
  GPIO.output(data) 
  continue 
  

