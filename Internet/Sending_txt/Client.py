
#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "127.0.0.1"  # Get local mahhhchine name
port = 65432                 # Reserve a port for your service.

print ('Connecting to '), host, port
s.connect((host, port))

while True:
  msg = input('CLIENT >> ')
  msg = bytes(msg, 'utf-8')
  s.send(msg)
  smsg = s.recv(1024)
  print ("server", (' >> '), smsg)

#s.close        134hi
