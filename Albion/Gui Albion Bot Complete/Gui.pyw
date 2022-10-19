from tkinter import *

import subprocess
import sys
CREATE_NO_WINDOW = 0x08000000

status=("Stopped")

def StartBot():
        global BOTSUB
        BOTSUB=subprocess.Popen(['python', 'BOT12.py'], stdout = None, stderr = None, shell=False, creationflags=CREATE_NO_WINDOW)
        global status
        status=("Running")
        StatusLChange()
        
def KillBot():
        BOTSUB.kill()
        global status
        status=("Stopped")
        StatusLChange()

import tkinter as tk

window = tk.Tk()
window.geometry('300x150')

window.configure(background="black")
window.title('Albion Fishing Bot!')

def StatusLChange():
        LabelB=Label(window, text=status, bg="black", fg="white", font="none 10 bold")
        LabelB.place(x=117, y=70)



#label and Buttons
LabelA=Label(window, text="Albion Fishing Bot!", bg="black", fg="white", font="none 20 bold")
LabelA.place(x=20, y=30)

StartB=Button(window, text="Start", command=StartBot, bg="gray", fg="white", font="none 15",)
StartB.place(x=20, y=100)

StopB=Button(window, text="Stop", command=KillBot, bg="gray", fg="white", font="none 15")
StopB.place(x=120, y=100)

EndB=Button(window, text="Exit", command=window.destroy, bg="gray", fg="white", font="none 15")
EndB.place(x=220, y=100)

StatusLChange()

##################
window.mainloop()

