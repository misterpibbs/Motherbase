import socket 
# Setup socket connection
TCP_IP = "10.0.0.151"
TCP_PORT = 5005
BUFFER_SIZE = 1024
CMD = "0" 
CMDOFF = "1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True: 
  on = "on"
  off = "off"
  c = "c"
  var = input(["On or Off?"])
  if var == on:
    print "Sending"
    s.send(CMD)
    
               
  elif var == off:
    print "Sending"
    s.send(CMDOFF)
    
  elif var == c:
    print "Goodbye"
    s.close()
