# This is the start of the internet connectivity checker. This script is to be run at startup. When 
# an internet connection is established it will light an LED letting the user know that a connection
# has been established. 

import RPi.GPIO as GPIO 
import socket 
import time 
import urllib2

GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 
GPIO.setup(11, GPIO.OUT) 

def inet_connect():
 try:
  urllib2.urlopen('http://www.capitalteas.com', timeout=1)
  print "Connected"
  return True  
 except urllib2URLError as err: 
  print "Nah" 
  return False

inet_connect() 

if inet_connect() == True: 
  GPIO.output(11, 1) 
  print "Connected" 

elif inet_connect() == False: 
  GPIO.output(11, 0) 
  print "Nope" 
