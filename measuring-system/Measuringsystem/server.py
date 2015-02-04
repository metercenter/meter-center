import os, sys
os.environ["DJANGO_SETTINGS_MODULE"] = "Measuringsystem.settings"

from django.contrib.auth.models import User
from MeterManagment.models import Meter
from MeterManagment.models import Data
import django
django.setup()

from socket import *
import datetime
import struct

HOST = '10.140.92.41'
PORT = 20000
BUFSIZE = 1024
ADDR = (HOST, PORT)
new_id = 0
SerSock = socket(AF_INET, SOCK_DGRAM)
SerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = SerSock.recvfrom(BUFSIZE)
    print 'received message from:', addr

    if data:
        if len(data) < 12:
            continue
        head = data[0:12]
        version, meter_type, eui, data_type, length = struct.unpack("!BB8sBB", head) 

    if version != 1:
        continue

    if data_type == 6:
        payload = data[12:(12+length)]
        qb, vb1, vb2 = struct.unpack("!IIH", payload)
        qb_s = str(qb)
        vb_s = str(vb1)+'.'+str(vb2)
        print qb_s+'  '+vb_s
        new_id = new_id + 1
        new_data = Data(data_id=new_id, data_vb=vb_s, data_qb=qb_s)
        new_data.data_date = datetime.datetime.now()
        new_data.save()

        try:
            data_list = Data.objects.all()
            print ("data num:%d" %(len(data_list)))
            print data_list[0].data_vb+' '+data_list[0].data_qb
        except (KeyError, Meter.DoesNotExist):
            print ("%s do not exist\n" %(eui))
 
SerSock.close()
