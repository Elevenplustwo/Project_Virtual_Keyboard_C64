from bluetooth import *
import tkinter as tk
import os
from time import sleep
import threading
import evdev
from evdev import InputDevice, categorize, ecodes, KeyEvent

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

#--------------------------- QUAD STICK ---------------------------
    
oben = False
unten = False
rechts = False
links = False
feuern = False
unten_a = True
oben_a = True
rechts_a = True
links_a = True
feuern_a = True

test = False

def run_quadstick(s):
    global oben, unten, rechts, links, feuern, oben_a, unten_a,rechts_a,links_a,feuern_a, test
    
    def connect_device(input):
        return evdev.InputDevice(input)
    
    def connect_dummy():
        class event():
            def __init__(self):
                self.type = 0
                self.code = 0
                self.value = 0
        class gamepad:
            def __init__(self):
                self.event = event()
            def read_loop(self):
                while True:
                    yield self.event
        return gamepad()
    
    gamepad = None
    
    while(gamepad == None):
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        for device in devices:
            if "input0" in device.phys and device.name == "QuadStick Quad Stick":
                print(device.path, device.name, device.phys)
                gamepad = evdev.InputDevice(device.path)
        sleep(1)
                

    #if test: gamepad = connect_dummy()
    #else: gamepad = connect_device()
    print("")
    print("Gekoppelt mit:")
    print(gamepad)
    richtung = ""

    # Lese Configdatei für Controller aus
    config_file = "Config.txt"

    # Open the config file and read its contents
    with open(config_file, "r") as f:
        lines = f.readlines()

    # Extract the values from the specified lines
    line3_val = int(lines[2].split(":")[1].strip())
    line4_val = int(lines[3].split(":")[1].strip())
    line6_val = int(lines[5].split(":")[1].strip())
    line7_val = int(lines[6].split(":")[1].strip())
    
    print(line3_val)
    print(line4_val)
    print(line6_val)
    print(line7_val)

    letzteRichtung = 0
    

    for event in gamepad.read_loop(): 
        x = event
        if x.type == 3:
            if x.code == 2 or x.code == 0:
                if x.value <= line3_val:
                    richtung = richtung + "L"
                    links = True
                    rechts = False

                if x.value >= line4_val:
                    richtung = richtung + "R"
                    rechts = True
                    links = False

                if x.value > line3_val and x.value < line4_val:
                    #print "HORIZONTAL-MITTE"
                    rechts = False
                    links = False
            if x.code == 5 or x.code == 1:
                if x.value <= line6_val:
                    richtung = richtung + "O"
                    oben = True
                    unten = False

                if x.value >= line7_val:
                    richtung = richtung + "U"
                    #print(x.value)
                    unten = True
                    oben = False

                if x.value > line6_val and x.value < line7_val:
                    #print "VERTIKAL-MITTE"
                    oben = False
                    unten = False
                    
        if(oben and not unten and not rechts and not links and letzteRichtung != 1):
            letzteRichtung = 1
            print("oben")
            s.put(chr(int(173)).encode('latin_1'))
            s.put(chr(int(71)).encode('latin_1'))
            s.put(chr(int(72)).encode('latin_1'))
            s.put(chr(int(74)).encode('latin_1'))

         
        if(oben and not unten and rechts and not links and letzteRichtung != 2):
            letzteRichtung = 2
            s.put(chr(int(173)).encode('latin_1'))
            s.put(chr(int(172)).encode('latin_1'))
            s.put(chr(int(71)).encode('latin_1'))
            s.put(chr(int(74)).encode('latin_1'))
           
        if(not oben and not unten and rechts and not links and letzteRichtung != 3):
            letzteRichtung = 3
            s.put(chr(int(172)).encode('latin_1'))
            s.put(chr(int(71)).encode('latin_1'))
            s.put(chr(int(73)).encode('latin_1'))
            s.put(chr(int(74)).encode('latin_1'))
           
        if(not oben and unten and rechts and not links and letzteRichtung != 4):
            letzteRichtung = 4
            s.put(chr(int(172)).encode('latin_1'))
            s.put(chr(int(174)).encode('latin_1'))
            s.put(chr(int(71)).encode('latin_1'))
            s.put(chr(int(73)).encode('latin_1'))
           
        if(not oben and unten and not rechts and not links and letzteRichtung != 5):
            letzteRichtung = 5
            s.put(chr(int(174)).encode('latin_1'))
            s.put(chr(int(71)).encode('latin_1'))
            s.put(chr(int(72)).encode('latin_1'))
            s.put(chr(int(73)).encode('latin_1'))
           
        if(not oben and unten and not rechts and links and letzteRichtung != 6):
            letzteRichtung = 6
            s.put(chr(int(174)).encode('latin_1'))
            s.put(chr(int(171)).encode('latin_1'))
            s.put(chr(int(72)).encode('latin_1'))
            s.put(chr(int(73)).encode('latin_1'))
            
        if(not oben and not unten and not rechts and links and letzteRichtung != 7):
            letzteRichtung = 7
            s.put(chr(int(171)).encode('latin_1'))
            s.put(chr(int(72)).encode('latin_1'))
            s.put(chr(int(73)).encode('latin_1'))
            s.put(chr(int(74)).encode('latin_1'))
            
        if(oben and not unten and not rechts and links and letzteRichtung != 8):
            letzteRichtung = 8
            s.put(chr(int(173)).encode('latin_1'))
            s.put(chr(int(171)).encode('latin_1'))
            s.put(chr(int(72)).encode('latin_1'))
            s.put(chr(int(74)).encode('latin_1'))
            
        if(not oben and not unten and not rechts and not links and letzteRichtung != 0):
            letzteRichtung = 0
            print("keine")
            s.put(chr(int(71)).encode('latin_1'))
            s.put(chr(int(72)).encode('latin_1'))
            s.put(chr(int(73)).encode('latin_1'))
            s.put(chr(int(74)).encode('latin_1'))

        if x.type == 1:
            if x.code == 304:
                print(x.value)
                if x.value == 1:
                    print("FEUER")
                    feuern = True
                    s.put(chr(int(175)).encode('latin_1'))
                if x.value == 0:
                    feuern = False
                    print("FEUER LOSGELASSEN")
                    s.put(chr(int(75)).encode('latin_1'))

