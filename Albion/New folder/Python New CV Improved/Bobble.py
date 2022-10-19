from mss import mss
import cv2
from PIL import Image
import numpy as np
from time import time
import win32gui, win32ui, win32con, win32api
from ctypes import windll
from PIL import Image

import usb.core
import usb.util
import libusb
import usb.core
import time

window_name = "Albion Online Client"
hwnd = win32gui.FindWindow(None, window_name)
hwndChild = win32gui.GetWindow(hwnd, win32con.GW_CHILD)

x = 212
y = 66
lParam = (y << 16) | x

needle_img = cv2.imread('Needle_Start.jpg', cv2.IMREAD_UNCHANGED)
threshold = 0.57

ValueR=False
thresholdS = 0.47
thresholdS2 = 0.100


hwnd = win32gui.FindWindow(None, 'Albion Online Client')

left, top, right, bot = win32gui.GetWindowRect(hwnd)
w = right - left
h = bot - top

crop_rectangle = (1, 1, 100, 100)

im=0


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


np_img = np.array(im)
    
result = cv2.matchTemplate(np_img, needle_img, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


if max_val >= thresholdS:
    print('Found needle in lake.')

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]


    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
    
    crop_img = np_img[max_loc[1]:max_loc[1]+needle_w, max_loc[0]:max_loc[0]+needle_h, :] 
        


cv2.imshow('test', np.array(crop_img))
