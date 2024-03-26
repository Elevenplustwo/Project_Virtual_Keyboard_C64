from bluetooth import *
import tkinter as tk
import os
from time import sleep
from math import hypot

class HoverButton(tk.Button):
    def __init__(self, master, images,**kw):
        tk.Button.__init__(self,master=master,**kw)
        self.images = images
        self.locked = False
        self.name = self._name
        self.config(image = self.images[0])
        self.width = 0
        self.height = 0
        self.x = 0
        self.y = 0
        self.center_x = 0
        self.center_y = 0
        self.up = None
        self.right = None
        self.down = None
        self.left = None
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Motion>", self.check_motion)
        self.bind("<Map>", self.map_pos)
    
    def map_pos(self,event):
        self.height = self.winfo_height()
        self.width = self.winfo_width()
        self.x = int(self.place_info()["x"])
        self.y = int(self.place_info()["y"])
        self.center_x = self.x+self.width/2
        self.center_y = self.y+self.height/2
    
    def on_enter(self, e):
        if self.locked: return
        self.config(image = self.images[1])
    
    def on_leave(self, e):
        if self.locked: return
        self.config(image = self.images[0])
    
    def lock_unlock(self):
        self.locked = not self.locked
        if self.locked: self.config(image = self.images[1])
        else: self.config(image = self.images[0])
    
    def check_motion(self,event:tk.Event):
        x = event.x/self.width*100
        y = event.y/self.height*100
        if x<20:
            #mouse_x = self.master.winfo_pointerx() - self.master.winfo_rootx()
            #mouse_y = self.master.winfo_pointery() - self.master.winfo_rooty()
            #self.jump_to_left_button(mouse_x,mouse_y)
            self.master.event_generate("<Motion>",warp=True,x=self.left.center_x,y=self.left.center_y)  
        elif y<20:
            #mouse_x = self.master.winfo_pointerx() - self.master.winfo_rootx()
            #mouse_y = self.master.winfo_pointery() - self.master.winfo_rooty()
            self.master.event_generate("<Motion>",warp=True,x=self.up.center_x,y=self.up.center_y)  
        elif x>80:
            #mouse_x = self.master.winfo_pointerx() - self.master.winfo_rootx()
            #mouse_y = self.master.winfo_pointery() - self.master.winfo_rooty()
            #self.jump_to_right_button(mouse_x,mouse_y)
            self.master.event_generate("<Motion>",warp=True,x=self.right.center_x,y=self.right.center_y)  
        elif y>80:
            #mouse_x = self.master.winfo_pointerx() - self.master.winfo_rootx()
            #mouse_y = self.master.winfo_pointery() - self.master.winfo_rooty()
            #self.jump_to_nearest_button(mouse_x,mouse_y,"DOWN")
            self.master.event_generate("<Motion>",warp=True,x=self.down.center_x,y=self.down.center_y)  
"""
    def jump_to_left_button(self,x,y):
        dist = 1_000_000
        temp_button = None
        for button in self.master.children.values():
            if button is self: continue
            if not type(button) is HoverButton: continue
            if button.center_x>=self.center_x: continue
            temp_dist = hypot(x-button.center_x, y-button.center_y) 
            if temp_dist<dist:
                dist = temp_dist
                temp_button = button
        self.master.event_generate("<Motion>",warp=True,x=temp_button.center_x,y=temp_button.center_y)  

    def jump_to_right_button(self,x,y):
        dist = 1_000_000
        temp_button = None
        for button in self.master.children.values():
            if button is self: continue
            if not type(button) is HoverButton: continue
            if button.center_x<=self.center_x: continue
            temp_dist = hypot(x-button.center_x, y-button.center_y) 
            if temp_dist<dist:
                dist = temp_dist
                temp_button = button
        self.master.event_generate("<Motion>",warp=True,x=temp_button.center_x,y=temp_button.center_y)  

    def jump_to_nearest_button(self,x,y,dir):
        dist = 1_000_000
        temp_button = None
        for button in self.master.children.values():
            if button is self: continue
            if type(button) is HoverButton:
                temp_dist = hypot(x-button.center_x, y-button.center_y) 
                if temp_dist<dist:
                    dist = temp_dist
                    temp_button = button
        self.master.event_generate("<Motion>",warp=True,x=temp_button.center_x,y=temp_button.center_y)
"""
#testklasse wenn bluetooth nicht verfügbar ist, statt über BluetoothSocket.send wird hier einfach geprintet
class s:
    def send(x):
        print(x)

#region Bluetooth

s = BluetoothSocket(RFCOMM)
ssid="00:21:13:05:A1:D3"
s.connect((ssid,1))

#endregion
#region TKinter initialisieren

#aktuellen pfad finden um den bildordner relativ dazu anzusteuern
filedirectory = os.path.dirname(os.path.abspath(__file__))

#tkinter window erstellen und konfigurieren
window = tk.Tk()
window.title("Virtual Keyboard 64")
window.geometry('1120x350')
window.configure(background='black')
#window.configure(cursor="None")
#endregion

