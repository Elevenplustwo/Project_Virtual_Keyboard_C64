from tkinter import *

from tkinter.ttk import *

window = Tk()
global Spalte 
global Zeile
global SendByte

Spalte = ["0","0","0","0","0","0","0","0"]
Zeile = ["0","0","0","0","0","0","0","0"]


shift = "AUS"

def toByte(Zeile):
   SendByte = 0
   if Zeile[0] == "X":
      SendByte = SendByte + 1
   if Zeile[1] == "X":
      SendByte = SendByte + 2
   if Zeile[2] == "X":
      SendByte = SendByte + 4
   if Zeile[3] == "X":
      SendByte = SendByte + 8
   if Zeile[4] == "X":
      SendByte = SendByte + 16
   if Zeile[5] == "X":
      SendByte = SendByte + 32
   if Zeile[6] == "X":
      SendByte = SendByte + 64
   if Zeile[7] == "X":
      SendByte = SendByte + 128        
   return SendByte

def send(Spalte, Zeile, shift):

   print("Zeile  :", Zeile)
   print("Spalte :",Spalte)
   print("Byte Zeile:",toByte(Zeile))
   print("Byte Spalte:",toByte(Spalte))

   
   Spalte[1] = "0"
   Spalte[2] = "0"
   Spalte[3] = "0"
   Spalte[4] = "0"
   Spalte[5] = "0"
   Spalte[6] = "0"
   Spalte[7] = "0"
   Spalte[0] = "0"
   Zeile[1] = "0"
   Zeile[2] = "0"
   Zeile[3] = "0"
   Zeile[4] = "0"
   Zeile[5] = "0"
   Zeile[6] = "0"
   Zeile[7] = "0"
   Zeile[0] = "0"   

      

   if shift == "AN":
      shift = "AUS"

   



def mouseClick(event):
   print(event.x)
   print(event.y)

def mouseClick1(event):
   Spalte[7] = "X"
   Zeile[1] = "X"
   send(Spalte, Zeile, shift)

def mouseClick2(event):
   Spalte[1] = "X"
   Zeile[3] = "X"
   send(Spalte, Zeile, shift)



window.title("Virtual Keyboard 64")
window.geometry('1120x340')
window.configure(background='black')
pic1 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Arrow.png")
pic2 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_1.png")
pic3 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_2.png")
pic4 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_3.png")
pic5 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_4.png")
pic6 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_5.png")
pic7 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_6.png")
pic8 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_7.png")
pic9 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_8.png")
pic10 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_9.png")
pic11 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_0.png")
pic12 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Plus.png")
pic13 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Minus.png")
pic14 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Pound.png")
pic15 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Clr_Home.png")
pic16 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Inst_Del.png")
pic17 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_F1.png")

pic21 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Control.png")
pic22 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Q.png")
pic23 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_W.png")
pic24 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_E.png")
pic25 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_R.png")
pic26 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_T.png")
pic27 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Y.png")
pic28 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_U.png")
pic29 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_I.png")
pic30 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_O.png")
pic31 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_P.png")
pic32 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_At.png")
pic33 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Asterisk.png")
pic34 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_ArrowUp.png")
pic35 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Restore.png")
pic36 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_F3.png")

pic40 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Run_Stop.png")
pic41 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Shift_Lock.png")
pic42 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_A.png")
pic43 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_S.png")
pic44 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_D.png")
pic45 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_F.png")
pic46 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_G.png")
pic47 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_H.png")
pic48 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_J.png")
pic49 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_K.png")
pic50 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_L.png")
pic51 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Brace_Open.png")
pic52 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Brace_Close.png")
pic53 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Equal.png")
pic54 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Return.png")
pic55 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_F5.png")

pic60 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Commodore.png")
pic61 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Shift.png")
pic62 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Z.png")
pic63 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_X.png")
pic64 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_C.png")
pic65 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_V.png")
pic66 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_B.png")
pic67 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_N.png")
pic68 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_M.png")
pic69 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Comma.png")
pic70 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Dot.png")
pic71 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Slash.png")
pic72 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Shift.png")
pic73 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Cursor_UpDown.png")
pic74 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Cursor_LeftRight.png")
pic75 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_F7.png")

pic80 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Space_Optimized.png")
pic90 = PhotoImage(file="/home/pi/Documents/VirtualKeyboard64/C64Keys60px/C64_Extratasten.png")

# Zeile 1 

btn1 = Label(window, image=pic1)
btn1.place(x=1, y=10, width=60, height=60)
btn1.bind( "<Button>", mouseClick1 )
btn1.configure(background='black')
btn1.configure(border=0)

