import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 
GPIO.setup(13, GPIO.IN)
GPIO.setup(16, GPIO.IN) 
GPIO.setup(32, GPIO.OUT) 

GPIO.add_event_detect(13, GPIO.RISING)
GPIO.add_event_detect(16, GPIO.RISING) 

while True: 

 if GPIO.event_detected(13):
   GPIO.output(32, GPIO.HIGH) 
   
 elif GPIO.event_detected(16): 
   GPIO.output(32, GPIO.LOW) 
