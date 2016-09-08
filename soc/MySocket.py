# -*- coding: utf-8 -*-

import socket

port=8080
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#从指定的端口，从任何发送者，接收UDP数据
s.bind(('',port))
print('正在等待接入...')
while True:
    #接收一个数据
    q = s.recvfrom(1024)
    data,addr= q
    print 'Received:',data,'from',addr
