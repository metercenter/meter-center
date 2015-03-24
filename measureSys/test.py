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

import dbhandle

while True:
    total = dbhandle.lastday_total(0001)
    print total
 
