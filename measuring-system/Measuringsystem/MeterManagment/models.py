import datetime
from django.utils import timezone
from django.db import models

from django.contrib import admin

class User(models.Model):
    user_id = models.IntegerField(default=0)
    user_name = models.CharField(max_length=200)
    user_index = models.CharField(max_length=200)
    user_addr = models.CharField(max_length=200)
    user_total = models.CharField(max_length=200)
    user_lastmonth = models.CharField(max_length=200)
    user_password = models.CharField(max_length=10, blank = True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.user_name
    
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_index', 'user_addr', 'user_total', 'user_lastmonth')

class Meter(models.Model):
    meter_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    meter_name = models.CharField(max_length=200)
    meter_type = models.IntegerField(default=0)
    meter_index = models.CharField(max_length=200)
    meter_eui = models.CharField(max_length=200)
    user_meterdata = models.CharField(max_length=200)
    user_revise = models.CharField(max_length=200)
    user_reviseid = models.CharField(max_length=200)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.meter_name
    
class MeterAdmin(admin.ModelAdmin):
    list_display = ('meter_id', 'user_id', 'meter_name', 'meter_type', 'meter_index', 'meter_eui', 'user_meterdata', 'user_revise', 'user_reviseid')

class Data(models.Model):
    data_id = models.IntegerField(default=0)
    meter_id = models.IntegerField(default=0)
    data_date = models.DateTimeField('date published')
    data_vb = models.CharField(max_length=200)
    data_vm = models.CharField(max_length=200)
    data_p = models.CharField(max_length=200)
    data_t = models.CharField(max_length=200)
    data_qb = models.CharField(max_length=200)
    data_qm = models.CharField(max_length=200)

class DataAdmin(admin.ModelAdmin):
    list_display = ('data_id', 'meter_id', 'data_date', 'data_vb', 'data_vm', 'data_p', 'data_t', 'data_qb', 'data_qm')
    
    
class UserGroup(models.Model):
    user_id = models.CharField(max_length = 24)
    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=10)
    def __unicode__(self):              # __unicode__ on Python 2
        return 'ID: '+ self.user_name + ' name: ' +self.user_password + ' password '+ self.user_id
    
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_index', 'user_addr', 'user_total', 'user_lastmonth')


admin.site.register(User, UserAdmin)
admin.site.register(Meter, MeterAdmin)
admin.site.register(Data, DataAdmin)
# Create your models here.