#------------------------- QUAD STICK ENDE -------------------------

def run_keyboard(filedirectory, s):
    def load_images():
        
        images_dict = {
        "pic_arrow_left" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Arrow.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Arrow.png")),
        "pic_one" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_1.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_1.png")),
        "pic_two" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_2.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_2.png")),
        "pic_three" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_3.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_3.png")),
        "pic_four" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_4.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_4.png")),
        "pic_five" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_5.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_5.png")),
        "pic_six" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_6.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_6.png")),
        "pic_seven" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_7.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_7.png")),
        "pic_eight" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_8.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_8.png")),
        "pic_nine" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_9.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_9.png")),
        "pic_zero" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_0.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_0.png")),
        "pic_plus" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Plus.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Plus.png")),
        "pic_minus" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Minus.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Minus.png")),
        "pic_pound" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Pound.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Pound.png")),
        "pic_home" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Clr_Home.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Clr_Home.png")),
        "pic_del" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Inst_Del.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Inst_Del.png")),
        "pic_f1_f2" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_F1.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_F1.png")),

        #pic_one1 = (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Control.png")
        "pic_q" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Q.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Q.png")),
        "pic_w" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_W.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_W.png")),
        "pic_e" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_E.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_E.png")),
        "pic_r" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_R.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_R.png")),
        "pic_t" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_T.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_T.png")),
        "pic_y" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Y.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Y.png")),
        "pic_u" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_U.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_U.png")),
        "pic_i" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_I.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_I.png")),
        "pic_o" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_O.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_O.png")),
        "pic_p" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_P.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_P.png")),
        "pic_at" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_At.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_At.png")),
        "pic_asterisk" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Asterisk.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Asterisk.png")),
        "pic_arrow_up" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_ArrowUp.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_ArrowUp.png")),
        "pic_control" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Control.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Control.png")),
        "pic_restore" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Restore.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Restore.png")),
        "pic_f3_f4" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_F3.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_F3.png")),

        "pic_run_stop" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Run_Stop.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Run_Stop.png")),
        "pic_shift_lock" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Shift_Lock.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Shift_Lock.png")),
        "pic_a" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_A.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_A.png")),
        "pic_s" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_S.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_S.png")),
        "pic_d" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_D.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_D.png")),
        "pic_f" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_F.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_F.png")),
        "pic_g" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_G.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_G.png")),
        "pic_h" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_H.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_H.png")),
        "pic_j" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_J.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_J.png")),
        "pic_k" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_K.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_K.png")),
        "pic_l" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_L.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_L.png")),
        "pic_brace_open" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Brace_Open.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Brace_Open.png")),
        "pic_brace_close" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Brace_Close.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Brace_Close.png")),
        "pic_equal" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Equal.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Equal.png")),
        "pic_return" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Return.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Return.png")),
        "pic_f5_f6" :(tk.PhotoImage(file=f"{filedirectory}/Img/C64_F5.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_F5.png")),

        "pic_commodore" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Commodore.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Commodore.png")),
        "pic_shift" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Shift.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Shift.png")),
        "pic_z" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Z.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Z.png")),
        "pic_x" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_X.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_X.png")),
        "pic_c" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_C.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_C.png")),
        "pic_v" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_V.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_V.png")),
        "pic_b" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_B.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_B.png")),
        "pic_n" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_N.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_N.png")),
        "pic_m" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_M.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_M.png")),
        "pic_comma" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Comma.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Comma.png")),
        "pic_dot" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Dot.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Dot.png")),
        "pic_slash" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Slash.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Slash.png")),
        "pic_cursor_up_down" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Cursor_UpDown.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Cursor_UpDown.png")),
        "pic_cursor_left_right" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Cursor_LeftRight.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Cursor_LeftRight.png")),
        "pic_f7_f8" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_F7.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_F7.png")),

        "pic_space" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Space_Optimized.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Space_Optimized.png")),
        "pic_extra" : (tk.PhotoImage(file=f"{filedirectory}/Img/C64_Extra.png"),tk.PhotoImage(file=f"{filedirectory}/bordered_pics/bordered-C64_Extra.png")),

        "pic_joystick_arrow_up" : (tk.PhotoImage(file=f"{filedirectory}/Img/joystick_arrow_up.png")),
        "pic_joystick_arrow_right" : (tk.PhotoImage(file=f"{filedirectory}/Img/joystick_arrow_right.png")),
        "pic_joystick_arrow_down" : (tk.PhotoImage(file=f"{filedirectory}/Img/joystick_arrow_down.png")),
        "pic_joystick_arrow_left" : (tk.PhotoImage(file=f"{filedirectory}/Img/joystick_arrow_left.png")),
        "pic_joystick_fire" : (tk.PhotoImage(file=f"{filedirectory}/Img/joystick_fire.png")),
        }
        
        pic_joystick =  tk.PhotoImage(file=f"{filedirectory}/Img/C64_Joystick.png")
        pic_menu = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Menu.png")
        pic_freeze = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Freeze.png")
        pic_reset = tk.PhotoImage(file=f"{filedirectory}/Img/C64_Reset.png")
        
        return images_dict, pic_joystick, pic_menu, pic_freeze, pic_reset
    
    keyCombo_list = []
    def send(event, key):
        if btn_keyCombo.locked:
            if not(event.widget,f"({key},LOW)") in keyCombo_list:
                #s.put(f"({key},HIGH)")
                #sleep(0.01)
                #keyCombo_list.append((event.widget,f"({key},LOW)"))
                #s.put(bytes(int(f"{key}")+100))
                sleep(0.01)
                #keyCombo_list.append((event.widget,f"({key},LOW)"))
                event.widget.lock_unlock()
        else: 
            #s.put(bytes(int(f"{key}")+100))
            #sleep(0.01)
            #s.put(bytes(int(f"{key}")))
            #s.put("50".encode())
            print(chr(int(f"{key}")+100).encode('latin_1'))
            s.put(chr(int(f"{key}")+100).encode('latin_1'))
            sleep(0.01)
            s.put(chr(int(f"{key}")).encode('latin_1'))
            print("Senden")

        if btn_shift.locked:
            btn_shift.lock_unlock()
            btn_shift_right.lock_unlock()
            s.put(chr(int(51)).encode('latin_1'))
            
    def shift_lock(event):
        btn_shift_lock.locked = not btn_shift_lock.locked
        if btn_shift_lock.locked: s.put(chr(int(151)).encode('latin_1'))
        else: s.put(chr(int(51)).encode('latin_1'))
        
    def shift(event):
        if event.widget.name == "shift":
            btn_shift.locked = not btn_shift.locked
            btn_shift_right.lock_unlock()
        elif event.widget.name == "shift_right":
            btn_shift_right.locked = not btn_shift_right.locked
            btn_shift.lock_unlock()
        if btn_shift.locked: s.put(chr(int(151)).encode('latin_1'))
        else: s.put(chr(int(51)).encode('latin_1'))
    
    def commodore(event):
        btn_commodore.locked = not btn_commodore.locked
        if btn_commodore.locked: s.put(chr(int(150)).encode('latin_1'))
        else: s.put(chr(int(50)).encode('latin_1'))
    
    def keyCombo(event):
        btn_keyCombo.locked = not btn_keyCombo.locked
        if not btn_keyCombo.locked:
            for i in keyCombo_list:
                s.put(i[1])
                i[0].lock_unlock()
            keyCombo_list.clear()
    
    window = tk.Tk()
    window.title("Virtual Keyboard 64")
    window.geometry('1120x350')
    window.configure(background='black')
    # Zeile 1 
    images_dict, pic_joystick, pic_menu, pic_freeze, pic_reset = load_images()
    
    btn_arrow_left = HoverButton(window, images=images_dict["pic_arrow_left"])
    btn_arrow_left.place(x=4, y=13, width=58, height=58)
    btn_arrow_left.bind( "<Button>", lambda x: send(x,"1"))
    btn_arrow_left.configure(background='black')
    btn_arrow_left.configure(border=0)

    btn_one = HoverButton(window, images=images_dict["pic_one"])
    btn_one.place(x=63, y=13, width=58, height=58)
    btn_one.bind( "<Button>", lambda x: send(x,"2") )
    btn_one.configure(background='black')
    btn_one.configure(border=0)

    btn_two = HoverButton(window, images=images_dict["pic_two"])
    btn_two.place(x=123, y=13, width=58, height=58)
    btn_two.bind( "<Button>", lambda x: send(x,"3") )
    btn_two.configure(background='black')
    btn_two.configure(border=0)

    btn_three = HoverButton(window, images=images_dict["pic_three"])
    btn_three.place(x=183, y=13, width=58, height=58)
    btn_three.bind( "<Button>", lambda x: send(x,"4") )
    btn_three.configure(background='black')
    btn_three.configure(border=0)

    btn_four = HoverButton(window, images=images_dict["pic_four"])
    btn_four.place(x=243, y=13, width=58, height=58)
    btn_four.bind( "<Button>", lambda x: send(x,"5") )
    btn_four.configure(background='black')
    btn_four.configure(border=0)

    btn_five = HoverButton(window, images=images_dict["pic_five"])
    btn_five.place(x=303, y=13, width=58, height=58)
    btn_five.bind( "<Button>", lambda x: send(x,"6") )
    btn_five.configure(background='black')
    btn_five.configure(border=0)

    btn_six = HoverButton(window, images=images_dict["pic_six"])
    btn_six.place(x=363, y=13, width=58, height=58)
    btn_six.bind( "<Button>", lambda x: send(x,"7") )
    btn_six.configure(background='black')
    btn_six.configure(border=0)

    btn_seven = HoverButton(window, images=images_dict["pic_seven"])
    btn_seven.place(x=423, y=13, width=58, height=58)
    btn_seven.bind( "<Button>", lambda x: send(x,"8") )
    btn_seven.configure(background='black')
    btn_seven.configure(border=0)

    btn_eight = HoverButton(window, images=images_dict["pic_eight"])
    btn_eight.place(x=483, y=13, width=58, height=58)
    btn_eight.bind( "<Button>", lambda x: send(x,"9") )
    btn_eight.configure(background='black')
    btn_eight.configure(border=0)

    btn_nine = HoverButton(window, images=images_dict["pic_nine"])
    btn_nine.place(x=543, y=13, width=58, height=58)
    btn_nine.bind( "<Button>", lambda x: send(x,"10") )
    btn_nine.configure(background='black')
    btn_nine.configure(border=0)

    btn_zero = HoverButton(window, images=images_dict["pic_zero"])
    btn_zero.place(x=603, y=13, width=58, height=58)
    btn_zero.bind( "<Button>", lambda x: send(x,"11") )
    btn_zero.configure(background='black')
    btn_zero.configure(border=0)

    btn_plus = HoverButton(window, images=images_dict["pic_plus"])
    btn_plus.place(x=663, y=13, width=58, height=58)
    btn_plus.bind( "<Button>", lambda x: send(x,"12") )
    btn_plus.configure(background='black')
    btn_plus.configure(border=0)

    btn_minus = HoverButton(window, images=images_dict["pic_minus"])
    btn_minus.place(x=723, y=13, width=58, height=58)
    btn_minus.bind( "<Button>", lambda x: send(x,"13") )
    btn_minus.configure(background='black')
    btn_minus.configure(border=0)

    btn_pound = HoverButton(window, images=images_dict["pic_pound"])
    btn_pound.place(x=783, y=13, width=58, height=58)
    btn_pound.bind( "<Button>", lambda x: send(x,"14") )
    btn_pound.configure(background='black')
    btn_pound.configure(border=0)

    btn_home = HoverButton(window, images=images_dict["pic_home"])
    btn_home.place(x=843, y=13, width=58, height=58)
    btn_home.bind( "<Button>", lambda x: send(x,"15") )
    btn_home.configure(background='black')
    btn_home.configure(border=0)

    btn_del = HoverButton(window, images=images_dict["pic_del"])
    btn_del.place(x=903, y=13, width=58, height=58)
    btn_del.bind( "<Button>", lambda x: send(x,"16") )
    btn_del.configure(background='black')
    btn_del.configure(border=0)

    btn_f1_f2 = HoverButton(window, images=images_dict["pic_f1_f2"])
    btn_f1_f2.place(x=1023, y=13, width=89, height=58)
    btn_f1_f2.bind( "<Button>", lambda x: send(x,"17") )
    btn_f1_f2.configure(background='black')
    btn_f1_f2.configure(border=0)

    # Zeile 2

    btn_control = HoverButton(window, images=images_dict["pic_control"])
    btn_control.place(x=4, y=73, width=89, height=58)
    btn_control.bind( "<Button>", lambda x: send(x,"18") )
    btn_control.configure(background='black')
    btn_control.configure(border=0)

    btn_q = HoverButton(window, images=images_dict["pic_q"])
    btn_q.place(x=93, y=73, width=58, height=58)
    btn_q.bind( "<Button>", lambda x: send(x,"19") )
    btn_q.configure(background='black')
    btn_q.configure(border=0)

    btn_w = HoverButton(window, images=images_dict["pic_w"])
    btn_w.place(x=153, y=73, width=58, height=58)
    btn_w.bind( "<Button>", lambda x: send(x,"20") )
    btn_w.configure(background='black')
    btn_w.configure(border=0)

    btn_e = HoverButton(window, images=images_dict["pic_e"])
    btn_e.place(x=213, y=73, width=58, height=58)
    btn_e.bind( "<Button>", lambda x: send(x,"21") )
    btn_e.configure(background='black')
    btn_e.configure(border=0)

    btn_r = HoverButton(window, images=images_dict["pic_r"])
    btn_r.place(x=273, y=73, width=58, height=58)
    btn_r.bind( "<Button>", lambda x: send(x,"22") )
    btn_r.configure(background='black')
    btn_r.configure(border=0)

    btn_t = HoverButton(window, images=images_dict["pic_t"])
    btn_t.place(x=333, y=73, width=58, height=58)
    btn_t.bind( "<Button>", lambda x: send(x,"23") )
    btn_t.configure(background='black')
    btn_t.configure(border=0)

    btn_y = HoverButton(window, images=images_dict["pic_y"])
    btn_y.place(x=393, y=73, width=58, height=58)
    btn_y.bind( "<Button>", lambda x: send(x,"24") )
    btn_y.configure(background='black')
    btn_y.configure(border=0)

    btn_u = HoverButton(window, images=images_dict["pic_u"])
    btn_u.place(x=453, y=73, width=58, height=58)
    btn_u.bind( "<Button>", lambda x: send(x,"25") )
    btn_u.configure(background='black')
    btn_u.configure(border=0)

    btn_i = HoverButton(window, images=images_dict["pic_i"])
    btn_i.place(x=513, y=73, width=58, height=58)
    btn_i.bind( "<Button>", lambda x: send(x,"26") )
    btn_i.configure(background='black')
    btn_i.configure(border=0)

    btn_o = HoverButton(window, images=images_dict["pic_o"])
    btn_o.place(x=573, y=73, width=58, height=58)
    btn_o.bind( "<Button>", lambda x: send(x,"27") )
    btn_o.configure(background='black')
    btn_o.configure(border=0)

    btn_p = HoverButton(window, images=images_dict["pic_p"])
    btn_p.place(x=633, y=73, width=58, height=58)
    btn_p.bind( "<Button>", lambda x: send(x,"28") )
    btn_p.configure(background='black')
    btn_p.configure(border=0)

    btn_at = HoverButton(window, images=images_dict["pic_at"])
    btn_at.place(x=693, y=73, width=58, height=58)
    btn_at.bind( "<Button>", lambda x: send(x,"29") )
    btn_at.configure(background='black')
    btn_at.configure(border=0)

    btn_asterisk = HoverButton(window, images=images_dict["pic_asterisk"])
    btn_asterisk.place(x=753, y=73, width=58, height=58)
    btn_asterisk.bind( "<Button>", lambda x: send(x,"30") )
    btn_asterisk.configure(background='black')
    btn_asterisk.configure(border=0)

    btn_arrow_up = HoverButton(window, images=images_dict["pic_arrow_up"])
    btn_arrow_up.place(x=813, y=73, width=58, height=58)
    btn_arrow_up.bind( "<Button>", lambda x: send(x,"31") )
    btn_arrow_up.configure(background='black')
    btn_arrow_up.configure(border=0)

    btn_restore = HoverButton(window, images=images_dict["pic_restore"])
    btn_restore.place(x=873, y=73, width=89, height=58)
    btn_restore.bind( "<Button>", lambda x: send(x,"32") )
    btn_restore.configure(background='black')
    btn_restore.configure(border=0)

    btn_f3_f4 = HoverButton(window, images=images_dict["pic_f3_f4"])
    btn_f3_f4.place(x=1023, y=73, width=89, height=58)
    btn_f3_f4.bind( "<Button>", lambda x: send(x,"33") )
    btn_f3_f4.configure(background='black')
    btn_f3_f4.configure(border=0)

    # Zeile 3

    btn_run_stop = HoverButton(window, images=images_dict["pic_run_stop"])
    btn_run_stop.place(x=4, y=133, width=58, height=58)
    btn_run_stop.bind( "<Button>", lambda x: send(x,"34") )
    btn_run_stop.configure(background='black')
    btn_run_stop.configure(border=0)

    #shift lock sendet 35
    btn_shift_lock = HoverButton(window, images=images_dict["pic_shift_lock"])
    btn_shift_lock.place(x=63, y=133, width=58, height=58)
    btn_shift_lock.bind( "<Button>", shift_lock)
    btn_shift_lock.configure(background='black')
    btn_shift_lock.configure(border=0)

    btn_a = HoverButton(window, images=images_dict["pic_a"])
    btn_a.place(x=123, y=133, width=58, height=58)
    btn_a.bind( "<Button>", lambda x: send(x,"36") )
    btn_a.configure(background='black')
    btn_a.configure(border=0)

    btn_s = HoverButton(window, images=images_dict["pic_s"])
    btn_s.place(x=183, y=133, width=58, height=58)
    btn_s.bind( "<Button>", lambda x: send(x,"37") )
    btn_s.configure(background='black')
    btn_s.configure(border=0)

    btn_d = HoverButton(window, images=images_dict["pic_d"])
    btn_d.place(x=243, y=133, width=58, height=58)
    btn_d.bind( "<Button>", lambda x: send(x,"38") )
    btn_d.configure(background='black')
    btn_d.configure(border=0)

    btn_f = HoverButton(window, images=images_dict["pic_f"])
    btn_f.place(x=303, y=133, width=58, height=58)
    btn_f.bind( "<Button>", lambda x: send(x,"39") )
    btn_f.configure(background='black')
    btn_f.configure(border=0)

    btn_g = HoverButton(window, images=images_dict["pic_g"])
    btn_g.place(x=363, y=133, width=58, height=58)
    btn_g.bind( "<Button>", lambda x: send(x,"40") )
    btn_g.configure(background='black')
    btn_g.configure(border=0)

    btn_h = HoverButton(window, images=images_dict["pic_h"])
    btn_h.place(x=423, y=133, width=58, height=58)
    btn_h.bind( "<Button>", lambda x: send(x,"41") )
    btn_h.configure(background='black')
    btn_h.configure(border=0)

    btn_j = HoverButton(window, images=images_dict["pic_j"])
    btn_j.place(x=483, y=133, width=58, height=58)
    btn_j.bind( "<Button>", lambda x: send(x,"42") )
    btn_j.configure(background='black')
    btn_j.configure(border=0)

    btn_k = HoverButton(window, images=images_dict["pic_k"])
    btn_k.place(x=543, y=133, width=58, height=58)
    btn_k.bind( "<Button>", lambda x: send(x,"43") )
    btn_k.configure(background='black')
    btn_k.configure(border=0)

    btn_l = HoverButton(window, images=images_dict["pic_l"])
    btn_l.place(x=603, y=133, width=58, height=58)
    btn_l.bind( "<Button>", lambda x: send(x,"44") )
    btn_l.configure(background='black')
    btn_l.configure(border=0)

    btn_brace_open = HoverButton(window, images=images_dict["pic_brace_open"])
    btn_brace_open.place(x=663, y=133, width=58, height=58)
    btn_brace_open.bind( "<Button>", lambda x: send(x,"45") )
    btn_brace_open.configure(background='black')
    btn_brace_open.configure(border=0)

    btn_brace_close = HoverButton(window, images=images_dict["pic_brace_close"])
    btn_brace_close.place(x=723, y=133, width=58, height=58)
    btn_brace_close.bind( "<Button>", lambda x: send(x,"46") )
    btn_brace_close.configure(background='black')
    btn_brace_close.configure(border=0)

    btn_equal = HoverButton(window, images=images_dict["pic_equal"])
    btn_equal.place(x=783, y=133, width=58, height=58)
    btn_equal.bind( "<Button>", lambda x: send(x,"47") )
    btn_equal.configure(background='black')
    btn_equal.configure(border=0)

    btn_return = HoverButton(window, images=images_dict["pic_return"])
    btn_return.place(x=843, y=133, width=118, height=58)
    btn_return.bind( "<Button>", lambda x: send(x,"48") )
    btn_return.configure(background='black')
    btn_return.configure(border=0)

    btn_f5_f6 = HoverButton(window, images=images_dict["pic_f5_f6"])
    btn_f5_f6.place(x=1023, y=133, width=89, height=58)
    btn_f5_f6.bind( "<Button>", lambda x: send(x,"49") )
    btn_f5_f6.configure(background='black')
    btn_f5_f6.configure(border=0)

    # Zeile 4
    #commodore sendet 50
    btn_commodore = HoverButton(window, images=images_dict["pic_commodore"])
    btn_commodore.place(x=4, y=193, width=58, height=58)
    btn_commodore.bind( "<Button>", commodore )
    btn_commodore.configure(background='black')
    btn_commodore.configure(border=0)

    #shift sendet 51
    btn_shift = HoverButton(window, images=images_dict["pic_shift"])
    btn_shift.place(x=63, y=193, width=89, height=58)
    btn_shift.bind( "<Button>", shift )
    btn_shift.configure(background='black')
    btn_shift.configure(border=0)
    btn_shift.name = "shift"

    btn_z = HoverButton(window, images=images_dict["pic_z"])
    btn_z.place(x=153, y=193, width=58, height=58)
    btn_z.bind( "<Button>", lambda x: send(x,"52") )
    btn_z.configure(background='black')
    btn_z.configure(border=0)

    btn_x = HoverButton(window, images=images_dict["pic_x"])
    btn_x.place(x=213, y=193, width=58, height=58)
    btn_x.bind( "<Button>", lambda x: send(x,"53") )
    btn_x.configure(background='black')
    btn_x.configure(border=0)

    btn_c = HoverButton(window, images=images_dict["pic_c"])
    btn_c.place(x=273, y=193, width=58, height=58)
    btn_c.bind( "<Button>", lambda x: send(x,"54") )
    btn_c.configure(background='black')
    btn_c.configure(border=0)

    btn_v = HoverButton(window, images=images_dict["pic_v"])
    btn_v.place(x=333, y=193, width=58, height=58)
    btn_v.bind( "<Button>", lambda x: send(x,"55") )
    btn_v.configure(background='black')
    btn_v.configure(border=0)

    btn_b = HoverButton(window, images=images_dict["pic_b"])
    btn_b.place(x=393, y=193, width=58, height=58)
    btn_b.bind( "<Button>", lambda x: send(x,"56") )
    btn_b.configure(background='black')
    btn_b.configure(border=0)

    btn_n = HoverButton(window, images=images_dict["pic_n"])
    btn_n.place(x=453, y=193, width=58, height=58)
    btn_n.bind( "<Button>", lambda x: send(x,"57") )
    btn_n.configure(background='black')
    btn_n.configure(border=0)

    btn_m = HoverButton(window, images=images_dict["pic_m"])
    btn_m.place(x=513, y=193, width=58, height=58)
    btn_m.bind( "<Button>", lambda x: send(x,"58") )
    btn_m.configure(background='black')
    btn_m.configure(border=0)

    btn_comma = HoverButton(window, images=images_dict["pic_comma"])
    btn_comma.place(x=573, y=193, width=58, height=58)
    btn_comma.bind( "<Button>", lambda x: send(x,"59") )
    btn_comma.configure(background='black')
    btn_comma.configure(border=0)

    btn_dot = HoverButton(window, images=images_dict["pic_dot"])
    btn_dot.place(x=633, y=193, width=58, height=58)
    btn_dot.bind( "<Button>", lambda x: send(x,"60") )
    btn_dot.configure(background='black')
    btn_dot.configure(border=0)

    btn_slash = HoverButton(window, images=images_dict["pic_slash"])
    btn_slash.place(x=693, y=193, width=58, height=58)
    btn_slash.bind( "<Button>", lambda x: send(x,"61") )
    btn_slash.configure(background='black')
    btn_slash.configure(border=0)

    #shift rechts sendet 62
    btn_shift_right = HoverButton(window, images=images_dict["pic_shift"])
    btn_shift_right.place(x=753, y=193, width=89, height=58)
    btn_shift_right.bind( "<Button>", shift )
    btn_shift_right.configure(background='black')
    btn_shift_right.configure(border=0)
    btn_shift_right.name = "shift_right"

    btn_cursor_up_down = HoverButton(window, images=images_dict["pic_cursor_up_down"])
    btn_cursor_up_down.place(x=843, y=193, width=58, height=58)
    btn_cursor_up_down.bind( "<Button>", lambda x: send(x,"63") )
    btn_cursor_up_down.configure(background='black')
    btn_cursor_up_down.configure(border=0)

    btn_cursor_left_right = HoverButton(window, images=images_dict["pic_cursor_left_right"])
    btn_cursor_left_right.place(x=903, y=193, width=58, height=58)
    btn_cursor_left_right.bind( "<Button>", lambda x: send(x,"64") )
    btn_cursor_left_right.configure(background='black')
    btn_cursor_left_right.configure(border=0)

    btn_f7_f8 = HoverButton(window, images=images_dict["pic_f7_f8"])
    btn_f7_f8.place(x=1023, y=193, width=89, height=58)
    btn_f7_f8.bind( "<Button>", lambda x: send(x,"65") )
    btn_f7_f8.configure(background='black')
    btn_f7_f8.configure(border=0)

    # SPACE Zeile

    btn_space = HoverButton(window, images=images_dict["pic_space"])
    btn_space.place(x=173, y=253, width=548, height=58)
    btn_space.bind( "<Button>", lambda x: send(x,"66"))
    btn_space.configure(background='black')
    btn_space.configure(border=0)

    #region Extratasten
    lbl_freeze = tk.Label(window, image=pic_freeze)
    lbl_freeze.place(x=785.5,y=263)
    lbl_freeze.configure(border=0)

    btn_freeze = HoverButton(window, images=images_dict["pic_extra"])
    btn_freeze.place(x=802, y=292,width=48,height=35)
    btn_freeze.bind( "<Button>", lambda x: send(x,"67") )
    btn_freeze.configure(background='black')
    btn_freeze.configure(border=0)

    lbl_menu = tk.Label(window, image=pic_menu)
    lbl_menu.place(x=870.5,y=263)
    lbl_menu.configure(border=0)

    btn_menu = HoverButton(window, images=images_dict["pic_extra"])
    btn_menu.place(x=873, y=292,width=48,height=35)
    btn_menu.bind( "<Button>", lambda x: send(x,"68") )
    btn_menu.configure(background='black')
    btn_menu.configure(border=0)

    lbl_reset = tk.Label(window, image=pic_reset)
    lbl_reset.place(x=933.5,y=263)
    lbl_reset.configure(border=0)

    btn_reset = HoverButton(window, images=images_dict["pic_extra"])
    btn_reset.place(x=941, y=292,width=48,height=35)
    btn_reset.bind( "<Button>", lambda x: send(x,"69") )
    btn_reset.configure(background='black')
    btn_reset.configure(border=0)

    lbl_joystick = tk.Label(window, image=pic_joystick)
    lbl_joystick.place(x=1007,y=263)
    lbl_joystick.configure(border=0)

    btn_joystick = HoverButton(window, images=images_dict["pic_extra"])
    btn_joystick.place(x=1011, y=292,width=48,height=35)
    btn_joystick.bind( "<Button>", lambda x: send(x,"70") )
    btn_joystick.configure(background='black')
    btn_joystick.configure(border=0)

    lbl_keyCombo = tk.Label(window, text="KEYCOMBO", background="red4",foreground="white",font='Helvetica 10 bold')
    lbl_keyCombo.place(x=52,y=263, width="80", height="22")

    btn_keyCombo = HoverButton(window, images=images_dict["pic_extra"])
    btn_keyCombo.place(x=65, y=292,width=48,height=35)
    btn_keyCombo.bind( "<Button>", keyCombo)
    btn_keyCombo.configure(background='black')
    btn_keyCombo.configure(border=0)
    
    lbl_joystick_arrow_up = tk.Label(window, image=images_dict["pic_joystick_arrow_up"])
    lbl_joystick_arrow_up.place(x=974, y=45, height=40, width=40)

    lbl_joystick_arrow_right = tk.Label(window, image=images_dict["pic_joystick_arrow_right"])
    lbl_joystick_arrow_right.place(x=974, y=87, height=40, width=40)

    lbl_joystick_arrow_down = tk.Label(window, image=images_dict["pic_joystick_arrow_down"])
    lbl_joystick_arrow_down.place(x=974, y=129, height=40, width=40)

    lbl_joystick_arrow_left = tk.Label(window, image=images_dict["pic_joystick_arrow_left"])
    lbl_joystick_arrow_left.place(x=974, y=171, height=40, width=40)

    lbl_joystick_fire = tk.Label(window, image=images_dict["pic_joystick_fire"])
    lbl_joystick_fire.place(x=974, y=213, height=40, width=40)

    def update_buttons():
        global unten, oben, rechts, links, feuern,unten_a,oben_a,rechts_a,links_a,feuern_a
        
        if(unten and not unten_a):
            lbl_joystick_arrow_down.place(x=974, y=129, height=40, width=40)
            unten_a = True
        elif(not unten and unten_a):
            lbl_joystick_arrow_down.place_forget()
            unten_a = False
        
        if(oben and not oben_a):
            lbl_joystick_arrow_up.place(x=974, y=45, height=40, width=40)
            oben_a = True
        elif(not oben and oben_a):
            lbl_joystick_arrow_up.place_forget()
            oben_a = False

        if(links and not links_a):
            lbl_joystick_arrow_left.place(x=974, y=171, height=40, width=40)
            links_a = True
        elif(not links and links_a):
            lbl_joystick_arrow_left.place_forget()
            links_a = False

        if(rechts and not rechts_a):
            lbl_joystick_arrow_right.place(x=974, y=87, height=40, width=40)
            rechts_a = True
        elif(not rechts and rechts_a):
            lbl_joystick_arrow_right.place_forget()
            rechts_a = False

        if(feuern and not feuern_a):
            lbl_joystick_fire.place(x=974, y=213, height=40, width=40)
            feuern_a = True
        elif(not feuern and feuern_a):
            lbl_joystick_fire.place_forget()
            feuern_a = False
        window.after(10, update_buttons)   

    window.after(10, update_buttons) 
    
    window.mainloop()
    
    
    
    