#region Bilddateien laden
pic_arrow_left = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Arrow.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Arrow.png"))
pic_one = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_1.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_1.png"))
pic_two = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_2.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_2.png"))
pic_three = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_3.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_3.png"))
pic_four = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_4.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_4.png"))
pic_five = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_5.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_5.png"))
pic_six = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_6.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_6.png"))
pic_seven = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_7.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_7.png"))
pic_eight = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_8.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_8.png"))
pic_nine = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_9.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_9.png"))
pic_zero = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_0.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_0.png"))
pic_plus = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Plus.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Plus.png"))
pic_minus = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Minus.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Minus.png"))
pic_pound = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Pound.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Pound.png"))
pic_home = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Clr_Home.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Clr_Home.png"))
pic_del = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Inst_Del.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Inst_Del.png"))
pic_f1_f2 = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_F1.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_F1.png"))

#pic_one1 = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Control.png")
pic_q = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Q.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Q.png"))
pic_w = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_W.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_W.png"))
pic_e = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_E.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_E.png"))
pic_r = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_R.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_R.png"))
pic_t = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_T.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_T.png"))
pic_y = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Y.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Y.png"))
pic_u = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_U.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_U.png"))
pic_i = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_I.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_I.png"))
pic_o = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_O.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_O.png"))
pic_p = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_P.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_P.png"))
pic_at = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_At.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_At.png"))
pic_asterisk = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Asterisk.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Asterisk.png"))
pic_arrow_up = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_ArrowUp.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_ArrowUp.png"))
pic_control = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Control.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Control.png"))
pic_restore = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Restore.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Restore.png"))
pic_f3_f4 = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_F3.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_F3.png"))

pic_run_stop = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Run_Stop.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Run_Stop.png"))
pic_shift_lock = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Shift_Lock.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Shift_Lock.png"))
pic_a = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_A.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_A.png"))
pic_s = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_S.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_S.png"))
pic_d = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_D.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_D.png"))
pic_f = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_F.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_F.png"))
pic_g = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_G.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_G.png"))
pic_h = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_H.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_H.png"))
pic_j = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_J.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_J.png"))
pic_k = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_K.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_K.png"))
pic_l = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_L.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_L.png"))
pic_brace_open = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Brace_Open.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Brace_Open.png"))
pic_brace_close = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Brace_Close.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Brace_Close.png"))
pic_equal = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Equal.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Equal.png"))
pic_return = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Return.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Return.png"))
pic_f5_f6 = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_F5.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_F5.png"))

pic_commodore = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Commodore.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Commodore.png"))
pic_shift = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Shift.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Shift.png"))
pic_z = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Z.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Z.png"))
pic_x = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_X.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_X.png"))
pic_c = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_C.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_C.png"))
pic_v = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_V.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_V.png"))
pic_b = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_B.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_B.png"))
pic_n = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_N.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_N.png"))
pic_m = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_M.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_M.png"))
pic_comma = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Comma.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Comma.png"))
pic_dot = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Dot.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Dot.png"))
pic_slash = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Slash.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Slash.png"))
pic_cursor_up_down = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Cursor_UpDown.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Cursor_UpDown.png"))
pic_cursor_left_right = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Cursor_LeftRight.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Cursor_LeftRight.png"))
pic_f7_f8 = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_F7.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_F7.png"))

pic_space = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Space_Optimized.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Space_Optimized.png"))
pic_extra = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Extra.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Extra.png"))

pic_joystick = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Joystick.png")
pic_menu = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Menu.png")
pic_freeze = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Freeze.png")
pic_reset = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Reset.png")
#endregion

#region TKinter Buttons erstellen

# Zeile 1 

keyCombo_list = []

def send(event, key):
    if btn_keyCombo.locked:
        if not (event.widget,f"({key},LOW)") in keyCombo_list:
            s.send(f"({key},HIGH)")
            sleep(0.01)
    
            keyCombo_list.append((event.widget,f"({key},LOW)"))
            event.widget.lock_unlock()
    else: 
        s.send(f"({key},HIGH)")
        sleep(0.01)
        s.send(f"({key},LOW)")

    if btn_shift.locked:
        btn_shift.lock_unlock()
        btn_shift_right.lock_unlock()
        s.send("(51,LOW)")

def shift_lock(event):
    btn_shift_lock.locked = not btn_shift_lock.locked
    if btn_shift_lock.locked: s.send("(35,HIGH)")
    else: s.send("(35,LOW)")

def shift(event):
    if event.widget.name == "shift":
        btn_shift.locked = not btn_shift.locked
        btn_shift_right.lock_unlock()
    elif event.widget.name == "shift_right":
        btn_shift_right.locked = not btn_shift_right.locked
        btn_shift.lock_unlock()
    if btn_shift.locked: s.send("(51,HIGH)")
    else: s.send("(51,LOW)")

def commodore(event):
    btn_commodore.locked = not btn_commodore.locked
    if btn_commodore.locked: s.send("(50,HIGH)")
    else: s.send("(50,LOW)")

def keyCombo(event):
    btn_keyCombo.locked = not btn_keyCombo.locked
    if not btn_keyCombo.locked:
        for i in keyCombo_list:
            s.send(i[1])
            i[0].lock_unlock()
        keyCombo_list.clear()
        