btn2 = Label(window, image=pic2)
btn2.place(x=60, y=10, width=60, height=60)
btn2.bind( "<Button>", mouseClick2 )
btn2.configure(background='black')
btn2.configure(border=0)

btn3 = Label(window, image=pic3)
btn3.place(x=120, y=10, width=60, height=60)
btn3.bind( "<Button>", mouseClick )
btn3.configure(background='black')
btn3.configure(border=0)

btn4 = Label(window, image=pic4)
btn4.place(x=180, y=10, width=60, height=60)
btn4.bind( "<Button>", mouseClick )
btn4.configure(background='black')
btn4.configure(border=0)

btn5 = Label(window, image=pic5)
btn5.place(x=240, y=10, width=60, height=60)
btn5.bind( "<Button>", mouseClick )
btn5.configure(background='black')
btn5.configure(border=0)

btn6 = Label(window, image=pic6)
btn6.place(x=300, y=10, width=60, height=60)
btn6.bind( "<Button>", mouseClick )
btn6.configure(background='black')
btn6.configure(border=0)

btn7 = Label(window, image=pic7)
btn7.place(x=360, y=10, width=60, height=60)
btn7.bind( "<Button>", mouseClick )
btn7.configure(background='black')
btn7.configure(border=0)

btn8 = Label(window, image=pic8)
btn8.place(x=420, y=10, width=60, height=60)
btn8.bind( "<Button>", mouseClick )
btn8.configure(background='black')
btn8.configure(border=0)

btn9 = Label(window, image=pic9)
btn9.place(x=480, y=10, width=60, height=60)
btn9.bind( "<Button>", mouseClick )
btn9.configure(background='black')
btn9.configure(border=0)

btn10 = Label(window, image=pic10)
btn10.place(x=540, y=10, width=60, height=60)
btn10.bind( "<Button>", mouseClick )
btn10.configure(background='black')
btn10.configure(border=0)

btn11 = Label(window, image=pic11)
btn11.place(x=600, y=10, width=60, height=60)
btn11.bind( "<Button>", mouseClick )
btn11.configure(background='black')
btn11.configure(border=0)

btn12 = Label(window, image=pic12)
btn12.place(x=660, y=10, width=60, height=60)
btn12.bind( "<Button>", mouseClick )
btn12.configure(background='black')
btn12.configure(border=0)

btn13 = Label(window, image=pic13)
btn13.place(x=720, y=10, width=60, height=60)
btn13.bind( "<Button>", mouseClick )
btn13.configure(background='black')
btn13.configure(border=0)

btn14 = Label(window, image=pic14)
btn14.place(x=780, y=10, width=60, height=60)
btn14.bind( "<Button>", mouseClick )
btn14.configure(background='black')
btn14.configure(border=0)

btn15 = Label(window, image=pic15)
btn15.place(x=840, y=10, width=60, height=60)
btn15.bind( "<Button>", mouseClick )
btn15.configure(background='black')
btn15.configure(border=0)

btn16 = Label(window, image=pic16)
btn16.place(x=900, y=10, width=60, height=60)
btn16.bind( "<Button>", mouseClick )
btn16.configure(background='black')
btn16.configure(border=0)

btn17 = Label(window, image=pic17)
btn17.place(x=1020, y=10, width=120, height=60)
btn17.bind( "<Button>", mouseClick )
btn17.configure(background='black')
btn17.configure(border=0)

# Zeile 2

btn21 = Label(window, image=pic21)
btn21.place(x=1, y=70, width=120, height=60)
btn21.bind( "<Button>", mouseClick )
btn21.configure(background='black')
btn21.configure(border=0)

btn22 = Label(window, image=pic22)
btn22.place(x=90, y=70, width=120, height=60)
btn22.bind( "<Button>", mouseClick )
btn22.configure(background='black')
btn22.configure(border=0)

btn23 = Label(window, image=pic23)
btn23.place(x=150, y=70, width=120, height=60)
btn23.bind( "<Button>", mouseClick )
btn23.configure(background='black')
btn23.configure(border=0)

btn24 = Label(window, image=pic24)
btn24.place(x=210, y=70, width=120, height=60)
btn24.bind( "<Button>", mouseClick )
btn24.configure(background='black')
btn24.configure(border=0)

btn25 = Label(window, image=pic25)
btn25.place(x=270, y=70, width=120, height=60)
btn25.bind( "<Button>", mouseClick )
btn25.configure(background='black')
btn25.configure(border=0)

btn26 = Label(window, image=pic26)
btn26.place(x=330, y=70, width=120, height=60)
btn26.bind( "<Button>", mouseClick )
btn26.configure(background='black')
btn26.configure(border=0)

