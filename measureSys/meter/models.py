from django.db import models

from django.contrib import admin

class User(models.Model):
    user_id = models.CharField(max_length=24)
    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=10)
    user_company = models.CharField(max_length=200)
    user_addr = models.CharField(max_length=200)
    user_phone = models.CharField(max_length=20)
    user_index = models.CharField(max_length=200)
    user_total = models.CharField(max_length=200)
    user_lastmonth = models.CharField(max_length=200)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.user_name
    
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_index', 'user_addr', 'user_total', 'user_lastmonth')

class Meter(models.Model):
    meter_id = models.IntegerField(default=0)
    user_id = models.CharField(max_length=24)
    meter_name = models.CharField(max_length=200)
    meter_type = models.IntegerField(default=0)
    meter_index = models.CharField(max_length=200)
    meter_eui = models.CharField(max_length=200)
    user_meterdata = models.CharField(max_length=200)
    user_revise = models.CharField(max_length=200)
    user_reviseid = models.CharField(max_length=200)
    meter_qb = models.CharField(max_length=200)
    meter_qm = models.CharField(max_length=200)
    def __unicode__(self):              # __unicode__ on Python 2
        return "name: "+self.meter_name+"meter EUI64: "+ self.meter_eui
        
class MeterAdmin(admin.ModelAdmin):
    list_display = ('meter_id',  'meter_name', 'meter_type', 'meter_index', 'meter_eui', 'user_meterdata', 'user_revise', 'user_reviseid')

class Data(models.Model):
    data_id = models.IntegerField(default=0)
    meter_id = models.IntegerField(default=0)
    meter_eui = models.CharField(max_length=200)
    data_warn = models.IntegerField(default=0)
    data_date = models.DateTimeField('date published')
    data_vb = models.CharField(max_length=200)
    data_vm = models.CharField(max_length=200)
    data_p = models.CharField(max_length=200)
    data_t = models.CharField(max_length=200)
    data_qb = models.CharField(max_length=200)
    data_qm = models.CharField(max_length=200)

class DataAdmin(admin.ModelAdmin):
    list_display = ('data_id', 'meter_id', 'data_date', 'data_vb', 'data_vm', 'data_p', 'data_t', 'data_qb', 'data_qm')
    
class MeterType(models.Model):
    meter_type = models.IntegerField(default=0)
    meter_type_name = models.CharField(max_length = 200)
    def __uincode__(self):
        return "meter_type: "+self.meter_type

class MeterTypeAdmin(admin.ModelAdmin):
    list_display = ('meter_type', 'meter_type_name')
    
class DataWarnType(models.Model):
    data_warn = models.IntegerField(default = 0)
    data_warn_reason = models.CharField(max_length = 200)
    def __uincode__(self):
        return "warn_type: " +self.data_warn
class WarnInfo(models.Model):
    meter_eui = models.CharField(max_length=200)
    data_warn = models.IntegerField(default = 0)
    warn_level = models.CharField(max_length=24)
    warn_date = models.DateTimeField('date published')
    warn_solution = models.CharField(max_length=200)
    warn_other = models.CharField(max_length=200)
    warn_date = models.DateTimeField('date published')
    def __uincode__(self):
        return "meter_eui: " +self.meter_eui + "data_warn " + self.data_warn 
        
class DataWarnTypeAdmin(admin.ModelAdmin):
    list_display = ('warn_type', 'warn_type_reason')
    
    
class Company(models.Model):
    user_id = models.CharField(max_length=24)
    company_title = models.CharField(max_length=200)
    company_content = models.CharField(max_length=200)
    company_contract = models.CharField(max_length=200)
    company_tel = models.CharField(max_length=200)
    company_addr = models.CharField(max_length=200)
    def __uincode__(self):
        return "user_id: "+self.user_id+ " company_title: "+self.company_title+ " content "+ self.company_content

class UserFeedback(models.Model):
    user_id = models.CharField(max_length=24)
    report_time = models.DateTimeField('date published')
    solution_deadline = models.CharField(max_length=200)
    problem = models.CharField(max_length=200)
    solution_result = models.CharField(max_length=200)
    def __uincode__(self):
        return "user_id: "+self.user_id+ " report_time: "+self.report_time+ " solution_deadlie "+ self.solution_deadline + " problem: "+ self.problem 

class IdentificationMeter(models.Model):
    meter_eui = models.CharField(max_length=200)
    meter_type = models.IntegerField(default=0)
    meter_version = models.CharField(max_length=200)
    meter_index = models.CharField(max_length=200)
    output_range = models.CharField(max_length=200)
    identify_date = models.DateTimeField('date published')
    next_identify_date = models.DateTimeField('date published')
    medium = models.CharField(max_length=200)
    pressure = models.CharField(max_length=200)
    temperature = models.CharField(max_length=200)
    Qmax100 = models.CharField(max_length=200)
    Qmax60 = models.CharField(max_length=200)
    Qmax40 = models.CharField(max_length=200)
    Qmax20 = models.CharField(max_length=200)
    Qmax10 = models.CharField(max_length=200)
    def __uincode__(self):
        return "meter_eui: "+self.meter_eui+ " meter_type: "+self.meter_type+ " meter_index "+ self.meter_index + " output_range: "+ self.output_range 


admin.site.register(User, UserAdmin)
admin.site.register(Meter, MeterAdmin)
admin.site.register(Data, DataAdmin)
# Create your models here.
