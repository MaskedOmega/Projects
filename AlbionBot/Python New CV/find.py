import usb.core
import usb.util
import libusb
import usb.core
import win32gui, win32ui, win32con, win32api
import time
from time import sleep

def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)

list_window_names()


VENDOR_ID = 0x413c
PRODUCT_ID = 0x2113
device = usb.core.find(idVendor=VENDOR_ID,
                       idProduct=PRODUCT_ID)
device.set_configuration()
endpoint = device[0][(0,0)][0]

#Keys
crouch = 0x11 
RClick =0x1
MClick=0x4
One=0x6
Tab=0x9 or 0x10 or 0x49
Jump=0x20
Two=0x32
Three=0x33
Four=0x34
Five=0x35
Emote=0x42
C=0x43
f=0x46
q=0x47
z=0x51
r=0x52
v=0x56
x=0x58
y=0x59



def keystroke(hwnd, key):
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    win32gui.PostMessage(hwnd, win32con.WM_KEYUP, key, 3 < 30)

list_window_names()

window_name = "Albion Online Client"
#window_name = "Among Us"
hwnd = win32gui.FindWindow(None, window_name)
hwndChild = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
#win = win32ui.CreateWindowFromHandle(hwnd)


x = 212
y = 66
lParam = (y << 16) | x

# read a data packet
data = None
collected = 0
attempts = 50000
while collected < attempts :
    try:
        data = device.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize)
        collected += 1
        print (data)

        if data[2] == 26:
            print("W")


            #win32api.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, hwnd);
            #win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x66, 0x001E0001);
            #win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x60, 0xC01E0001);

            win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, lParam)
            win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

            
            #win32api.SendMessage(hwnd, win32con.WM_CHAR, ord("w"), 0)
            win32api.SendMessage(hwndChild, win32con.WM_KEYDOWN, win32con.VK_UP, 0)
            #win32api.SendMessage(hwndChild, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
            #win32api.SendMessage(hwndChild, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

            #win32api.PostMessage(hwndChild, win32con.WM_CHAR, 0x44, 0)


            

        if data[2] == 4:
            print("A")

        if data[2] == 44:
            print("Jump")
            win32api.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, hwnd);
            win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x20, 0x001E0001);
            win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x20, 0xC01E0001);


        if data[2] == 7:
            print("D")

        if data[2] == 22:
            print("S")

    except usb.core.USBError as e:
        data = None
        if e.args == ('Operation timed out',):
            attempts -= 1
            continue
    print (data)




