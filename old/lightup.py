import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 
GPIO.setup(11,GPIO.OUT) 
print "Led On"
GPIO.output(11,GPIO.HIGH) 

