import datetime
from django.utils import timezone
from django.db import models

class Item(models.Model):
    item_id = models.IntegerField(default=0)
    item_name = models.CharField(max_length=200)
    item_addr = models.CharField(max_length=200)
    item_data = models.IntegerField(default=0)
    item_lastdate = models.DateTimeField('date published')
    def __unicode__(self):              # __unicode__ on Python 2
        return self.item_name

# Create your models here.
