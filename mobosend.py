import socket 

UDP_IP = "10.0.0.151"
UDP_PORT = 5005 
CMD = "0" 
CMDOFF = "1"
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

while True: 
  on = "on"
  off = "off"
  var = input(["On or Off?"])
  if var == on:
   print "Sending"
   sock.sendto(CMD, (UDP_IP, UDP_PORT))
               
  elif var == off:
   print "Sending"
   sock.sendto(CMDOFF, (UDP_IP, UDP_PORT))

