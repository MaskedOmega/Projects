import socket             
from mss import mss
import cv2
import numpy as np
from PIL import Image


mon = {'top': 0, 'left':0, 'width':1920, 'height':1080}

sct = mss()

s = socket.socket()         # Create a socket object
host = "127.0.0.1"  # Get local mahhhchine name
port = 65434           # Reserve a port for your service.

print ('Connecting to '), host, port
s.connect((host, port))

def Transalte(a):
  a = np.frombuffer(a, dtype=np.uint8)
  print(np.size(a))
  return a

def Format(a):
  a = np.reshape(a, (1080, 1920, 3))
  print(np.size(a))
  return a

while True:
  msg = s.recv(6220800)
  msg=Transalte(msg)
  msglen=len(msg)
  print(msglen)

  
  if msglen == 6220800:
      x = Format(msg)
      cv2.imshow('test', np.array(x))
      if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
      
  else:
    print(len(msg))


  #print(loads(dumps(msg)))
  
  #y = np.frombuffer(smsg, dtype=a.dtype)
    cv2.imshow('test', np.array(x))