from queue import Queue

def main():
    filedirectory = os.path.dirname(os.path.abspath(__file__))
    print(filedirectory)
    connected = False
    while (connected == False):
        try:
            s = BluetoothSocket(RFCOMM)
        except NameError as e:
            print(e)
            #wenn bluetooth nicht importiert wird/auskommentiert ist, erstellen wir eine hilfsklasse zu testzwecken
            class s:
                def send(x):
                    print(x)
                def connect(s):
                    print(s)
                def close():
                    print("verbindung geschlossen")
     
        #ssid = "DC:A6:32:47:93:A1" 
        ssid="00:21:13:05:A1:D3"
    
        try:
            print(s.getpeername())
            connected = True
        except:
            print("Keine Aktive Verbindung zum C64")
            connected = False
            
        try:
            print("verbinden...")
            s.connect((ssid,1))
            connected = True
        except:
            print("Keine verbindung möglich...")
        sleep(3)
    
    data_queue = Queue()
    #run_quadstick(data_queue)
    
    keyboard_thread = threading.Thread(group=None, target=run_keyboard,args=(filedirectory,data_queue),daemon=False)
    keyboard_thread.start()
    quadstick_thread = threading.Thread(group=None, target=run_quadstick,args=(data_queue,),daemon=False)
    quadstick_thread.start()
    while True:
        if not data_queue.empty():
            s.send(data_queue.get())
    """class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
        This constructor should always be called with keyword arguments. Arguments are:

        group should be None; reserved for future extension when a ThreadGroup class is implemented.

        target is the callable object to be invoked by the run() method. Defaults to None, meaning nothing is called.

        name is the thread name. By default, a unique name is constructed of the form “Thread-N” where N is a small decimal number, or “Thread-N (target)” where “target” is target.__name__ if the target argument is specified.

        args is the argument tuple for the target invocation. Defaults to ().

        kwargs is a dictionary of keyword arguments for the target invocation. Defaults to {}.

        If not None, daemon explicitly sets whether the thread is daemonic. If None (the default), the daemonic property is inherited from the current thread.

        If the subclass overrides the constructor, it must make sure to invoke the base class constructor (Thread.__init__()) before doing anything else to the thread.

        Changed in version 3.10: Use the target name if name argument is omitted.

        Changed in version 3.3: Added the daemon argument."""
    
    s.close()
    
if __name__ == "__main__":
    main()
