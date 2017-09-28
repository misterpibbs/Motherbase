import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

fobone = True

while fobone:
  basement = "b"
  basementOff = "bo"
  livingRoom = "l"
  livingRoomoff= "lo"
  bathroom = "br"
  bathroomOff = "bro"
  c = "c"
  all = "a"
  allOff = "ao"
  var = raw_input (["Whaddya' want?"])
  if var == basement:
    GPIO.output(10,GPIO.LOW)
  elif var == basementOff:
    GPIO.output(10,GPIO.HIGH)
    print "It's dark down here..."
  elif var == livingRoom:
    GPIO.output(11, GPIO.LOW)
    print "Living room lit"
  elif var == livingRoomoff:
    GPIO.output(11, GPIO.HIGH)
    print "Turn off the tv too!"
  elif var == bathroom:
    GPIO.output(12, GPIO.LOW)
    print "If you sprinkle when you tinkle..."
  elif var == bathroomOff:
    GPIO.output(12, GPIO.HIGH)
    print "Please be neat and wipe the seat!"
  elif var == all:
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    print "All On"
  elif var == allOff:
    GPIO.output(10, GPIO.HIGHH)
    GPIO.output(11, GPIO.HIGH)
    print "Lights Out"   
  elif var == c:
    fobone = False
    print "Ok :("
   
    
