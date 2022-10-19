from mss import mss
import cv2
from PIL import Image
import numpy as np
from time import time
import win32gui, win32ui, win32con, win32api

window_name = "IDLE Shell 3.10.1"
#hwnd = win32gui.FindWindow(None, window_name)
#hwndChild = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
#win = win32ui.CreateWindowFromHandle(hwnd)


#def getWindowInfo("Albion Online Client"):
    # Local variables
    #window_information = []

    # Local variables
    #window_handle = None
    #window_width = None
    #window_height = None


#cv2.imshow('test', np.array(img))




import win32gui
import win32ui
from ctypes import windll
from PIL import Image

hwnd = win32gui.FindWindow(None, 'Albion Online Client')

left, top, right, bot = win32gui.GetWindowRect(hwnd)
w = right - left
h = bot - top

while(True):
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 3)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    cv2.imshow('test', np.array(im))
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break