btn_arrow_left = HoverButton(window, images=pic_arrow_left)
btn_arrow_left.place(x=4, y=13, width=58, height=58)
btn_arrow_left.bind( "<Button>", lambda x: send(x,"1"))
btn_arrow_left.configure(background='black')
btn_arrow_left.configure(border=0)

btn_one = HoverButton(window, images=pic_one)
btn_one.place(x=63, y=13, width=58, height=58)
btn_one.bind( "<Button>", lambda x: send(x,"2") )
btn_one.configure(background='black')
btn_one.configure(border=0)

btn_two = HoverButton(window, images=pic_two)
btn_two.place(x=123, y=13, width=58, height=58)
btn_two.bind( "<Button>", lambda x: send(x,"3") )
btn_two.configure(background='black')
btn_two.configure(border=0)

btn_three = HoverButton(window, images=pic_three)
btn_three.place(x=183, y=13, width=58, height=58)
btn_three.bind( "<Button>", lambda x: send(x,"4") )
btn_three.configure(background='black')
btn_three.configure(border=0)

btn_four = HoverButton(window, images=pic_four)
btn_four.place(x=243, y=13, width=58, height=58)
btn_four.bind( "<Button>", lambda x: send(x,"5") )
btn_four.configure(background='black')
btn_four.configure(border=0)

btn_five = HoverButton(window, images=pic_five)
btn_five.place(x=303, y=13, width=58, height=58)
btn_five.bind( "<Button>", lambda x: send(x,"6") )
btn_five.configure(background='black')
btn_five.configure(border=0)

btn_six = HoverButton(window, images=pic_six)
btn_six.place(x=363, y=13, width=58, height=58)
btn_six.bind( "<Button>", lambda x: send(x,"7") )
btn_six.configure(background='black')
btn_six.configure(border=0)

btn_seven = HoverButton(window, images=pic_seven)
btn_seven.place(x=423, y=13, width=58, height=58)
btn_seven.bind( "<Button>", lambda x: send(x,"8") )
btn_seven.configure(background='black')
btn_seven.configure(border=0)

btn_eight = HoverButton(window, images=pic_eight)
btn_eight.place(x=483, y=13, width=58, height=58)
btn_eight.bind( "<Button>", lambda x: send(x,"9") )
btn_eight.configure(background='black')
btn_eight.configure(border=0)

btn_nine = HoverButton(window, images=pic_nine)
btn_nine.place(x=543, y=13, width=58, height=58)
btn_nine.bind( "<Button>", lambda x: send(x,"10") )
btn_nine.configure(background='black')
btn_nine.configure(border=0)

btn_zero = HoverButton(window, images=pic_zero)
btn_zero.place(x=603, y=13, width=58, height=58)
btn_zero.bind( "<Button>", lambda x: send(x,"11") )
btn_zero.configure(background='black')
btn_zero.configure(border=0)

btn_plus = HoverButton(window, images=pic_plus)
btn_plus.place(x=663, y=13, width=58, height=58)
btn_plus.bind( "<Button>", lambda x: send(x,"12") )
btn_plus.configure(background='black')
btn_plus.configure(border=0)

btn_minus = HoverButton(window, images=pic_minus)
btn_minus.place(x=723, y=13, width=58, height=58)
btn_minus.bind( "<Button>", lambda x: send(x,"13") )
btn_minus.configure(background='black')
btn_minus.configure(border=0)

btn_pound = HoverButton(window, images=pic_pound)
btn_pound.place(x=783, y=13, width=58, height=58)
btn_pound.bind( "<Button>", lambda x: send(x,"14") )
btn_pound.configure(background='black')
btn_pound.configure(border=0)

btn_home = HoverButton(window, images=pic_home)
btn_home.place(x=843, y=13, width=58, height=58)
btn_home.bind( "<Button>", lambda x: send(x,"15") )
btn_home.configure(background='black')
btn_home.configure(border=0)

btn_del = HoverButton(window, images=pic_del)
btn_del.place(x=903, y=13, width=58, height=58)
btn_del.bind( "<Button>", lambda x: send(x,"16") )
btn_del.configure(background='black')
btn_del.configure(border=0)

btn_f1_f2 = HoverButton(window, images=pic_f1_f2)
btn_f1_f2.place(x=1023, y=13, width=89, height=58)
btn_f1_f2.bind( "<Button>", lambda x: send(x,"17") )
btn_f1_f2.configure(background='black')
btn_f1_f2.configure(border=0)

# Zeile 2

btn_control = HoverButton(window, images=pic_control)
btn_control.place(x=4, y=73, width=89, height=58)
btn_control.bind( "<Button>", lambda x: send(x,"18") )
btn_control.configure(background='black')
btn_control.configure(border=0)

btn_q = HoverButton(window, images=pic_q)
btn_q.place(x=93, y=73, width=58, height=58)
btn_q.bind( "<Button>", lambda x: send(x,"19") )
btn_q.configure(background='black')
btn_q.configure(border=0)

