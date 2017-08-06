import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

fobone = True
while fobone:
  basement = "b"
  basementoff = "bo"
  livingroom = "l"
  livingroomoff= "lo"
  bathroom = "br"
  bathroomoff = "bro"
  c = "c"
  var = raw_input (["Whaddya' want?"])
  if var == basement:
    GPIO.output(10,GPIO.LOW)
    print "Basement Illuminated"
    continue 
  elif var == basementoff:
    GPIO.output(10,GPIO.HIGH)
    print "It's dark down here..."
    continue 
  elif var == livingroom:
    GPIO.output(11,GPIO.LOW)
    print "Living room lit"
    continue
  elif var == livingroomoff:
    GPIO.output(11,GPIO.HIGH)
    print "Turn off the tv too!"
  elif var == bathroom:
    GPIO.output(12,GPIO.LOW)
    print "If you sprinkle when you tinkle..."
  elif var == bathroomoff:
    GPIO.output(12,GPIO.HIGH)
    print "Please be neat and wipe the seat!"
  elif var == c:
    fobone = False
    print "Ok :("
   
    
