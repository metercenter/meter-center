import os, sys
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"

from django.contrib.auth.models import User
from datahandle.models import Meter
from datahandle.models import Data
import django
django.setup()

from socket import *
import datetime

HOST = '10.140.92.51'
PORT = 20000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SerSock = socket(AF_INET, SOCK_DGRAM)
SerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = SerSock.recvfrom(BUFSIZE)
    print 'received message from:', addr

    if data:
        head = data[0:12]
        version = head[0]
        meter_type = hear[1]
        eui = head[2:9]
        data_type = head[10]
        lenth = head[11]
        payload = data[12:12+lenth-1]

        if version != 1:
            continue
 
        try:
            meter=Meter.objects.get(meter_eui=eui)      
        except (KeyError, Meter.DoesNotExist):
            print ("do not exist\n" %(eui))

        if not meter:
            continue

        try:
            data_t=Data.objects.get(meter_id=meter.meter_id) 
        except (KeyError, Data.DoesNotExist):
            print ("do not exist\n")

        if data_t:
            data_l = data.object.order_by('data_id')[0]
            new_id = data_l.data_id + 1
        else:
            new_id = 1

        if data_type = 6:
            qb = socket.ntohl(payload[0:3])
            qb_s = str(qb)
            vb1 = socket.ntohl(payload[4:7])
            vb2 = socket.ntohs(payload[8:9])
            vb_s = str(vb1)+'.'+str(vb2)
            new_data = Data(data_id=new_id, data_vb=vb_s, data_qb=qb_s)
            new_data.save()

SerSock.close()
