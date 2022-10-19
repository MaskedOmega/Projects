import socket             
from mss import mss
import cv2
import numpy as np
from PIL import Image

def ndarray2str(a):
    a = a.tostring()
    return a

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
  # Convert the numpy array to string 
  a = a.tostring()
  #print(len(a))
  return a

def str2ndarray(a):
  # Specify your data type, mine is numpy float64 type, so I am specifying it as np.float64
  a = np.fromstring(a, dtype=np.uint8)
  #array = np.arange(0, 737280, 1, np.uint8)
  a = np.reshape(a, (1080, 1920, 3))
  #a = Image.fromarray(a.reshape(1920,1080), 'RGB')
  return a

while True:
  sct_img = sct.grab(mon)
  #print(sct_img)
  img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
  #print(img)
  img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
  
  screenmsg=img_bgr
  #print(screenmsg)
  #print(np.shape(screenmsg))
  x = ndarray2str(screenmsg)

  #x = str2ndarray(x)
  #print(x)
  #print(len(x))

  #sleep(1)
  c.send(x)
                    




