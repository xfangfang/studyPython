# -*- coding: utf-8 -*-

import socket
port=1234
host='127.0.0.1'
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = "123"
print s.sendto(data,(host,port))
