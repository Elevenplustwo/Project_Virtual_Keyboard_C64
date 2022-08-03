from tkinter import *
from tkinter.ttk import *


window = Tk()

window.title("Virtual Keyboard 64")
window.geometry('1180x300')
photo1 = PhotoImage(file = "/home/pi/Documents/VirtualKeyboard64/C64_1.png")

btn1 = Button(window, image=photo1)
btn1.place(x=10, y=10, width=170, height=170)
btn2 = Button(window, image=photo1)
btn2.place(x=190, y=10, width=170, height=170)






window.mainloop()
