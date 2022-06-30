import bluetooth
import sys
import tkinter as tk

import tkinter.ttk as ttk

import os

class HoverButton(tk.Button):
    def __init__(self, master, image_alt, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["foreground"]
        self.image = self["image"]
        self.image_alt = image_alt
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self.config(image = self.image_alt)

    def on_leave(self, e):
        self.config(image = self.image)

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

#verbindung is aufgebaut
print("Connected. Type something...")




#aktuellen pfad finden um den bildordner relativ dazu anzusteuern
filedirectory = os.path.dirname(os.path.abspath(__file__))

#tkinter window erstellen und konfigurieren
window = tk.Tk()
window.title("Virtual Keyboard 64")
window.geometry('1120x340')
window.configure(background='black')

#region Bilddateien laden
pic_arrow_left = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Arrow.png")
pic_one = tk.PhotoImage(file=f"{filedirectory}/Img/C64_1.png")
pic_two = tk.PhotoImage(file=f"{filedirectory}/Img/C64_2.png")
pic_three = tk.PhotoImage(file=f"{filedirectory}/Img/C64_3.png")
pic_four = tk.PhotoImage(file=f"{filedirectory}/Img/C64_4.png")
pic_five = tk.PhotoImage(file=f"{filedirectory}/Img/C64_5.png")
pic_six = tk.PhotoImage(file=f"{filedirectory}/Img/C64_6.png")
pic_seven = tk.PhotoImage(file=f"{filedirectory}/Img/C64_7.png")
pic_eight = tk.PhotoImage(file=f"{filedirectory}/Img/C64_8.png")
pic_nine = tk.PhotoImage(file=f"{filedirectory}/Img/C64_9.png")
pic_zero = tk.PhotoImage(file=f"{filedirectory}/Img/C64_0.png")
pic_plus = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Plus.png")
pic_minus = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Minus.png")
pic_pound = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Pound.png")
pic_home = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Clr_Home.png")
pic_del = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Inst_Del.png")
pic_f1_f2 = tk.PhotoImage(file=f"{filedirectory}/Img/C64_F1.png")

#pic_one1 = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Control.png")
pic_q = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Q.png")
pic_w = tk.PhotoImage(file=f"{filedirectory}/Img/C64_W.png")
pic_e = tk.PhotoImage(file=f"{filedirectory}/Img/C64_E.png")
pic_r = tk.PhotoImage(file=f"{filedirectory}/Img/C64_R.png")
pic_t = tk.PhotoImage(file=f"{filedirectory}/Img/C64_T.png")
pic_y = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Y.png")
pic_u = tk.PhotoImage(file=f"{filedirectory}/Img/C64_U.png")
pic_i = tk.PhotoImage(file=f"{filedirectory}/Img/C64_I.png")
pic_o = tk.PhotoImage(file=f"{filedirectory}/Img/C64_O.png")
pic_p = tk.PhotoImage(file=f"{filedirectory}/Img/C64_P.png")
pic_at = tk.PhotoImage(file=f"{filedirectory}/Img/C64_At.png")
pic_asterisk = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Asterisk.png")
pic_arrow_up = tk.PhotoImage(file=f"{filedirectory}/Img/C64_ArrowUp.png")
pic_control = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Control.png")
pic_restore = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Restore.png")
pic_f3_f4 = tk.PhotoImage(file=f"{filedirectory}/Img/C64_F3.png")

pic_run_stop = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Run_Stop.png")
pic_shift_lock = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Shift_Lock.png")
pic_a = tk.PhotoImage(file=f"{filedirectory}/Img/C64_A.png")
pic_s = tk.PhotoImage(file=f"{filedirectory}/Img/C64_S.png")
pic_d = tk.PhotoImage(file=f"{filedirectory}/Img/C64_D.png")
pic_f = tk.PhotoImage(file=f"{filedirectory}/Img/C64_F.png")
pic_g = tk.PhotoImage(file=f"{filedirectory}/Img/C64_G.png")
pic_h = tk.PhotoImage(file=f"{filedirectory}/Img/C64_H.png")
pic_j = tk.PhotoImage(file=f"{filedirectory}/Img/C64_J.png")
pic_k = tk.PhotoImage(file=f"{filedirectory}/Img/C64_K.png")
pic_l = tk.PhotoImage(file=f"{filedirectory}/Img/C64_L.png")
pic_brace_open = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Brace_Open.png")
pic_brace_close = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Brace_Close.png")
pic_equal = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Equal.png")
pic_return = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Return.png")
pic_f5_f6 = tk.PhotoImage(file=f"{filedirectory}/Img/C64_F5.png")

pic_commodore = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Commodore.png")
pic_shift = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Shift.png")
pic_z = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Z.png")
pic_x = tk.PhotoImage(file=f"{filedirectory}/Img/C64_X.png")
pic_c = tk.PhotoImage(file=f"{filedirectory}/Img/C64_C.png")
pic_v = tk.PhotoImage(file=f"{filedirectory}/Img/C64_V.png")
pic_b = tk.PhotoImage(file=f"{filedirectory}/Img/C64_B.png")
pic_n = tk.PhotoImage(file=f"{filedirectory}/Img/C64_N.png")
pic_m = tk.PhotoImage(file=f"{filedirectory}/Img/C64_M.png")
pic_comma = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Comma.png")
pic_dot = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Dot.png")
pic_slash = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Slash.png")
pic_cursor_up_down = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Cursor_UpDown.png")
pic_cursor_left_right = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Cursor_LeftRight.png")
pic_f7_f8 = tk.PhotoImage(file=f"{filedirectory}/Img/C64_F7.png")

pic_space = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Space_Optimized.png")
pic_extra = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Extra.png")

#endregion

#region TKinter Buttons erstellen

# Zeile 1 

"""Beispiel hoverbutton:
btn1 = HoverButton(window, image=pic_arrow_left, image_alt = pic_f1_f2)
btn1.place(x=1, y=10, width=60, height=60)
btn1.bind( "<Button>", lambda x: print("test") )
btn1.configure(background='black')
btn1.configure(border=0)"""

btn1 = ttk.Label(window, image=pic_arrow_left)
btn1.place(x=1, y=10, width=60, height=60)
btn1.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn1.configure(background='black')
btn1.configure(border=0)

btn2 = ttk.Label(window, image=pic_one)
btn2.place(x=60, y=10, width=60, height=60)
btn2.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn2.configure(background='black')
btn2.configure(border=0)

btn3 = ttk.Label(window, image=pic_two)
btn3.place(x=120, y=10, width=60, height=60)
btn3.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn3.configure(background='black')
btn3.configure(border=0)

btn4 = ttk.Label(window, image=pic_three)
btn4.place(x=180, y=10, width=60, height=60)
btn4.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn4.configure(background='black')
btn4.configure(border=0)

btn5 = ttk.Label(window, image=pic_four)
btn5.place(x=240, y=10, width=60, height=60)
btn5.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn5.configure(background='black')
btn5.configure(border=0)

btn6 = ttk.Label(window, image=pic_five)
btn6.place(x=300, y=10, width=60, height=60)
btn6.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn6.configure(background='black')
btn6.configure(border=0)

btn7 = ttk.Label(window, image=pic_six)
btn7.place(x=360, y=10, width=60, height=60)
btn7.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn7.configure(background='black')
btn7.configure(border=0)

btn8 = ttk.Label(window, image=pic_seven)
btn8.place(x=420, y=10, width=60, height=60)
btn8.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn8.configure(background='black')
btn8.configure(border=0)

btn9 = ttk.Label(window, image=pic_eight)
btn9.place(x=480, y=10, width=60, height=60)
btn9.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn9.configure(background='black')
btn9.configure(border=0)

btn_nine = ttk.Label(window, image=pic_nine)
btn_nine.place(x=540, y=10, width=60, height=60)
btn_nine.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_nine.configure(background='black')
btn_nine.configure(border=0)

btn_zero = ttk.Label(window, image=pic_zero)
btn_zero.place(x=600, y=10, width=60, height=60)
btn_zero.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_zero.configure(background='black')
btn_zero.configure(border=0)

btn_plus = ttk.Label(window, image=pic_plus)
btn_plus.place(x=660, y=10, width=60, height=60)
btn_plus.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_plus.configure(background='black')
btn_plus.configure(border=0)

btn_minus = ttk.Label(window, image=pic_minus)
btn_minus.place(x=720, y=10, width=60, height=60)
btn_minus.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_minus.configure(background='black')
btn_minus.configure(border=0)

btn_pound = ttk.Label(window, image=pic_pound)
btn_pound.place(x=780, y=10, width=60, height=60)
btn_pound.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_pound.configure(background='black')
btn_pound.configure(border=0)

btn_home = ttk.Label(window, image=pic_home)
btn_home.place(x=840, y=10, width=60, height=60)
btn_home.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_home.configure(background='black')
btn_home.configure(border=0)

btn_del = ttk.Label(window, image=pic_del)
btn_del.place(x=900, y=10, width=60, height=60)
btn_del.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_del.configure(background='black')
btn_del.configure(border=0)

btn_f1_f2 = ttk.Label(window, image=pic_f1_f2)
btn_f1_f2.place(x=1020, y=10, width=120, height=60)
btn_f1_f2.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_f1_f2.configure(background='black')
btn_f1_f2.configure(border=0)

# Zeile 2

btn_control = ttk.Label(window, image=pic_control)
btn_control.place(x=1, y=70, width=120, height=60)
btn_control.bind( "<Button>", lambda x: print("zu sendende daten hier reinschreiben") )
btn_control.configure(background='black')
btn_control.configure(border=0)

btn_q = ttk.Label(window, image=pic_q)
btn_q.place(x=90, y=70, width=120, height=60)
btn_q.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_q.configure(background='black')
btn_q.configure(border=0)

btn_w = ttk.Label(window, image=pic_w)
btn_w.place(x=150, y=70, width=120, height=60)
btn_w.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_w.configure(background='black')
btn_w.configure(border=0)

btn_e = ttk.Label(window, image=pic_e)
btn_e.place(x=210, y=70, width=120, height=60)
btn_e.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_e.configure(background='black')
btn_e.configure(border=0)

btn_r = ttk.Label(window, image=pic_r)
btn_r.place(x=270, y=70, width=120, height=60)
btn_r.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_r.configure(background='black')
btn_r.configure(border=0)

btn_t = ttk.Label(window, image=pic_t)
btn_t.place(x=330, y=70, width=120, height=60)
btn_t.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_t.configure(background='black')
btn_t.configure(border=0)

btn_y = ttk.Label(window, image=pic_y)
btn_y.place(x=390, y=70, width=120, height=60)
btn_y.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_y.configure(background='black')
btn_y.configure(border=0)

btn_u = ttk.Label(window, image=pic_u)
btn_u.place(x=450, y=70, width=120, height=60)
btn_u.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_u.configure(background='black')
btn_u.configure(border=0)

btn_i = ttk.Label(window, image=pic_i)
btn_i.place(x=510, y=70, width=120, height=60)
btn_i.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_i.configure(background='black')
btn_i.configure(border=0)

btn_o = ttk.Label(window, image=pic_o)
btn_o.place(x=570, y=70, width=120, height=60)
btn_o.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_o.configure(background='black')
btn_o.configure(border=0)

btn_p = ttk.Label(window, image=pic_p)
btn_p.place(x=630, y=70, width=120, height=60)
btn_p.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_p.configure(background='black')
btn_p.configure(border=0)


btn_at = ttk.Label(window, image=pic_at)
btn_at.place(x=690, y=70, width=120, height=60)
btn_at.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_at.configure(background='black')
btn_at.configure(border=0)

btn_asterisk = ttk.Label(window, image=pic_asterisk)
btn_asterisk.place(x=750, y=70, width=120, height=60)
btn_asterisk.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_asterisk.configure(background='black')
btn_asterisk.configure(border=0)

btn_arrow_up = ttk.Label(window, image=pic_arrow_up)
btn_arrow_up.place(x=810, y=70, width=120, height=60)
btn_arrow_up.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_arrow_up.configure(background='black')
btn_arrow_up.configure(border=0)

btn_restore = ttk.Label(window, image=pic_restore)
btn_restore.place(x=870, y=70, width=120, height=60)
btn_restore.bind( "<Button>", lambda x: print("zu sendende daten hier reinschreiben") )
btn_restore.configure(background='black')
btn_restore.configure(border=0)

btn_f3_f4 = ttk.Label(window, image=pic_f3_f4)
btn_f3_f4.place(x=1020, y=70, width=120, height=60)
btn_f3_f4.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_f3_f4.configure(background='black')
btn_f3_f4.configure(border=0)

# Zeile 3

btn_run_stop = ttk.Label(window, image=pic_run_stop)
btn_run_stop.place(x=1, y=130, width=120, height=60)
btn_run_stop.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_run_stop.configure(background='black')
btn_run_stop.configure(border=0)

btn_shift_lock = ttk.Label(window, image=pic_shift_lock)
btn_shift_lock.place(x=60, y=130, width=120, height=60)
btn_shift_lock.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_shift_lock.configure(background='black')
btn_shift_lock.configure(border=0)

btn_a = ttk.Label(window, image=pic_a)
btn_a.place(x=120, y=130, width=120, height=60)
btn_a.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_a.configure(background='black')
btn_a.configure(border=0)

btn_s = ttk.Label(window, image=pic_s)
btn_s.place(x=180, y=130, width=120, height=60)
btn_s.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_s.configure(background='black')
btn_s.configure(border=0)

btn_d = ttk.Label(window, image=pic_d)
btn_d.place(x=240, y=130, width=120, height=60)
btn_d.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_d.configure(background='black')
btn_d.configure(border=0)

btn_f = ttk.Label(window, image=pic_f)
btn_f.place(x=300, y=130, width=120, height=60)
btn_f.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_f.configure(background='black')
btn_f.configure(border=0)

btn_g = ttk.Label(window, image=pic_g)
btn_g.place(x=360, y=130, width=120, height=60)
btn_g.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_g.configure(background='black')
btn_g.configure(border=0)

btn_h = ttk.Label(window, image=pic_h)
btn_h.place(x=420, y=130, width=120, height=60)
btn_h.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_h.configure(background='black')
btn_h.configure(border=0)

btn_j = ttk.Label(window, image=pic_j)
btn_j.place(x=480, y=130, width=120, height=60)
btn_j.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_j.configure(background='black')
btn_j.configure(border=0)

btn_k = ttk.Label(window, image=pic_k)
btn_k.place(x=540, y=130, width=120, height=60)
btn_k.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_k.configure(background='black')
btn_k.configure(border=0)

btn_l = ttk.Label(window, image=pic_l)
btn_l.place(x=600, y=130, width=120, height=60)
btn_l.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_l.configure(background='black')
btn_l.configure(border=0)

btn_brace_open = ttk.Label(window, image=pic_brace_open)
btn_brace_open.place(x=660, y=130, width=120, height=60)
btn_brace_open.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_brace_open.configure(background='black')
btn_brace_open.configure(border=0)

btn_brace_close = ttk.Label(window, image=pic_brace_close)
btn_brace_close.place(x=720, y=130, width=120, height=60)
btn_brace_close.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_brace_close.configure(background='black')
btn_brace_close.configure(border=0)

btn_equal = ttk.Label(window, image=pic_equal)
btn_equal.place(x=780, y=130, width=120, height=60)
btn_equal.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_equal.configure(background='black')
btn_equal.configure(border=0)

btn_return = ttk.Label(window, image=pic_return)
btn_return.place(x=840, y=130, width=120, height=60)
btn_return.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_return.configure(background='black')
btn_return.configure(border=0)

btn_f5_f6 = ttk.Label(window, image=pic_f5_f6)
btn_f5_f6.place(x=1020, y=130, width=120, height=60)
btn_f5_f6.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_f5_f6.configure(background='black')
btn_f5_f6.configure(border=0)

# Zeile 4

btn_commodore = ttk.Label(window, image=pic_commodore)
btn_commodore.place(x=1, y=190, width=120, height=60)
btn_commodore.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_commodore.configure(background='black')
btn_commodore.configure(border=0)

btn_shift = ttk.Label(window, image=pic_shift)
btn_shift.place(x=60, y=190, width=120, height=60)
btn_shift.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_shift.configure(background='black')
btn_shift.configure(border=0)

btn_z = ttk.Label(window, image=pic_z)
btn_z.place(x=150, y=190, width=120, height=60)
btn_z.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_z.configure(background='black')
btn_z.configure(border=0)

btn_x = ttk.Label(window, image=pic_x)
btn_x.place(x=210, y=190, width=120, height=60)
btn_x.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_x.configure(background='black')
btn_x.configure(border=0)

btn_c = ttk.Label(window, image=pic_c)
btn_c.place(x=270, y=190, width=120, height=60)
btn_c.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_c.configure(background='black')
btn_c.configure(border=0)

btn_v = ttk.Label(window, image=pic_v)
btn_v.place(x=330, y=190, width=120, height=60)
btn_v.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_v.configure(background='black')
btn_v.configure(border=0)

btn_b = ttk.Label(window, image=pic_b)
btn_b.place(x=390, y=190, width=120, height=60)
btn_b.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_b.configure(background='black')
btn_b.configure(border=0)

btn_n = ttk.Label(window, image=pic_n)
btn_n.place(x=450, y=190, width=120, height=60)
btn_n.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_n.configure(background='black')
btn_n.configure(border=0)

btn_m = ttk.Label(window, image=pic_m)
btn_m.place(x=510, y=190, width=120, height=60)
btn_m.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_m.configure(background='black')
btn_m.configure(border=0)

btn_comma = ttk.Label(window, image=pic_comma)
btn_comma.place(x=570, y=190, width=120, height=60)
btn_comma.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_comma.configure(background='black')
btn_comma.configure(border=0)

btn_dot = ttk.Label(window, image=pic_dot)
btn_dot.place(x=630, y=190, width=120, height=60)
btn_dot.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_dot.configure(background='black')
btn_dot.configure(border=0)

btn_slash = ttk.Label(window, image=pic_slash)
btn_slash.place(x=690, y=190, width=120, height=60)
btn_slash.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_slash.configure(background='black')
btn_slash.configure(border=0)

btn_shift = ttk.Label(window, image=pic_shift)
btn_shift.place(x=750, y=190, width=120, height=60)
btn_shift.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_shift.configure(background='black')
btn_shift.configure(border=0)

btn_cursor_up_down = ttk.Label(window, image=pic_cursor_up_down)
btn_cursor_up_down.place(x=840, y=190, width=120, height=60)
btn_cursor_up_down.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_cursor_up_down.configure(background='black')
btn_cursor_up_down.configure(border=0)

btn_cursor_left_right = ttk.Label(window, image=pic_cursor_left_right)
btn_cursor_left_right.place(x=900, y=190, width=120, height=60)
btn_cursor_left_right.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_cursor_left_right.configure(background='black')
btn_cursor_left_right.configure(border=0)

btn_f7_f8 = ttk.Label(window, image=pic_f7_f8)
btn_f7_f8.place(x=1020, y=190, width=120, height=60)
btn_f7_f8.bind( "<Button>", lambda x: sock.send("zu sendende daten hier reinschreiben") )
btn_f7_f8.configure(background='black')
btn_f7_f8.configure(border=0)

# SPACE Zeile

btn_space = ttk.Label(window, image=pic_space)
btn_space.place(x=170, y=250, width=550, height=60)
btn_space.bind( "<Button>", lambda x: sock.send("leertaste gedrückt"))
btn_space.configure(background='black')
btn_space.configure(border=0)

#region Extratasten
lbl_freeze = tk.Label(window, text="Freeze", background="red",foreground="black",font='Helvetica 10 bold')
lbl_freeze.place(x=785.5,y=260, width="52", height="20")

btn_freeze = ttk.Label(window, image=pic_extra)
btn_freeze.place(x=780, y=280)
btn_freeze.bind( "<Button>", lambda x: print("freeze") )
btn_freeze.configure(background='black')
btn_freeze.configure(border=0)

lbl_menu = tk.Label(window, text="Menu", background="red",foreground="black",font='Helvetica 10 bold')
lbl_menu.place(x=855.5,y=260, width="52", height="20")

btn_menu = ttk.Label(window, image=pic_extra)
btn_menu.place(x=850, y=280)
btn_menu.bind( "<Button>", lambda x: print("menu") )
btn_menu.configure(background='black')
btn_menu.configure(border=0)

lbl_reset = tk.Label(window, text="Reset", background="red",foreground="black",font='Helvetica 10 bold')
lbl_reset.place(x=925.5,y=260, width="52", height="20")

btn_reset = ttk.Label(window, image=pic_extra)
btn_reset.place(x=920, y=280)
btn_reset.bind( "<Button>", lambda x: print("reset") )
btn_reset.configure(background='black')
btn_reset.configure(border=0)

lbl_joystick = tk.Label(window, text="Joystick", background="red",foreground="black",font='Helvetica 10 bold')
lbl_joystick.place(x=995.5,y=260, width="52", height="20")

btn_joystick = ttk.Label(window, image=pic_extra)
btn_joystick.place(x=990, y=280)
btn_joystick.bind( "<Button>", lambda x: print("joy") )
btn_joystick.configure(background='black')
btn_joystick.configure(border=0)
#endregion

window.mainloop()

sock.close()
