from tkinter import *

top = Tk()

def doSomething():
        print ("doing something")

b = Button(top, text="Doing something", command=doSomething) 

b.pack()
top.mainloop()