btn27 = Label(window, image=pic27)
btn27.place(x=390, y=70, width=120, height=60)
btn27.bind( "<Button>", mouseClick )
btn27.configure(background='black')
btn27.configure(border=0)

btn28 = Label(window, image=pic28)
btn28.place(x=450, y=70, width=120, height=60)
btn28.bind( "<Button>", mouseClick )
btn28.configure(background='black')
btn28.configure(border=0)

btn29 = Label(window, image=pic29)
btn29.place(x=510, y=70, width=120, height=60)
btn29.bind( "<Button>", mouseClick )
btn29.configure(background='black')
btn29.configure(border=0)

btn30 = Label(window, image=pic30)
btn30.place(x=570, y=70, width=120, height=60)
btn30.bind( "<Button>", mouseClick )
btn30.configure(background='black')
btn30.configure(border=0)

btn31 = Label(window, image=pic31)
btn31.place(x=630, y=70, width=120, height=60)
btn31.bind( "<Button>", mouseClick )
btn31.configure(background='black')
btn31.configure(border=0)


btn32 = Label(window, image=pic32)
btn32.place(x=690, y=70, width=120, height=60)
btn32.bind( "<Button>", mouseClick )
btn32.configure(background='black')
btn32.configure(border=0)

btn33 = Label(window, image=pic33)
btn33.place(x=750, y=70, width=120, height=60)
btn33.bind( "<Button>", mouseClick )
btn33.configure(background='black')
btn33.configure(border=0)

btn34 = Label(window, image=pic34)
btn34.place(x=810, y=70, width=120, height=60)
btn34.bind( "<Button>", mouseClick )
btn34.configure(background='black')
btn34.configure(border=0)

btn35 = Label(window, image=pic35)
btn35.place(x=870, y=70, width=120, height=60)
btn35.bind( "<Button>", mouseClick )
btn35.configure(background='black')
btn35.configure(border=0)

btn36 = Label(window, image=pic36)
btn36.place(x=1020, y=70, width=120, height=60)
btn36.bind( "<Button>", mouseClick )
btn36.configure(background='black')
btn36.configure(border=0)

# Zeile 3

btn40 = Label(window, image=pic40)
btn40.place(x=1, y=130, width=120, height=60)
btn40.bind( "<Button>", mouseClick )
btn40.configure(background='black')
btn40.configure(border=0)

btn41 = Label(window, image=pic41)
btn41.place(x=60, y=130, width=120, height=60)
btn41.bind( "<Button>", mouseClick )
btn41.configure(background='black')
btn41.configure(border=0)

btn42 = Label(window, image=pic42)
btn42.place(x=120, y=130, width=120, height=60)
btn42.bind( "<Button>", mouseClick )
btn42.configure(background='black')
btn42.configure(border=0)

btn43 = Label(window, image=pic43)
btn43.place(x=180, y=130, width=120, height=60)
btn43.bind( "<Button>", mouseClick )
btn43.configure(background='black')
btn43.configure(border=0)

btn44 = Label(window, image=pic44)
btn44.place(x=240, y=130, width=120, height=60)
btn44.bind( "<Button>", mouseClick )
btn44.configure(background='black')
btn44.configure(border=0)

btn45 = Label(window, image=pic45)
btn45.place(x=300, y=130, width=120, height=60)
btn45.bind( "<Button>", mouseClick )
btn45.configure(background='black')
btn45.configure(border=0)

btn46 = Label(window, image=pic46)
btn46.place(x=360, y=130, width=120, height=60)
btn46.bind( "<Button>", mouseClick )
btn46.configure(background='black')
btn46.configure(border=0)

btn47 = Label(window, image=pic47)
btn47.place(x=420, y=130, width=120, height=60)
btn47.bind( "<Button>", mouseClick )
btn47.configure(background='black')
btn47.configure(border=0)

btn48 = Label(window, image=pic48)
btn48.place(x=480, y=130, width=120, height=60)
btn48.bind( "<Button>", mouseClick )
btn48.configure(background='black')
btn48.configure(border=0)

btn49 = Label(window, image=pic49)
btn49.place(x=540, y=130, width=120, height=60)
btn49.bind( "<Button>", mouseClick )
btn49.configure(background='black')
btn49.configure(border=0)

btn50 = Label(window, image=pic50)
btn50.place(x=600, y=130, width=120, height=60)
btn50.bind( "<Button>", mouseClick )
btn50.configure(background='black')
btn50.configure(border=0)

btn51 = Label(window, image=pic51)
btn51.place(x=660, y=130, width=120, height=60)
btn51.bind( "<Button>", mouseClick )
btn51.configure(background='black')
btn51.configure(border=0)

