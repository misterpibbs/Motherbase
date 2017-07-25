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
   
        self.QUIT.grid(row=2, columnspan=2)
  
        self.bO = Button(self)
        self.bO["text"] = "Basement On"
        self.bO["fg"] = "green"
        self.bO["command"] = self.bOn

        self.bO.grid(row=0, column=0)

        self.bF = Button(self)
        self.bF["text"] = "Basement Off"
        self.bF["fg"] = "red"
        self.bF["command"] = self.bOff

        self.bF.grid(row=1, column=0)
        
        self.lO = Button(self) 
        self.lO["text"] = "Living Room On"
        self.lO["fg"] = "green" 
        self.lO ["command"] = self.lOn

        self.lO.grid(row=0, column=1)

        self.lf = Button(self)
        self.lf["text"] = "Living Room Off"
        self.lf["fg"] = "red"
        self.lf["command"] = self.lOff

        self.lf.grid(row=1, column=1)
         
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.wm_title("Welcome to Motherbase")
app = Application(master=root)
app.mainloop()
root.destroy()
  

  
