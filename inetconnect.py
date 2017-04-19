# This is the start of the internet connectivity checker. This script is to be run at startup. When 
# an internet connection is established it will light an LED letting the user know that a connection
# has been established. 

import RPi.GPIO as GPIO 
import socket 
import time 

GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 
GPIO.setup( , GPIO.OUT) 
