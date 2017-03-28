# import interface code
from tkinter import *
# import random num generator functions
from random import randint
size = 500
# create a window
window = Tk()

def change(event):
         canvas.itemconfig(oval3, state=HIDDEN)

def changeback(event):
         canvas.itemconfig(oval3, state=NORMAL)

def oval3_move(event):
         key = event.keysym
         if key == "Up":
                  canvas.move(oval3, 0, -1)
         elif key == "Down":
                  canvas.move(oval3, 0, 1)

#create a canvas
canvas = Canvas(window, width=size, height=size, bg="lightblue")
# use the pack() function to add components to window
canvas.pack()

rec1=canvas.create_rectangle(100, 100, 300, 200)

rec2=canvas.create_rectangle(30, 30, 80, 80)

oval1=canvas.create_oval(100, 100, 300, 200)

oval2=canvas.create_oval(30, 30, 80, 80)

oval3=canvas.create_oval(200, 30, 80, 80, outline='red', fill='blue')

line1=canvas.create_line(30, 400, 400, 400)


canvas.bind_all('<Button-1>', change)

canvas.bind_all('<Button-3>', changeback)

canvas.bind_all('<Key>', oval3_move)

