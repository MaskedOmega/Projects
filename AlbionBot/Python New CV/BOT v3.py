from mss import mss
import cv2
from PIL import Image
import numpy as np
from time import time
import win32gui, win32ui, win32con, win32api
from ctypes import windll
from PIL import Image




###############################################
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

###############################################



needle_img = cv2.imread('Needle_MG.jpg', cv2.IMREAD_UNCHANGED)
threshold = 0.50


needle_img_start = cv2.imread('Needle_Start.jpg', cv2.IMREAD_UNCHANGED)
ValueR=0
thresholdS = 0.54
thresholdS2 = 0.70



hwnd = win32gui.FindWindow(None, 'Albion Online Client')

left, top, right, bot = win32gui.GetWindowRect(hwnd)
w = right - left
h = bot - top


crop_rectangle = (1, 1, 100, 100)



#fish starter:#####

def Fish_Starter(ValueR):

    #print("hi")

    np_img = np.array(im)
    
    
    result = cv2.matchTemplate(np_img, needle_img_start, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


    if max_val >= thresholdS:
        #print('Found needle.')

        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]


        top_left = max_loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)


    
        crop_img = np_img[max_loc[1]:max_loc[1]+needle_w, max_loc[0]:max_loc[0]+needle_h, :] 
        
        result = cv2.matchTemplate(crop_img, needle_img_start, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= thresholdS2:

            needle_w = needle_img_start.shape[1]
            needle_h = needle_img_start.shape[0]


            top_left = max_loc
            bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

            cv2.rectangle(crop_img, top_left, bottom_right,
                         color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)

        elif max_val <= thresholdS2:
            win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)
            win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)
            

        
        cv2.imshow('Crop', np.array(crop_img))
    #cv2.imshow('aa', np.array(np_img))


#fish starter:#####





while(True):

    #Grabbing Game Screen:############################################
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
    #Grabbing Game Screen:#############################################


    #Shrinking image:#########################

    width, height = im.size
 
    left = 300
    top = (height / 4)+100
    right = 700
    bottom = (3 * height / 4)-175
 
    imc = im.crop((left, top, right, bottom))

    #Shrinking image:#########################


    Fish_Starter(ValueR)
    print(ValueR)

    
    #Finding needle:####################################################

    np_img = np.array(imc)
    
    
    result = cv2.matchTemplate(np_img, needle_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


    if max_val >= threshold:
        #print('Found needle.')

        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]


        top_left = max_loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

        cv2.rectangle(np_img, top_left, bottom_right, 
                    color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)


    #Finding needle:####################################################


    #Catching fish:

        print(top_left)
        print(bottom_right)

        middle = (top_left[0]+bottom_right[0])/2

        if middle < 220:
            print("click")
            win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)

        if middle > 220:
            win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

        

    #Catching fish: 







    

    
    #cv2.imshow('test', np.array(im))
    cv2.imshow('Tracking', np.array(np_img))
    #cv2.imshow('testa', np.array(imc))
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break


