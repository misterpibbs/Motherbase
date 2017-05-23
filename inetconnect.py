#Internet connectivity checker and indicator.  

import RPi.GPIO as GPIO 
import time 
import urllib2

def check(pin): #sets blinking led function
 GPIO.output(pin, 1)
 time.sleep(.3)
 GPIO.output(pin, 0)
 time.sleep(.3)
 return 
 
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 
GPIO.setup(11, GPIO.OUT) 

def inet_connect(): #sets internet connectivity check function
 try:
  urllib2.urlopen('http://www.google.com', timeout=1)
  return True  
 except urllib2URLError as err:  
  return False

for i in range(0,10): #blinks led confirming previous script ran successfully
 check(11)

inet_connect() #runs internet function

if inet_connect() == True: #if elif returns solid led if connection works
  GPIO.output(11, 1) 
  print "Connected" 

elif inet_connect() == False: 
  check(11) 
  print "Not yet..."
