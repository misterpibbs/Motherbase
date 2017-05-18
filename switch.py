#This was a successful test script for adding a rocker switch to the pi
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40, GPIO.OUT) 
GPIO.setup(16, GPIO.IN)
GPIO.setup(15, GPIO.IN) 

while True: 
  if (GPIO.input(16)):
    GPIO.output(40, GPIO.LOW) 
  elif (GPIO.output(16)): 
    GPIO.output(40, GPIO.HIGH)
