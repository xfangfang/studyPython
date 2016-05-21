# -*- coding: utf-8 -*
import socket,re,json,httplib, urllib, base64,json

HOST, PORT = '', 80

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

def getinfo(id):
    headers = {
        'Ocp-Apim-Subscription-Key': 'f7cc29509a8443c5b3a5e56b0e38b5a6',
    }
    params = urllib.urlencode({
        'expr': 'Id='+id,
        'model': 'latest',
        'count': '10',
        'offset': '0',
        'attributes': 'Id,AA.AuId,AA.AfId',
    })
    conn = httplib.HTTPSConnection('oxfordhk.azure-api.net')
    conn.request("GET", "/academic/v1.0/evaluate?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

print 'Serving HTTP on port %s ...' % PORT
while True:
    try:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        print request
        relink = 'id1=(.*)&id2=(.*) '
        cinfo = re.findall(relink,request)
        print cinfo
        id1 = cinfo[0][0]
        id2 = cinfo[0][1]
        RES = '{\"'+id1+'\",\"'+id2+'\"}'
        # RES = getinfo(id1)+getinfo(id2)
        http_response = "HTTP/1.1 200 OK\ntext/html\n\n"+RES
        client_connection.sendall(http_response)
        client_connection.close()
    except:
        print 123
