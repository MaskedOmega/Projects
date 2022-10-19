
from Bobble import CompleteTrack
from CompleteCatch import CompleteCatch

import usb.core
import usb.util
import libusb
import usb.core
import time
import win32gui, win32ui, win32con, win32api

x = 212
y = 66
lParam = (y << 16) | x
window_name = "Albion Online Client"
hwnd = win32gui.FindWindow(None, window_name)

CatchEnd=False
ReturnValueBobble=0
counter=0

while(True):
    CatchEnd=False
    
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)
    time.sleep(0.1)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

    time.sleep(3)
    
    ReturnValueBobble=CompleteTrack(ReturnValueBobble)
    #print(ReturnValueBobble)
    
    if ReturnValueBobble == True:
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

    while counter != 200:
        CatchEnd=CompleteCatch(CatchEnd)
        #print(CatchEnd)
        counter=counter+1
