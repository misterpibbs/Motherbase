import socket 

UDP_IP = ""
UDP_PORT = "" 
CMD = "" 

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
                     
sock.sendto(CMD, (UDP_IP, UDP_PORT))
