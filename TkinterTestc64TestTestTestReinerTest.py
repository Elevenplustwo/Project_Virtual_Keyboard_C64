#GUI - DO
from tkinter import *
def do_something(buchstabe):
    print('hat geklappt', buchstabe)


window = Tk()
                  #defines a button. "window" means
                  #put the button the window, and
                  #"text=" means what the button
                  #should say

img = PhotoImage(file="C:\\temp\\Stick Entleerung\\pics entleerung plus\\Button_A.png", width=100, height=100)
#Button Nr1

buttonA = Button(window, text='A', command= lambda: do_something("A"), image=img)
buttonA.pack()#tells the button to go on the window

#Button Nr2

buttonB = Button(window, text='B', command= lambda: do_something("B"))
buttonB.pack()#tells the button to go on the window

window.mainloop()





"""
root = Tk()
lbl = Label(root, text="Hello")
lbl.grid(column=0, row=0)
w1 = Label(root, text="Und hier könnte Ihre Werbung stehen").grid(column=1, row=0) 
labeltext = Label(root,
           justify=LEFT,
           padx = 10,
           text="irgendeinstring").grid(column=2, row=0)
root.mainloop()
"""