btn_w = HoverButton(window, images=pic_w)
btn_w.place(x=153, y=73, width=58, height=58)
btn_w.bind( "<Button>", lambda x: send(x,"20") )
btn_w.configure(background='black')
btn_w.configure(border=0)

btn_e = HoverButton(window, images=pic_e)
btn_e.place(x=213, y=73, width=58, height=58)
btn_e.bind( "<Button>", lambda x: send(x,"21") )
btn_e.configure(background='black')
btn_e.configure(border=0)

btn_r = HoverButton(window, images=pic_r)
btn_r.place(x=273, y=73, width=58, height=58)
btn_r.bind( "<Button>", lambda x: send(x,"22") )
btn_r.configure(background='black')
btn_r.configure(border=0)

btn_t = HoverButton(window, images=pic_t)
btn_t.place(x=333, y=73, width=58, height=58)
btn_t.bind( "<Button>", lambda x: send(x,"23") )
btn_t.configure(background='black')
btn_t.configure(border=0)

btn_y = HoverButton(window, images=pic_y)
btn_y.place(x=393, y=73, width=58, height=58)
btn_y.bind( "<Button>", lambda x: send(x,"24") )
btn_y.configure(background='black')
btn_y.configure(border=0)

btn_u = HoverButton(window, images=pic_u)
btn_u.place(x=453, y=73, width=58, height=58)
btn_u.bind( "<Button>", lambda x: send(x,"25") )
btn_u.configure(background='black')
btn_u.configure(border=0)

btn_i = HoverButton(window, images=pic_i)
btn_i.place(x=513, y=73, width=58, height=58)
btn_i.bind( "<Button>", lambda x: send(x,"26") )
btn_i.configure(background='black')
btn_i.configure(border=0)

btn_o = HoverButton(window, images=pic_o)
btn_o.place(x=573, y=73, width=58, height=58)
btn_o.bind( "<Button>", lambda x: send(x,"27") )
btn_o.configure(background='black')
btn_o.configure(border=0)

btn_p = HoverButton(window, images=pic_p)
btn_p.place(x=633, y=73, width=58, height=58)
btn_p.bind( "<Button>", lambda x: send(x,"28") )
btn_p.configure(background='black')
btn_p.configure(border=0)

btn_at = HoverButton(window, images=pic_at)
btn_at.place(x=693, y=73, width=58, height=58)
btn_at.bind( "<Button>", lambda x: send(x,"29") )
btn_at.configure(background='black')
btn_at.configure(border=0)

btn_asterisk = HoverButton(window, images=pic_asterisk)
btn_asterisk.place(x=753, y=73, width=58, height=58)
btn_asterisk.bind( "<Button>", lambda x: send(x,"30") )
btn_asterisk.configure(background='black')
btn_asterisk.configure(border=0)

btn_arrow_up = HoverButton(window, images=pic_arrow_up)
btn_arrow_up.place(x=813, y=73, width=58, height=58)
btn_arrow_up.bind( "<Button>", lambda x: send(x,"31") )
btn_arrow_up.configure(background='black')
btn_arrow_up.configure(border=0)

btn_restore = HoverButton(window, images=pic_restore)
btn_restore.place(x=873, y=73, width=89, height=58)
btn_restore.bind( "<Button>", lambda x: send(x,"32") )
btn_restore.configure(background='black')
btn_restore.configure(border=0)

btn_f3_f4 = HoverButton(window, images=pic_f3_f4)
btn_f3_f4.place(x=1023, y=73, width=89, height=58)
btn_f3_f4.bind( "<Button>", lambda x: send(x,"33") )
btn_f3_f4.configure(background='black')
btn_f3_f4.configure(border=0)

# Zeile 3

btn_run_stop = HoverButton(window, images=pic_run_stop)
btn_run_stop.place(x=4, y=133, width=58, height=58)
btn_run_stop.bind( "<Button>", lambda x: send(x,"34") )
btn_run_stop.configure(background='black')
btn_run_stop.configure(border=0)

#shift lock sendet 35
btn_shift_lock = HoverButton(window, images=pic_shift_lock)
btn_shift_lock.place(x=63, y=133, width=58, height=58)
btn_shift_lock.bind( "<Button>", shift_lock)
btn_shift_lock.configure(background='black')
btn_shift_lock.configure(border=0)

btn_a = HoverButton(window, images=pic_a)
btn_a.place(x=123, y=133, width=58, height=58)
btn_a.bind( "<Button>", lambda x: send(x,"36") )
btn_a.configure(background='black')
btn_a.configure(border=0)

btn_s = HoverButton(window, images=pic_s)
btn_s.place(x=183, y=133, width=58, height=58)
btn_s.bind( "<Button>", lambda x: send(x,"37") )
btn_s.configure(background='black')
btn_s.configure(border=0)

btn_d = HoverButton(window, images=pic_d)
btn_d.place(x=243, y=133, width=58, height=58)
btn_d.bind( "<Button>", lambda x: send(x,"38") )
btn_d.configure(background='black')
btn_d.configure(border=0)

