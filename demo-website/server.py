import os, sys
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"

from django.contrib.auth.models import User
from datahandle.models import Item
import django
django.setup()

from socket import *
import datetime

HOST = '10.140.92.51'
PORT = 20000
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:', addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        d_id = ord(data[0])
        d_type = ord(data[1])
        d_data = ord(data[2])
        print ("recv data: id:%d, type:%d data:%d" %(d_id, d_type, d_data))
        try:
            item=Item.objects.get(item_id=d_id)      
        except (KeyError, Item.DoesNotExist):
            print ("id:%d do not exist\n" %(d_id))
        if item:
            item.item_data=d_data
            item.item_lastdate = datetime.datetime.now()
            item.save()
#tcpCliSock.send('[%s] %s' %(ctime(), data))


tcpSerSock.close()
