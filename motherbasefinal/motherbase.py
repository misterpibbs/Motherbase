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

    def bOn(self):   
        s.send("0")
        print ("Basement On")
    
    def bOff(self):
        s.send("1")
        print ("Basement Off") 

    def lOn(self):
        s.send("2")
        print ("Living room on")  
  
    def lOff(self):
        s.send("3")
        print ("Living room off") 
    
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["bg"] = "gray"
        self.QUIT["command"] = self.quit
   
        self.QUIT.pack(fill=X,padx=10)
  
        self.bO = Button(self)
        self.bO["text"] = "Basement On"
        self.bO["fg"] = "green"
        self.bO["command"] = self.bOn

        self.bO.pack(fill=X,padx=10)

        self.bF = Button(self)
        self.bF["text"] = "Basement Off",
        self.bF["fg"] = "red"
        self.bF["command"] = self.bOff

        self.bF.pack(fill=X,padx=10)
        
        self.lO = Button(self) 
        self.lO["text"] = "Living Room On"
        self.lO["fg"] = "green" 
        self.lO ["command"] = self.lOn

        self.lO.pack(fill=X,padx=10)

        self.lOff = Button(self)
        self.lOff["text"] = "Living Room Off"
        self.lOff["fg"] = "red"
        self.lOff["command"] = self.lOff

        self.lOff.pack(fill=X,padx=10)
         
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
  

  
