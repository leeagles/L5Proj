# import interface code
from tkinter import *
# import random num generator functions
from random import randint
#sensor read


def drawButton1():
    # add a button called ButtonA
    buttonA = Button(window, text="Read Sensor", command=sensorOn)
    buttonA.pack()


def drawButton2():
    buttonB = Button(window, text="Sensor Off", command=sensorOff)
    buttonB.pack()

def drawButton2():
    buttonB = Button(window, text="Sensor On", command=sensorOn)
    buttonB.pack()

def drawWindow(status):
    # start a window
    window = Tk()
    # add a text area called text
    text = Text(window, width=10, height=1, fg="blue", bg="white")
    # use the pack() function to add components to window
    text.pack()

    drawButton1()
    if (status == 1):
        drawButton2()
    else:
        drawButton3()

def sensorOn():
         text.delete(0.0, END)
         text.insert(END, str(randint(0, 10)))
         drawWindow(1)
         #do GPIO commands
         #turn LED on
         #read sensor
                  
def sensorOff():
         text.delete(0.0, END)
         text.insert(END, "Sensor Off")
         drawWindow(0)
         #do GPIO commands
         #turn LED off



drawWindow(1)    