btn_f = HoverButton(window, images=pic_f)
btn_f.place(x=303, y=133, width=58, height=58)
btn_f.bind( "<Button>", lambda x: send(x,"39") )
btn_f.configure(background='black')
btn_f.configure(border=0)

btn_g = HoverButton(window, images=pic_g)
btn_g.place(x=363, y=133, width=58, height=58)
btn_g.bind( "<Button>", lambda x: send(x,"40") )
btn_g.configure(background='black')
btn_g.configure(border=0)

btn_h = HoverButton(window, images=pic_h)
btn_h.place(x=423, y=133, width=58, height=58)
btn_h.bind( "<Button>", lambda x: send(x,"41") )
btn_h.configure(background='black')
btn_h.configure(border=0)

btn_j = HoverButton(window, images=pic_j)
btn_j.place(x=483, y=133, width=58, height=58)
btn_j.bind( "<Button>", lambda x: send(x,"42") )
btn_j.configure(background='black')
btn_j.configure(border=0)

btn_k = HoverButton(window, images=pic_k)
btn_k.place(x=543, y=133, width=58, height=58)
btn_k.bind( "<Button>", lambda x: send(x,"43") )
btn_k.configure(background='black')
btn_k.configure(border=0)

btn_l = HoverButton(window, images=pic_l)
btn_l.place(x=603, y=133, width=58, height=58)
btn_l.bind( "<Button>", lambda x: send(x,"44") )
btn_l.configure(background='black')
btn_l.configure(border=0)

btn_brace_open = HoverButton(window, images=pic_brace_open)
btn_brace_open.place(x=663, y=133, width=58, height=58)
btn_brace_open.bind( "<Button>", lambda x: send(x,"45") )
btn_brace_open.configure(background='black')
btn_brace_open.configure(border=0)

btn_brace_close = HoverButton(window, images=pic_brace_close)
btn_brace_close.place(x=723, y=133, width=58, height=58)
btn_brace_close.bind( "<Button>", lambda x: send(x,"46") )
btn_brace_close.configure(background='black')
btn_brace_close.configure(border=0)

btn_equal = HoverButton(window, images=pic_equal)
btn_equal.place(x=783, y=133, width=58, height=58)
btn_equal.bind( "<Button>", lambda x: send(x,"47") )
btn_equal.configure(background='black')
btn_equal.configure(border=0)

btn_return = HoverButton(window, images=pic_return)
btn_return.place(x=843, y=133, width=118, height=58)
btn_return.bind( "<Button>", lambda x: send(x,"48") )
btn_return.configure(background='black')
btn_return.configure(border=0)

btn_f5_f6 = HoverButton(window, images=pic_f5_f6)
btn_f5_f6.place(x=1023, y=133, width=89, height=58)
btn_f5_f6.bind( "<Button>", lambda x: send(x,"49") )
btn_f5_f6.configure(background='black')
btn_f5_f6.configure(border=0)

# Zeile 4
#commodore sendet 50
btn_commodore = HoverButton(window, images=pic_commodore)
btn_commodore.place(x=4, y=193, width=58, height=58)
btn_commodore.bind( "<Button>", commodore )
btn_commodore.configure(background='black')
btn_commodore.configure(border=0)

#shift sendet 51
btn_shift = HoverButton(window, images=pic_shift)
btn_shift.place(x=63, y=193, width=89, height=58)
btn_shift.bind( "<Button>", shift )
btn_shift.configure(background='black')
btn_shift.configure(border=0)
btn_shift.name = "shift"

btn_z = HoverButton(window, images=pic_z)
btn_z.place(x=153, y=193, width=58, height=58)
btn_z.bind( "<Button>", lambda x: send(x,"52") )
btn_z.configure(background='black')
btn_z.configure(border=0)

btn_x = HoverButton(window, images=pic_x)
btn_x.place(x=213, y=193, width=58, height=58)
btn_x.bind( "<Button>", lambda x: send(x,"53") )
btn_x.configure(background='black')
btn_x.configure(border=0)

btn_c = HoverButton(window, images=pic_c)
btn_c.place(x=273, y=193, width=58, height=58)
btn_c.bind( "<Button>", lambda x: send(x,"54") )
btn_c.configure(background='black')
btn_c.configure(border=0)

btn_v = HoverButton(window, images=pic_v)
btn_v.place(x=333, y=193, width=58, height=58)
btn_v.bind( "<Button>", lambda x: send(x,"55") )
btn_v.configure(background='black')
btn_v.configure(border=0)

btn_b = HoverButton(window, images=pic_b)
btn_b.place(x=393, y=193, width=58, height=58)
btn_b.bind( "<Button>", lambda x: send(x,"56") )
btn_b.configure(background='black')
btn_b.configure(border=0)

btn_n = HoverButton(window, images=pic_n)
btn_n.place(x=453, y=193, width=58, height=58)
btn_n.bind( "<Button>", lambda x: send(x,"57") )
btn_n.configure(background='black')
btn_n.configure(border=0)

btn_m = HoverButton(window, images=pic_m)
btn_m.place(x=513, y=193, width=58, height=58)
btn_m.bind( "<Button>", lambda x: send(x,"58") )
btn_m.configure(background='black')
btn_m.configure(border=0)