btn52 = Label(window, image=pic52)
btn52.place(x=720, y=130, width=120, height=60)
btn52.bind( "<Button>", mouseClick )
btn52.configure(background='black')
btn52.configure(border=0)

btn53 = Label(window, image=pic53)
btn53.place(x=780, y=130, width=120, height=60)
btn53.bind( "<Button>", mouseClick )
btn53.configure(background='black')
btn53.configure(border=0)

btn54 = Label(window, image=pic54)
btn54.place(x=840, y=130, width=120, height=60)
btn54.bind( "<Button>", mouseClick )
btn54.configure(background='black')
btn54.configure(border=0)

btn55 = Label(window, image=pic55)
btn55.place(x=1020, y=130, width=120, height=60)
btn55.bind( "<Button>", mouseClick )
btn55.configure(background='black')
btn55.configure(border=0)

# Zeile 4

btn60 = Label(window, image=pic60)
btn60.place(x=1, y=190, width=120, height=60)
btn60.bind( "<Button>", mouseClick )
btn60.configure(background='black')
btn60.configure(border=0)

btn61 = Label(window, image=pic61)
btn61.place(x=60, y=190, width=120, height=60)
btn61.bind( "<Button>", mouseClick )
btn61.configure(background='black')
btn61.configure(border=0)

btn62 = Label(window, image=pic62)
btn62.place(x=150, y=190, width=120, height=60)
btn62.bind( "<Button>", mouseClick )
btn62.configure(background='black')
btn62.configure(border=0)

btn63 = Label(window, image=pic63)
btn63.place(x=210, y=190, width=120, height=60)
btn63.bind( "<Button>", mouseClick )
btn63.configure(background='black')
btn63.configure(border=0)

btn64 = Label(window, image=pic64)
btn64.place(x=270, y=190, width=120, height=60)
btn64.bind( "<Button>", mouseClick )
btn64.configure(background='black')
btn64.configure(border=0)

btn65 = Label(window, image=pic65)
btn65.place(x=330, y=190, width=120, height=60)
btn65.bind( "<Button>", mouseClick )
btn65.configure(background='black')
btn65.configure(border=0)

btn66 = Label(window, image=pic66)
btn66.place(x=390, y=190, width=120, height=60)
btn66.bind( "<Button>", mouseClick )
btn66.configure(background='black')
btn66.configure(border=0)

btn67 = Label(window, image=pic67)
btn67.place(x=450, y=190, width=120, height=60)
btn67.bind( "<Button>", mouseClick )
btn67.configure(background='black')
btn67.configure(border=0)

btn68 = Label(window, image=pic68)
btn68.place(x=510, y=190, width=120, height=60)
btn68.bind( "<Button>", mouseClick )
btn68.configure(background='black')
btn68.configure(border=0)

btn69 = Label(window, image=pic69)
btn69.place(x=570, y=190, width=120, height=60)
btn69.bind( "<Button>", mouseClick )
btn69.configure(background='black')
btn69.configure(border=0)

btn70 = Label(window, image=pic70)
btn70.place(x=630, y=190, width=120, height=60)
btn70.bind( "<Button>", mouseClick )
btn70.configure(background='black')
btn70.configure(border=0)

btn71 = Label(window, image=pic71)
btn71.place(x=690, y=190, width=120, height=60)
btn71.bind( "<Button>", mouseClick )
btn71.configure(background='black')
btn71.configure(border=0)

btn72 = Label(window, image=pic72)
btn72.place(x=750, y=190, width=120, height=60)
btn72.bind( "<Button>", mouseClick )
btn72.configure(background='black')
btn72.configure(border=0)

btn73 = Label(window, image=pic73)
btn73.place(x=840, y=190, width=120, height=60)
btn73.bind( "<Button>", mouseClick )
btn73.configure(background='black')
btn73.configure(border=0)

btn74 = Label(window, image=pic74)
btn74.place(x=900, y=190, width=120, height=60)
btn74.bind( "<Button>", mouseClick )
btn74.configure(background='black')
btn74.configure(border=0)

btn75 = Label(window, image=pic75)
btn75.place(x=1020, y=190, width=120, height=60)
btn75.bind( "<Button>", mouseClick )
btn75.configure(background='black')
btn75.configure(border=0)

# SPACE Zeile

btn80 = Label(window, image=pic80)
btn80.place(x=170, y=250, width=550, height=60)
btn80.bind( "<Button>", mouseClick )
btn80.configure(background='black')
btn80.configure(border=0)

# Extratasten
btn90 = Label(window, image=pic90)
btn90.place(x=780, y=260, width=320, height=74)
btn90.bind( "<Button>", mouseClick )
btn90.configure(background='black')
btn90.configure(border=0)

window.mainloop()

