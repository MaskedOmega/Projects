import socket             
from mss import mss
import cv2
import numpy as np
from PIL import Image

s = socket.socket() 
mon = {'top': 0, 'left':0, 'width':1920, 'height':1080}
sct = mss()

host = "127.0.0.1"  
port = 65434
print ('Server started!')
print ('Waiting for clients...')
s.bind((host, port))        
s.listen(5)                
c, addr = s.accept()     
print ('Got connection from'), addr

def ndarray2str(a):
  a = a.tostring()
  return a

while True:
  sct_img = sct.grab(mon)
  img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
  img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
  
  screenmsg=img_bgr
  x = ndarray2str(screenmsg)
  c.send(x)
                    




