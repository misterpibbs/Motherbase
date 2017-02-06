import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(FALSE) 
GPIO.setup(17,GPIO.OUT)
fobone = True 
while fobone:
  on = "on" 
  off = "off" 
  var = input(["On or Off?"])
  if var == on: 
    GPIO.output(17,LOW)
    print "LED on"
    continue
  elif var == off:
    GPIO.output(17,HIGH)
    print "LED off" 
    continue 
