import os, sys
sys.path.append('../')
os.environ["DJANGO_SETTINGS_MODULE"] = "measureSys.settings"

from django.contrib.auth.models import User
from meter.models import Meter
from meter.models import Data
import django
django.setup()

from socket import *
import datetime

def lastday_total(userid): 
  meterlist = Meter.objects.filter(user_id=userid)
  d1 = datetime.datetime.now()
  d2 = d1 + datetime.timedelta(days=-1)
  total = 0;
  for meter in meterlist:
      today_data=Data.objects.filter(meter_eui=meter.meter_eui,data_date=d1).order_by('-data_date')
      yestoday_data=Data.objects.filter(meter_eui=meter.meter_eui,data_date=d2).order_by('-data_date')

      if len(today_data) > 0 and len(yestoday_data) > 0:
          total = total + float(today_data[0].data_vb) - float(yestoday[0].data_vb)
  return total;
