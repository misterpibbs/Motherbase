from Tkinter import *
import RPi.GPIO as GPIO
import socket
#import subprocess 
#from subprocess import call

TCP_IP = "10.0.0.11"
TCP_PORT = 5005
BUFFER_SIZE = 1024

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.OUT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


class Application(Frame):

    def lightOn(self):   
        s.send("0")
        print "ON"
    
    def lightOff(self):
        s.send("1")
        print ("OFF") 

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["bg"] = "gray"
        self.QUIT["command"] = self.quit
   
        self.QUIT.pack({"side": "bottom"})
  
        self.lO = Button(self)
        self.lO["text"] = "On"
        self.lO["fg"] = "green"
        self.lO["command"] = self.lightOn

        self.lO.pack({"side": "left"})

        self.lF = Button(self)
        self.lF["text"] = "Off",
        self.lF["fg"] = "red"
        self.lF["command"] = self.lightOff

        self.lF.pack({"side": "right"})
        

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
  

  