btn_comma = HoverButton(window, images=pic_comma)
btn_comma.place(x=573, y=193, width=58, height=58)
btn_comma.bind( "<Button>", lambda x: send(x,"59") )
btn_comma.configure(background='black')
btn_comma.configure(border=0)

btn_dot = HoverButton(window, images=pic_dot)
btn_dot.place(x=633, y=193, width=58, height=58)
btn_dot.bind( "<Button>", lambda x: send(x,"60") )
btn_dot.configure(background='black')
btn_dot.configure(border=0)

btn_slash = HoverButton(window, images=pic_slash)
btn_slash.place(x=693, y=193, width=58, height=58)
btn_slash.bind( "<Button>", lambda x: send(x,"61") )
btn_slash.configure(background='black')
btn_slash.configure(border=0)

#shift rechts sendet 62
btn_shift_right = HoverButton(window, images=pic_shift)
btn_shift_right.place(x=753, y=193, width=89, height=58)
btn_shift_right.bind( "<Button>", shift )
btn_shift_right.configure(background='black')
btn_shift_right.configure(border=0)
btn_shift_right.name = "shift_right"

btn_cursor_up_down = HoverButton(window, images=pic_cursor_up_down)
btn_cursor_up_down.place(x=843, y=193, width=58, height=58)
btn_cursor_up_down.bind( "<Button>", lambda x: send(x,"63") )
btn_cursor_up_down.configure(background='black')
btn_cursor_up_down.configure(border=0)

btn_cursor_left_right = HoverButton(window, images=pic_cursor_left_right)
btn_cursor_left_right.place(x=903, y=193, width=58, height=58)
btn_cursor_left_right.bind( "<Button>", lambda x: send(x,"64") )
btn_cursor_left_right.configure(background='black')
btn_cursor_left_right.configure(border=0)

btn_f7_f8 = HoverButton(window, images=pic_f7_f8)
btn_f7_f8.place(x=1023, y=193, width=89, height=58)
btn_f7_f8.bind( "<Button>", lambda x: send(x,"65") )
btn_f7_f8.configure(background='black')
btn_f7_f8.configure(border=0)

# SPACE Zeile

btn_space = HoverButton(window, images=pic_space)
btn_space.place(x=173, y=253, width=548, height=58)
btn_space.bind( "<Button>", lambda x: send(x,"66"))
btn_space.configure(background='black')
btn_space.configure(border=0)

#region Extratasten
lbl_freeze = tk.Label(window, image=pic_freeze)
lbl_freeze.place(x=785.5,y=263)
lbl_freeze.configure(border=0)

btn_freeze = HoverButton(window, images=pic_extra)
btn_freeze.place(x=802, y=292,width=48,height=35)
btn_freeze.bind( "<Button>", lambda x: send(x,"67") )
btn_freeze.configure(background='black')
btn_freeze.configure(border=0)

lbl_menu = tk.Label(window, image=pic_menu)
lbl_menu.place(x=870.5,y=263)
lbl_menu.configure(border=0)

btn_menu = HoverButton(window, images=pic_extra)
btn_menu.place(x=873, y=292,width=48,height=35)
btn_menu.bind( "<Button>", lambda x: send(x,"68") )
btn_menu.configure(background='black')
btn_menu.configure(border=0)

lbl_reset = tk.Label(window, image=pic_reset)
lbl_reset.place(x=933.5,y=263)
lbl_reset.configure(border=0)

btn_reset = HoverButton(window, images=pic_extra)
btn_reset.place(x=941, y=292,width=48,height=35)
btn_reset.bind( "<Button>", lambda x: send(x,"69") )
btn_reset.configure(background='black')
btn_reset.configure(border=0)

lbl_joystick = tk.Label(window, image=pic_joystick)
lbl_joystick.place(x=1007,y=263)
lbl_joystick.configure(border=0)

btn_joystick = HoverButton(window, images=pic_extra)
btn_joystick.place(x=1011, y=292,width=48,height=35)
btn_joystick.bind( "<Button>", lambda x: send(x,"70") )
btn_joystick.configure(background='black')
btn_joystick.configure(border=0)

lbl_keyCombo = tk.Label(window, text="KEYCOMBO", background="red4",foreground="white",font='Helvetica 10 bold')
lbl_keyCombo.place(x=52,y=263, width="80", height="22")

btn_keyCombo = HoverButton(window, images=pic_extra)
btn_keyCombo.place(x=65, y=292,width=48,height=35)
btn_keyCombo.bind( "<Button>", keyCombo)
btn_keyCombo.configure(background='black')
btn_keyCombo.configure(border=0)

#endregion
#endregion

#region directions

#line 1
btn_space.up = btn_b
btn_space.left = btn_keyCombo
btn_space.right = btn_freeze
btn_space.down = btn_seven

btn_arrow_left.up = btn_keyCombo
btn_arrow_left.left = btn_f1_f2
btn_arrow_left.right = btn_one
btn_arrow_left.down = btn_control

