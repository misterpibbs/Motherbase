import socket 

UDP_IP = "10.0.0.151"
UDP_PORT = 5005 
CMD = "11" 

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

while True: 
  on = "on"
  off = "off"
  var = input(["On or Off?])
               if var == on:
               print "Sending"
               sock.sendto(CMD, "1", (UDP_IP, UDP_PORT))
               
               elif var == off:
               print "Sending"
               sock.sendto(CMD, "0" (UDP_IP, UDP_PORT))

