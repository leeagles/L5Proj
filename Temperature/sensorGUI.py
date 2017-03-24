# import interface code
from tkinter import *
# import random num generator functions
from random import randint
#sensor read
def sensorOn():
         text.delete(0.0, END)
         text.insert(END, str(randint(0, 10)))
         #do GPIO commands
         #turn LED on
         #read sensor
                  
def sensorOff():
         text.delete(0.0, END)
         text.insert(END, "Sensor Off")
         #do GPIO commands
         #turn LED off
         
# start a window
window = Tk()

# add a text area called text
text = Text(window, width=10, height=1, fg="blue", bg="white")

# add a button called ButtonA
buttonA = Button(window, text="Read Sensor", command=sensorOn)
buttonB = Button(window, text="Sensor Off", command=sensorOff)

# use the pack() function to add components to window

text.pack()
buttonA.pack()
buttonB.pack()

