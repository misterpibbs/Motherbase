import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 
GPIO.setup(11,GPIO.OUT)
fobone = True 
while fobone:
  on = "on" 
  off = "off"
  c = "c"
  var = input(["On or Off?"])
  if var == on: 
    GPIO.output(11,GPIO.LOW)
    print "LED on"
    continue
  elif var == off:
    GPIO.output(11,GPIO.HIGH)
    print "LED off" 
    continue 
  elif var == c:
    fobone = False
    print "Goodbye" 