btn_one.up = btn_keyCombo
btn_one.left = btn_arrow_left
btn_one.right = btn_two
btn_one.down = btn_q

btn_two.up = btn_keyCombo
btn_two.left = btn_one
btn_two.right = btn_three
btn_two.down = btn_w

btn_three.up = btn_space
btn_three.left = btn_two
btn_three.right = btn_four
btn_three.down = btn_e

btn_four.up = btn_space
btn_four.left = btn_three
btn_four.right = btn_five
btn_four.down = btn_r

btn_five.up = btn_space
btn_five.left = btn_four
btn_five.right = btn_six
btn_five.down = btn_t

btn_six.up = btn_space
btn_six.left = btn_five
btn_six.right = btn_seven
btn_six.down = btn_y

btn_seven.up = btn_space
btn_seven.left = btn_six
btn_seven.right = btn_eight
btn_seven.down = btn_u

btn_eight.up = btn_space
btn_eight.left = btn_seven
btn_eight.right = btn_nine
btn_eight.down = btn_i

btn_nine.up = btn_space
btn_nine.left = btn_eight
btn_nine.right = btn_zero
btn_nine.down = btn_o

btn_zero.up = btn_space
btn_zero.left = btn_nine
btn_zero.right = btn_plus
btn_zero.down = btn_p

btn_plus.up = btn_space
btn_plus.left = btn_zero
btn_plus.right = btn_minus
btn_plus.down = btn_at

btn_minus.up = btn_freeze
btn_minus.left = btn_plus
btn_minus.right = btn_pound
btn_minus.down = btn_asterisk

btn_pound.up = btn_freeze
btn_pound.left = btn_minus
btn_pound.right = btn_home
btn_pound.down = btn_arrow_up

btn_home.up = btn_menu
btn_home.left = btn_pound
btn_home.right = btn_del
btn_home.down = btn_restore

btn_del.up = btn_reset
btn_del.left = btn_home
btn_del.right = btn_f1_f2
btn_del.down = btn_restore

btn_f1_f2.up = btn_joystick
btn_f1_f2.left = btn_del
btn_f1_f2.right = btn_arrow_left
btn_f1_f2.down = btn_f3_f4

#line 2
btn_control.up = btn_arrow_left
btn_control.left = btn_f3_f4
btn_control.right = btn_q
btn_control.down = btn_run_stop

btn_q.up = btn_one
btn_q.left = btn_control
btn_q.right = btn_w
btn_q.down = btn_shift_lock

btn_w.up = btn_two
btn_w.left = btn_q
btn_w.right = btn_e
btn_w.down = btn_a

btn_e.up = btn_three
btn_e.left = btn_w
btn_e.right = btn_r
btn_e.down = btn_s

btn_r.up = btn_four
btn_r.left = btn_e
btn_r.right = btn_t
btn_r.down = btn_d

btn_t.up = btn_five
btn_t.left = btn_r
btn_t.right = btn_y
btn_t.down = btn_f

btn_y.up = btn_six
btn_y.left = btn_t
btn_y.right = btn_u
btn_y.down = btn_g

btn_u.up = btn_seven
btn_u.left = btn_y
btn_u.right = btn_i
btn_u.down = btn_h

btn_i.up = btn_eight
btn_i.left = btn_u
btn_i.right = btn_o
btn_i.down = btn_j

btn_o.up = btn_nine
btn_o.left = btn_i
btn_o.right = btn_p
btn_o.down = btn_k

btn_p.up = btn_zero
btn_p.left = btn_o
btn_p.right = btn_at
btn_p.down = btn_l

btn_at.up = btn_plus
btn_at.left = btn_p
btn_at.right = btn_asterisk
btn_at.down = btn_brace_open

btn_asterisk.up = btn_minus
btn_asterisk.left = btn_at
btn_asterisk.right = btn_arrow_up
btn_asterisk.down = btn_brace_close

btn_arrow_up.up = btn_pound
btn_arrow_up.left = btn_asterisk
btn_arrow_up.right = btn_restore
btn_arrow_up.down = btn_equal

btn_restore.up = btn_del
btn_restore.left = btn_arrow_up
btn_restore.right = btn_f3_f4
btn_restore.down = btn_return

btn_f3_f4.up = btn_f1_f2
btn_f3_f4.left = btn_restore
btn_f3_f4.right = btn_control
btn_f3_f4.down = btn_f5_f6

#line 3
btn_run_stop.up = btn_control
btn_run_stop.left = btn_f5_f6
btn_run_stop.right = btn_shift_lock
btn_run_stop.down = btn_commodore

btn_shift_lock.up = btn_q
btn_shift_lock.left = btn_run_stop
btn_shift_lock.right = btn_a
btn_shift_lock.down = btn_shift

btn_a.up = btn_w
btn_a.left = btn_shift_lock
btn_a.right = btn_s
btn_a.down = btn_z

btn_s.up = btn_e
btn_s.left = btn_a
btn_s.right = btn_d
btn_s.down = btn_x

btn_d.up = btn_r
btn_d.left = btn_s
btn_d.right = btn_f
btn_d.down = btn_c

btn_f.up = btn_t
btn_f.left = btn_d
btn_f.right = btn_g
btn_f.down = btn_v

btn_g.up = btn_y
btn_g.left = btn_f
btn_g.right = btn_h
btn_g.down = btn_b

btn_h.up = btn_u
btn_h.left = btn_g
btn_h.right = btn_j
btn_h.down = btn_n

btn_j.up = btn_i
btn_j.left = btn_h
btn_j.right = btn_k
btn_j.down = btn_m

btn_k.up = btn_o
btn_k.left = btn_j
btn_k.right = btn_l
btn_k.down = btn_comma

btn_l.up = btn_p
btn_l.left = btn_k
btn_l.right = btn_brace_open
btn_l.down = btn_dot

btn_brace_open.up = btn_at
btn_brace_open.left = btn_l
btn_brace_open.right = btn_brace_close
btn_brace_open.down = btn_slash

btn_brace_close.up = btn_asterisk
btn_brace_close.left = btn_brace_open
btn_brace_close.right = btn_equal
btn_brace_close.down = btn_shift_right

btn_equal.up = btn_arrow_up
btn_equal.left = btn_brace_close
btn_equal.right = btn_return
btn_equal.down = btn_cursor_up_down

btn_return.up = btn_restore
btn_return.left = btn_equal
btn_return.right = btn_f5_f6
btn_return.down = btn_cursor_left_right

btn_f5_f6.up = btn_f3_f4
btn_f5_f6.left = btn_return
btn_f5_f6.right = btn_run_stop
btn_f5_f6.down = btn_f7_f8

#line 4
btn_commodore.up = btn_run_stop
btn_commodore.left = btn_f7_f8
btn_commodore.right = btn_shift
btn_commodore.down = btn_keyCombo

btn_shift.up = btn_shift_lock
btn_shift.left = btn_commodore
btn_shift.right = btn_z
btn_shift.down = btn_keyCombo

btn_z.up = btn_a
btn_z.left = btn_shift
btn_z.right = btn_x
btn_z.down = btn_space

btn_x.up = btn_s
btn_x.left = btn_z
btn_x.right = btn_c
btn_x.down = btn_space

btn_c.up = btn_d
btn_c.left = btn_x
btn_c.right = btn_v
btn_c.down = btn_space

btn_v.up = btn_f
btn_v.left = btn_c
btn_v.right = btn_b
btn_v.down = btn_space

btn_b.up = btn_g
btn_b.left = btn_v
btn_b.right = btn_n
btn_b.down = btn_space

btn_n.up = btn_h
btn_n.left = btn_b
btn_n.right = btn_m
btn_n.down = btn_space

btn_m.up = btn_j
btn_m.left = btn_n
btn_m.right = btn_comma
btn_m.down = btn_space

btn_comma.up = btn_k
btn_comma.left = btn_m
btn_comma.right = btn_dot
btn_comma.down = btn_space

btn_dot.up = btn_l
btn_dot.left = btn_comma
btn_dot.right = btn_slash
btn_dot.down = btn_space

btn_slash.up = btn_brace_open
btn_slash.left = btn_dot
btn_slash.right = btn_shift_right
btn_slash.down = btn_space

btn_shift_right.up = btn_brace_close
btn_shift_right.left = btn_slash
btn_shift_right.right = btn_cursor_up_down
btn_shift_right.down = btn_freeze

"""
FRAGE WEGEN CURSOR LEFT RIGHT UP DOWN ETC
"""

btn_cursor_up_down.up = btn_return
btn_cursor_up_down.left = btn_shift_right
btn_cursor_up_down.right = btn_cursor_left_right
btn_cursor_up_down.down = btn_menu

btn_cursor_left_right.up = btn_return
btn_cursor_left_right.left = btn_cursor_up_down
btn_cursor_left_right.right = btn_f7_f8
btn_cursor_left_right.down = btn_reset

btn_f7_f8.up = btn_f5_f6
btn_f7_f8.left = btn_cursor_left_right
btn_f7_f8.right = btn_commodore
btn_f7_f8.down = btn_joystick

#line 5
btn_keyCombo.up = btn_shift
btn_keyCombo.left = btn_joystick
btn_keyCombo.right = btn_space
btn_keyCombo.down = btn_one

btn_space.up = btn_b
btn_space.left =btn_keyCombo
btn_space.right = btn_freeze
btn_space.down = btn_seven

btn_freeze.up = btn_shift_right
btn_freeze.left = btn_space
btn_freeze.right = btn_menu
btn_freeze.down = btn_pound

btn_menu.up = btn_cursor_up_down
btn_menu.left = btn_freeze
btn_menu.right = btn_reset
btn_menu.down = btn_home

btn_reset.up = btn_cursor_left_right
btn_reset.left = btn_menu
btn_reset.right = btn_joystick
btn_reset.down = btn_del

btn_joystick.up = btn_f7_f8
btn_joystick.left = btn_reset
btn_joystick.right = btn_keyCombo
btn_joystick.down = btn_f1_f2



#endregion

window.mainloop()

#s.close() #<- bluetooth
