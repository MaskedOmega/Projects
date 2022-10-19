from mss import mss
import cv2
from PIL import Image
import numpy as np
from time import time
import win32gui, win32ui, win32con, win32api
from ctypes import windll
from PIL import Image

import ctypes

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



def MakeLParam(LoWord, HiWord):
        return ((HiWord << 16) | (LoWord & 0xFFFF));



while(True):
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 1,MakeLParam(222,20));
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0,MakeLParam(100,21));







