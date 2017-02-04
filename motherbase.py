import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(FALSE) 
GPIO.setup(17,GPIO.OUT)
on = 'on' 
off = 'off' 
var = input (["On or Off?"]) 
if var == on: 
  GPIO.Output(17,GPIO.LOW)
  print "LED ON" 
elif var == off: 
  GPIO.Output(17,GPIO.HIGH) 
  print "LED OFF" 
