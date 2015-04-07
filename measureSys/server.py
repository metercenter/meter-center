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

HOST = '221.226.182.14'
PORT = 20000
BUFSIZE = 1024
ADDR = (HOST, PORT)
SerSock = socket(AF_INET, SOCK_DGRAM)
SerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = SerSock.recvfrom(BUFSIZE)
    print 'received message from:', addr
    print data
    if data:
        if len(data) < 12:
            continue
        head = data[0:12]
        version, meter_type, eui, data_type, length = struct.unpack("!BB8sBB", head) 

    print len(data)
    if version != 1:
        continue

    meter_list = Meter.objects.all()
    #eui_str=eui.decode('UTF-8').encode('hex')
    eui_str=eui.encode('hex')
    print eui_str

    try:
        meter=Meter.objects.get(meter_eui=eui_str)      
    except (KeyError, Meter.DoesNotExist):
        print ("meter do not exist\n")
        continue
 
    if data_type == 6:
        payload = data[12:(12+length)]
        qb, vb1, vb2 = struct.unpack("!IIH", payload)
        meter_data=Data.objects.filter(meter_eui=eui_str).order_by('-data_id')
        if len(meter_data) > 0:
            new_id = meter_data[0].data_id + 1
#            vb_last=float(meter_data[0].data_vb)
#            vb_diff=vb1 - vb_last
#            val=(float(meter.meter_qb))*4/5
#            print vb_last, vb_diff, val 
#            if vb_diff < val:
#              warn=1
#            else:
#              warn=0
                       
        else:
            print ("firstdata of this meter\n")
            new_id = 1;
            warn=False

        qb_s = str(qb)
        vb_s = str(vb1)+'.'+str(vb2)
        new_data = Data(data_id=new_id, meter_id=meter.meter_id, meter_eui=eui_str, data_warn=warn, data_vb=vb_s, data_qb=qb_s)
        new_data.data_date = datetime.datetime.now()
        new_data.save()

    if data_type == 7:
        payload = data[12:(12+length)]
        battery, vm2, vb2, vm1, vb1, pres, temp, qm, qb = struct.unpack("!HHHIIffff", payload)
        meter_data=Data.objects.filter(meter_eui=eui_str).order_by('-data_id')
        if len(meter_data) > 0:
            new_id = meter_data[0].data_id + 1
 #           vb_last=float(meter_data[0].data_vb)
 #           vb_diff=vb1 - vb_last
 #           val=(float(meter.meter_qb))*4/5
 #           print vb_last, vb_diff, val 
 #           if vb_diff < val:
 #             warn=1
 #           else:
 #             warn=0
                       
        else:
            print ("firstdata for this meter\n")
            new_id = 1;
        warn=False
        battery_s = str(battery)
        vb_s = str(vb1)+'.'+str(vb2)
        vm_s = str(vm1)+'.'+str(vm2)      
        p_s = str(pres)
        t_s = str(temp)
        qb_s = str(qb)
        qm_s = str(qm)
        new_data = Data(data_id=new_id, meter_id=meter.meter_id, meter_eui=eui_str, data_battery=battery_s, data_warn=warn, data_vb=vb_s, data_vm=vm_s, data_p=p_s, data_t=t_s, data_qb=qb_s, data_qm=qm_s)
        new_data.data_date = datetime.datetime.now()
        new_data.save()

SerSock.close()
