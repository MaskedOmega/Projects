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

needle_img = cv2.imread('Needle_MG.jpg', cv2.IMREAD_UNCHANGED)
threshold = 0.50

needle_img_start = cv2.imread('Needle_Start.jpg', cv2.IMREAD_UNCHANGED)
ValueR=False
thresholdS = 0.47
thresholdS2 = 0.54

needle_img_end = cv2.imread('Needle_End.jpg', cv2.IMREAD_UNCHANGED)
thresholdB=0.35


hwnd = win32gui.FindWindow(None, 'Albion Online Client')

left, top, right, bot = win32gui.GetWindowRect(hwnd)
w = right - left
h = bot - top

crop_rectangle = (1, 1, 100, 100)

im=0


def Cast():
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

def Fish_Starter(ValueR):

    np_img = np.array(im)
    
    result = cv2.matchTemplate(np_img, needle_img_start, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= thresholdS:
        print('Found needle in lake.')

        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]

        top_left = max_loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
    
        crop_img = np_img[max_loc[1]:max_loc[1]+needle_w, max_loc[0]:max_loc[0]+needle_h, :] 
        
        result = cv2.matchTemplate(crop_img, needle_img_start, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        if max_val >= thresholdS2:
            print('tracked needle in lake.')

        elif max_val <= thresholdS2:
                ValueR=True
                return(ValueR)
        

            



def Grab_Screen():
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
    return(im)

def Crop():
    width, height = im.size
 
    left = 300
    top = (height / 4)+100
    right = 700
    bottom = (3 * height / 4)-175
 
    imc = im.crop((left, top, right, bottom))

    return (imc)


def Mini_Game():
    
    np_img = np.array(imc)
    
    result = cv2.matchTemplate(np_img, needle_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:

        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]


        top_left = max_loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

        middle = (top_left[0]+bottom_right[0])/2

        if middle < 215:
            print("click")
            win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)

        elif middle > 215:
            win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

def End(ValueR1):
        np_img = np.array(imc)
        
        result = cv2.matchTemplate(np_img, needle_img_end, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val < thresholdB:
                print("end")
                ValueR1=True
                return(ValueR1)


while(True):
        counter=0
        #win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)
        #win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

        while counter != 1:
                print("Reset")
                ValueR1=False
                ValueR=False
                ValueRE1 = False
                ValueRE0 = False
                ValueRE = False


                win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)
                time.sleep(2.5)
                win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)
    
                
        
                while(ValueRE != True):
                        im=Grab_Screen()
                        ValueRE=Fish_Starter(ValueR)

                counter=1

        Cast()
        time.sleep(0.1)
        print("captured")


        while(ValueRE1 != True):
                im=Grab_Screen()
                imc=Crop()
                Mini_Game()
                ValueRE1=End(ValueR1)
        
        print("done")
        #win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

        
