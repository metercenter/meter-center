import os, sys
sys.path.append('./db_handle')
os.environ["DJANGO_SETTINGS_MODULE"] = "measureSys.settings"

from django.contrib.auth.models import User
from meter.models import Meter
from meter.models import Data
import django
django.setup()

from socket import *
import datetime
import struct

HOST = '114.215.138.135'
PORT = 20000
BUFSIZE = 1024
ADDR = (HOST, PORT)
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

    meter_list = Meter.objects.all()
    print eui,len(meter_list),meter_list[0].meter_eui

    try:
        meter=Meter.objects.get(meter_eui=eui)      
    except (KeyError, Meter.DoesNotExist):
        print ("meter do not exist\n")
        continue
 
    if data_type == 6:
        payload = data[12:(12+length)]
        qb, vb1, vb2 = struct.unpack("!IIH", payload)
        meter_data=Data.objects.filter(meter_eui=eui).order_by('-data_id')
        if len(meter_data) > 0:
            new_id = meter_data[0].data_id + 1
            vb_last=float(meter_data[0].data_vb)
            vb_diff=vb1 - vb_last
            val=(float(meter.meter_qb))*4/5
            print vb_last, vb_diff, val 
            if vb_diff < val:
              warn=True
            else:
              warn=False
                       
        else:
            print ("firstdata for this meter\n")
            new_id = 1;
            warn=False

        qb_s = str(qb)
        vb_s = str(vb1)+'.'+str(vb2)
        new_data = Data(data_id=new_id, meter_id=meter.meter_id, meter_eui=eui, data_warn=warn, data_vb=vb_s, data_qb=qb_s)
        new_data.data_date = datetime.datetime.now()
        new_data.save()

SerSock.close()
