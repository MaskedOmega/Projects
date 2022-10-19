from mss import mss
import cv2
from PIL import Image
import numpy as np
from time import time

import win32gui, win32ui, win32con, win32api
from ctypes import windll

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
threshold = 0.60

needle_img_start = cv2.imread('Needle_Start.jpg', cv2.IMREAD_UNCHANGED)
ValueR=False
thresholdS = 0.40

needle_img_start2 = cv2.imread('Needle_Start2.jpg', cv2.IMREAD_UNCHANGED)
thresholdS2 = 0.47

needle_img_end = cv2.imread('Needle_End.jpg', cv2.IMREAD_UNCHANGED)
thresholdB=0.40


hwnd = win32gui.FindWindow(None, 'Albion Online Client')

left, top, right, bot = win32gui.GetWindowRect(hwnd)
w = right - left
h = bot - top

crop_rectangle = (1, 1, 100, 100)

im=0

    #cv2.imshow("q",np.array(np_img))
    #if cv2.waitKey(1) == ord('q'):
        #cv2.destroyAllWindows()

def Cast():
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

def Fish_Starter(ValueR):
    im=Grab_Screen()
    np_img = np.array(im)
    
    result = cv2.matchTemplate(np_img, needle_img_start, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #print(max_val)

    
    if max_val >= thresholdS:
            needle_w = needle_img_start.shape[1]
            needle_h = needle_img_start.shape[0]

            top_left = max_loc
            bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

            #cv2.rectangle(np_img, top_left, bottom_right,
                          #color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)

            #cv2.imshow("q",np.array(np_img))
           # if cv2.waitKey(1) == ord('q'):
                    #cv2.destroyAllWindows()

            #print('Found needle in lake.')
                
            y=top_left[1]
            x=top_left[0]
            h=needle_h
            w=needle_w
            crop = np_img[y:y+h, x:x+w]
            #cv2.imshow('Image', crop)
            #if cv2.waitKey(1) == ord('q'):
                    #cv2.destroyAllWindows()
            

        
            if max_val > thresholdS2:
                    result = cv2.matchTemplate(crop, needle_img_start2, cv2.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

                    top_left = max_loc
                    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

                   #cv2.rectangle(crop, top_left, bottom_right,
                               #   color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)

                   # cv2.imshow("q1",np.array(crop))
                   # if cv2.waitKey(1) == ord('q'):
                          #  cv2.destroyAllWindows()
                            
                    #print('tracked needle in lake.')
                    #print(max_val)

            if max_val < thresholdS2:
                    cv2.destroyAllWindows()
                    #print('click.')
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
    im=Grab_Screen()
    width, height = im.size
    left = 300
    top = (height / 4)+100
    right = 700
    bottom = (3 * height / 4)-175
 
    imc = im.crop((left, top, right, bottom))

    return (imc)


def Mini_Game(np_img):
    imc=Crop()
    np_img = np.array(imc)
    
    result = cv2.matchTemplate(np_img, needle_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #print(max_val)

    if max_val >= threshold:

        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]


        top_left = max_loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
        middle = (top_left[0]+bottom_right[0])/2

       # cv2.rectangle(np_img, top_left, bottom_right,
                   #   color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)

        if middle < 240:
                #print("click")
                win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)

        elif middle > 240:
                win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)


    #cv2.imshow("q12",np.array(np_img))
    #if cv2.waitKey(1) == ord('q'):
           # cv2.destroyAllWindows()
    #return (np_img)


np_img=0


def StartBot():
        counter=0
        time.sleep(2)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)
        time.sleep(0.15)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

        print("Reset")
        ValueR1=False
        ValueR=False
        ValueRE1 = False
        ValueRE0 = False
        ValueRE = False
        counter=0

        while counter != 1:
                time.sleep(1)
                while(ValueRE != True):
                        ValueRE=Fish_Starter(ValueR)
                counter=1
        Cast()
        print("captured")
        
        while(counter != 300):
                a=Mini_Game(np_img)
                counter=counter+1
        
        print("done")
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)
        
while(True):
        StartBot()






