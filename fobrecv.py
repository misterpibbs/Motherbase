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

while True:

