import bluetooth
import sys
import tkinter as tk
import os
from time import sleep

class HoverButton(tk.Button):
    def __init__(self, master, images,**kw):
        tk.Button.__init__(self,master=master,**kw)
        self.images = images
        self.locked = False
        self.name = self._name
        self.config(image = self.images[0])
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        
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
#region Bluetooth
addr = None

if len(sys.argv) < 2:
    print("No device specified. Searching all nearby bluetooth devices for "
          "the SampleServer service...")
else:
    addr = sys.argv[1]
    print("Searching for SampleServer on {}...".format(addr))

# search for the SampleServer service
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
service_matches = bluetooth.find_service(uuid=uuid, address=addr)

if len(service_matches) == 0:
    print("Couldn't find the SampleServer service.")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"{}\" on {}".format(name, host))

# Create the client socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

# verbindung is aufgebaut
print("Connected. Type something...")
#endregion

#region TKinter initialisieren

#aktuellen pfad finden um den bildordner relativ dazu anzusteuern
filedirectory = os.path.dirname(os.path.abspath(__file__))

#tkinter window erstellen und konfigurieren
window = tk.Tk()
window.title("Virtual Keyboard 64")
window.geometry('1120x350')
window.configure(background='black')
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

#endregion

#region TKinter Buttons erstellen

# Zeile 1 
#Beispiel hoverbutton:
# btn_arrow_left = HoverButton(window, images=pic_arrow_left, image_alt = pic_f1_f2)
# btn_arrow_left.place(x=1, y=10, width=58, height=58)
# btn_arrow_left.bind( "<Button>", lambda x: send("") )
# btn_arrow_left.configure(background='black')
# btn_arrow_left.configure(border=0)

def send(key):
    print(key, "HIGH")
    sleep(0.01)
    print(key, "LOW")
    if btn_shift.locked:
        btn_shift.lock_unlock()
        btn_shift_right.lock_unlock()
        print("51","LOW")

def shift_lock(event):
    btn_shift_lock.locked = not btn_shift_lock.locked
    if btn_shift_lock.locked: sock.send("35","HIGH")
    else: sock.send("35", "LOW")

def shift(event):
    if event.widget.name == "shift":
        btn_shift.locked = not btn_shift.locked
        btn_shift_right.lock_unlock()
    elif event.widget.name == "shift_right":
        btn_shift_right.locked = not btn_shift_right.locked
        btn_shift.lock_unlock()
    if btn_shift.locked: sock.send("51","HIGH")
    else: sock.send("51", "LOW")

def commodore(event):
    btn_commodore.locked = not btn_commodore.locked
    if btn_commodore.locked: sock.send("","HIGH")
    else: sock.send("", "LOW")

btn_arrow_left = HoverButton(window, images=pic_arrow_left)
btn_arrow_left.place(x=4, y=13, width=58, height=58)
btn_arrow_left.bind( "<Button>", lambda x: send("1"))
btn_arrow_left.configure(background='black')
btn_arrow_left.configure(border=0)

btn_one = HoverButton(window, images=pic_one)
btn_one.place(x=63, y=13, width=58, height=58)
btn_one.bind( "<Button>", lambda x: send("2") )
btn_one.configure(background='black')
btn_one.configure(border=0)

btn_two = HoverButton(window, images=pic_two)
btn_two.place(x=123, y=13, width=58, height=58)
btn_two.bind( "<Button>", lambda x: send("3") )
btn_two.configure(background='black')
btn_two.configure(border=0)

btn_three = HoverButton(window, images=pic_three)
btn_three.place(x=183, y=13, width=58, height=58)
btn_three.bind( "<Button>", lambda x: send("4") )
btn_three.configure(background='black')
btn_three.configure(border=0)

btn_four = HoverButton(window, images=pic_four)
btn_four.place(x=243, y=13, width=58, height=58)
btn_four.bind( "<Button>", lambda x: send("5") )
btn_four.configure(background='black')
btn_four.configure(border=0)

btn_five = HoverButton(window, images=pic_five)
btn_five.place(x=303, y=13, width=58, height=58)
btn_five.bind( "<Button>", lambda x: send("6") )
btn_five.configure(background='black')
btn_five.configure(border=0)

btn_six = HoverButton(window, images=pic_six)
btn_six.place(x=363, y=13, width=58, height=58)
btn_six.bind( "<Button>", lambda x: send("7") )
btn_six.configure(background='black')
btn_six.configure(border=0)

btn_seven = HoverButton(window, images=pic_seven)
btn_seven.place(x=423, y=13, width=58, height=58)
btn_seven.bind( "<Button>", lambda x: send("8") )
btn_seven.configure(background='black')
btn_seven.configure(border=0)

btn_eight = HoverButton(window, images=pic_eight)
btn_eight.place(x=483, y=13, width=58, height=58)
btn_eight.bind( "<Button>", lambda x: send("9") )
btn_eight.configure(background='black')
btn_eight.configure(border=0)

btn_nine = HoverButton(window, images=pic_nine)
btn_nine.place(x=543, y=13, width=58, height=58)
btn_nine.bind( "<Button>", lambda x: send("10") )
btn_nine.configure(background='black')
btn_nine.configure(border=0)

btn_zero = HoverButton(window, images=pic_zero)
btn_zero.place(x=603, y=13, width=58, height=58)
btn_zero.bind( "<Button>", lambda x: send("11") )
btn_zero.configure(background='black')
btn_zero.configure(border=0)

btn_plus = HoverButton(window, images=pic_plus)
btn_plus.place(x=663, y=13, width=58, height=58)
btn_plus.bind( "<Button>", lambda x: send("12") )
btn_plus.configure(background='black')
btn_plus.configure(border=0)

btn_minus = HoverButton(window, images=pic_minus)
btn_minus.place(x=723, y=13, width=58, height=58)
btn_minus.bind( "<Button>", lambda x: send("13") )
btn_minus.configure(background='black')
btn_minus.configure(border=0)

btn_pound = HoverButton(window, images=pic_pound)
btn_pound.place(x=783, y=13, width=58, height=58)
btn_pound.bind( "<Button>", lambda x: send("14") )
btn_pound.configure(background='black')
btn_pound.configure(border=0)

btn_home = HoverButton(window, images=pic_home)
btn_home.place(x=843, y=13, width=58, height=58)
btn_home.bind( "<Button>", lambda x: send("15") )
btn_home.configure(background='black')
btn_home.configure(border=0)

btn_del = HoverButton(window, images=pic_del)
btn_del.place(x=903, y=13, width=58, height=58)
btn_del.bind( "<Button>", lambda x: send("16") )
btn_del.configure(background='black')
btn_del.configure(border=0)

btn_f1_f2 = HoverButton(window, images=pic_f1_f2)
btn_f1_f2.place(x=1023, y=13, width=89, height=58)
btn_f1_f2.bind( "<Button>", lambda x: send("17") )
btn_f1_f2.configure(background='black')
btn_f1_f2.configure(border=0)

# Zeile 2

btn_control = HoverButton(window, images=pic_control)
btn_control.place(x=4, y=73, width=89, height=58)
btn_control.bind( "<Button>", lambda x: send("18") )
btn_control.configure(background='black')
btn_control.configure(border=0)

btn_q = HoverButton(window, images=pic_q)
btn_q.place(x=93, y=73, width=58, height=58)
btn_q.bind( "<Button>", lambda x: send("19") )
btn_q.configure(background='black')
btn_q.configure(border=0)

btn_w = HoverButton(window, images=pic_w)
btn_w.place(x=153, y=73, width=58, height=58)
btn_w.bind( "<Button>", lambda x: send("20") )
btn_w.configure(background='black')
btn_w.configure(border=0)

btn_e = HoverButton(window, images=pic_e)
btn_e.place(x=213, y=73, width=58, height=58)
btn_e.bind( "<Button>", lambda x: send("21") )
btn_e.configure(background='black')
btn_e.configure(border=0)

btn_r = HoverButton(window, images=pic_r)
btn_r.place(x=273, y=73, width=58, height=58)
btn_r.bind( "<Button>", lambda x: send("22") )
btn_r.configure(background='black')
btn_r.configure(border=0)

btn_t = HoverButton(window, images=pic_t)
btn_t.place(x=333, y=73, width=58, height=58)
btn_t.bind( "<Button>", lambda x: send("23") )
btn_t.configure(background='black')
btn_t.configure(border=0)

btn_y = HoverButton(window, images=pic_y)
btn_y.place(x=393, y=73, width=58, height=58)
btn_y.bind( "<Button>", lambda x: send("24") )
btn_y.configure(background='black')
btn_y.configure(border=0)

btn_u = HoverButton(window, images=pic_u)
btn_u.place(x=453, y=73, width=58, height=58)
btn_u.bind( "<Button>", lambda x: send("25") )
btn_u.configure(background='black')
btn_u.configure(border=0)

btn_i = HoverButton(window, images=pic_i)
btn_i.place(x=513, y=73, width=58, height=58)
btn_i.bind( "<Button>", lambda x: send("26") )
btn_i.configure(background='black')
btn_i.configure(border=0)

btn_o = HoverButton(window, images=pic_o)
btn_o.place(x=573, y=73, width=58, height=58)
btn_o.bind( "<Button>", lambda x: send("27") )
btn_o.configure(background='black')
btn_o.configure(border=0)

btn_p = HoverButton(window, images=pic_p)
btn_p.place(x=633, y=73, width=58, height=58)
btn_p.bind( "<Button>", lambda x: send("28") )
btn_p.configure(background='black')
btn_p.configure(border=0)


btn_at = HoverButton(window, images=pic_at)
btn_at.place(x=693, y=73, width=58, height=58)
btn_at.bind( "<Button>", lambda x: send("29") )
btn_at.configure(background='black')
btn_at.configure(border=0)

btn_asterisk = HoverButton(window, images=pic_asterisk)
btn_asterisk.place(x=753, y=73, width=58, height=58)
btn_asterisk.bind( "<Button>", lambda x: send("30") )
btn_asterisk.configure(background='black')
btn_asterisk.configure(border=0)

btn_arrow_up = HoverButton(window, images=pic_arrow_up)
btn_arrow_up.place(x=813, y=73, width=58, height=58)
btn_arrow_up.bind( "<Button>", lambda x: send("31") )
btn_arrow_up.configure(background='black')
btn_arrow_up.configure(border=0)

btn_restore = HoverButton(window, images=pic_restore)
btn_restore.place(x=873, y=73, width=89, height=58)
btn_restore.bind( "<Button>", lambda x: send("32") )
btn_restore.configure(background='black')
btn_restore.configure(border=0)

btn_f3_f4 = HoverButton(window, images=pic_f3_f4)
btn_f3_f4.place(x=1023, y=73, width=89, height=58)
btn_f3_f4.bind( "<Button>", lambda x: send("33") )
btn_f3_f4.configure(background='black')
btn_f3_f4.configure(border=0)

# Zeile 3

btn_run_stop = HoverButton(window, images=pic_run_stop)
btn_run_stop.place(x=4, y=133, width=58, height=58)
btn_run_stop.bind( "<Button>", lambda x: send("34") )
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
btn_a.bind( "<Button>", lambda x: send("36") )
btn_a.configure(background='black')
btn_a.configure(border=0)

btn_s = HoverButton(window, images=pic_s)
btn_s.place(x=183, y=133, width=58, height=58)
btn_s.bind( "<Button>", lambda x: send("37") )
btn_s.configure(background='black')
btn_s.configure(border=0)

btn_d = HoverButton(window, images=pic_d)
btn_d.place(x=243, y=133, width=58, height=58)
btn_d.bind( "<Button>", lambda x: send("38") )
btn_d.configure(background='black')
btn_d.configure(border=0)

btn_f = HoverButton(window, images=pic_f)
btn_f.place(x=303, y=133, width=58, height=58)
btn_f.bind( "<Button>", lambda x: send("39") )
btn_f.configure(background='black')
btn_f.configure(border=0)

btn_g = HoverButton(window, images=pic_g)
btn_g.place(x=363, y=133, width=58, height=58)
btn_g.bind( "<Button>", lambda x: send("40") )
btn_g.configure(background='black')
btn_g.configure(border=0)

btn_h = HoverButton(window, images=pic_h)
btn_h.place(x=423, y=133, width=58, height=58)
btn_h.bind( "<Button>", lambda x: send("41") )
btn_h.configure(background='black')
btn_h.configure(border=0)

btn_j = HoverButton(window, images=pic_j)
btn_j.place(x=483, y=133, width=58, height=58)
btn_j.bind( "<Button>", lambda x: send("42") )
btn_j.configure(background='black')
btn_j.configure(border=0)

btn_k = HoverButton(window, images=pic_k)
btn_k.place(x=543, y=133, width=58, height=58)
btn_k.bind( "<Button>", lambda x: send("43") )
btn_k.configure(background='black')
btn_k.configure(border=0)

btn_l = HoverButton(window, images=pic_l)
btn_l.place(x=603, y=133, width=58, height=58)
btn_l.bind( "<Button>", lambda x: send("44") )
btn_l.configure(background='black')
btn_l.configure(border=0)

btn_brace_open = HoverButton(window, images=pic_brace_open)
btn_brace_open.place(x=663, y=133, width=58, height=58)
btn_brace_open.bind( "<Button>", lambda x: send("45") )
btn_brace_open.configure(background='black')
btn_brace_open.configure(border=0)

btn_brace_close = HoverButton(window, images=pic_brace_close)
btn_brace_close.place(x=723, y=133, width=58, height=58)
btn_brace_close.bind( "<Button>", lambda x: send("46") )
btn_brace_close.configure(background='black')
btn_brace_close.configure(border=0)

btn_equal = HoverButton(window, images=pic_equal)
btn_equal.place(x=783, y=133, width=58, height=58)
btn_equal.bind( "<Button>", lambda x: send("47") )
btn_equal.configure(background='black')
btn_equal.configure(border=0)

btn_return = HoverButton(window, images=pic_return)
btn_return.place(x=843, y=133, width=118, height=58)
btn_return.bind( "<Button>", lambda x: send("48") )
btn_return.configure(background='black')
btn_return.configure(border=0)

btn_f5_f6 = HoverButton(window, images=pic_f5_f6)
btn_f5_f6.place(x=1023, y=133, width=89, height=58)
btn_f5_f6.bind( "<Button>", lambda x: send("49") )
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
btn_z.bind( "<Button>", lambda x: send("52") )
btn_z.configure(background='black')
btn_z.configure(border=0)

btn_x = HoverButton(window, images=pic_x)
btn_x.place(x=213, y=193, width=58, height=58)
btn_x.bind( "<Button>", lambda x: send("53") )
btn_x.configure(background='black')
btn_x.configure(border=0)

btn_c = HoverButton(window, images=pic_c)
btn_c.place(x=273, y=193, width=58, height=58)
btn_c.bind( "<Button>", lambda x: send("54") )
btn_c.configure(background='black')
btn_c.configure(border=0)

btn_v = HoverButton(window, images=pic_v)
btn_v.place(x=333, y=193, width=58, height=58)
btn_v.bind( "<Button>", lambda x: send("55") )
btn_v.configure(background='black')
btn_v.configure(border=0)

btn_b = HoverButton(window, images=pic_b)
btn_b.place(x=393, y=193, width=58, height=58)
btn_b.bind( "<Button>", lambda x: send("56") )
btn_b.configure(background='black')
btn_b.configure(border=0)

btn_n = HoverButton(window, images=pic_n)
btn_n.place(x=453, y=193, width=58, height=58)
btn_n.bind( "<Button>", lambda x: send("57") )
btn_n.configure(background='black')
btn_n.configure(border=0)

btn_m = HoverButton(window, images=pic_m)
btn_m.place(x=513, y=193, width=58, height=58)
btn_m.bind( "<Button>", lambda x: send("58") )
btn_m.configure(background='black')
btn_m.configure(border=0)

btn_comma = HoverButton(window, images=pic_comma)
btn_comma.place(x=573, y=193, width=58, height=58)
btn_comma.bind( "<Button>", lambda x: send("59") )
btn_comma.configure(background='black')
btn_comma.configure(border=0)

btn_dot = HoverButton(window, images=pic_dot)
btn_dot.place(x=633, y=193, width=58, height=58)
btn_dot.bind( "<Button>", lambda x: send("60") )
btn_dot.configure(background='black')
btn_dot.configure(border=0)

btn_slash = HoverButton(window, images=pic_slash)
btn_slash.place(x=693, y=193, width=58, height=58)
btn_slash.bind( "<Button>", lambda x: send("61") )
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
btn_cursor_up_down.bind( "<Button>", lambda x: send("63") )
btn_cursor_up_down.configure(background='black')
btn_cursor_up_down.configure(border=0)

btn_cursor_left_right = HoverButton(window, images=pic_cursor_left_right)
btn_cursor_left_right.place(x=903, y=193, width=58, height=58)
btn_cursor_left_right.bind( "<Button>", lambda x: send("64") )
btn_cursor_left_right.configure(background='black')
btn_cursor_left_right.configure(border=0)

btn_f7_f8 = HoverButton(window, images=pic_f7_f8)
btn_f7_f8.place(x=1023, y=193, width=89, height=58)
btn_f7_f8.bind( "<Button>", lambda x: send("65") )
btn_f7_f8.configure(background='black')
btn_f7_f8.configure(border=0)

# SPACE Zeile

btn_space = HoverButton(window, images=pic_space)
btn_space.place(x=173, y=253, width=548, height=58)
btn_space.bind( "<Button>", lambda x: sock.send("66"))
btn_space.configure(background='black')
btn_space.configure(border=0)

#region Extratasten
lbl_freeze = tk.Label(window, text="Freeze", background="red",foreground="black",font='Helvetica 10 bold')
lbl_freeze.place(x=785.5,y=263, width="52", height="20")

btn_freeze = HoverButton(window, images=pic_extra)
btn_freeze.place(x=783, y=283,width=58,height=58)
btn_freeze.bind( "<Button>", lambda x: send("66") )
btn_freeze.configure(background='black')
btn_freeze.configure(border=0)

lbl_menu = tk.Label(window, text="Menu", background="red",foreground="black",font='Helvetica 10 bold')
lbl_menu.place(x=855.5,y=263, width="52", height="20")

btn_menu = HoverButton(window, images=pic_extra)
btn_menu.place(x=853, y=283,width=58,height=58)
btn_menu.bind( "<Button>", lambda x: send("67") )
btn_menu.configure(background='black')
btn_menu.configure(border=0)

lbl_reset = tk.Label(window, text="Reset", background="red",foreground="black",font='Helvetica 10 bold')
lbl_reset.place(x=925.5,y=263, width="52", height="20")

btn_reset = HoverButton(window, images=pic_extra)
btn_reset.place(x=923, y=283,width=58,height=58)
btn_reset.bind( "<Button>", lambda x: send("68") )
btn_reset.configure(background='black')
btn_reset.configure(border=0)

lbl_joystick = tk.Label(window, text="Joystick", background="red",foreground="black",font='Helvetica 10 bold')
lbl_joystick.place(x=995.5,y=263, width="52", height="20")

btn_joystick = HoverButton(window, images=pic_extra)
btn_joystick.place(x=993, y=283,width=58,height=58)
btn_joystick.bind( "<Button>", lambda x: send("69") )
btn_joystick.configure(background='black')
btn_joystick.configure(border=0)
#endregion
#endregion

window.mainloop()

sock.close()
