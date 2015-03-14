# coding=utf8
from django.shortcuts import render_to_response
from meter.models import Meter, MeterType, DataWarnType
from meter.models import User
from meter.models import Data
from django.http import HttpResponse
from django.utils import formats
import json
from datetime import datetime
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import csv
import sys  



def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    csv.writer
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

# Create your views here.
@login_required(login_url='/login/')
def mainPage(request):
#     return render_to_response('index.html')
    try:
        if  not 'user_id' in request.session:
            return render_to_response('index.html', context_instance=RequestContext(request))
    except:
        print('session has been closed')
    return render_to_response('login.html', context_instance=RequestContext(request))

def loginPage(request):
#     return render_to_response('login.html')
    if 'user_id' in request.session:
        del request.session['user_id']
    # return render_to_response('login.html', context_instance=RequestContext(request))
    return render_to_response('login.html')

def meterTypeName(meter_type):
    meterType = MeterType.objects.get(meter_type = meter_type)
    return meterType.meter_type_name


def getMeter(request):
#     posts = Meter()
#     posts.meter_id = 1
#     user = User.objects.get(user_id = '0001000100000001')
#     posts.user = user
#     #posts.user_id = 2
#     posts.meter_name = '万达流量计'
#     posts.meter_type =  1
#     posts.user_id = '0001000100000001'
#     posts.meter_index = 3
#     posts.meter_eui = 'wandaguangchang'
#     posts.user_meterdata = '1,2,3,4'
#     posts.user_revise = '1'
#     posts.user_reviseid = '2,3,4,5'
#     posts.save()
    responseData = []
    try:
        if 'user_name' in request.GET:
            user = User.objects.get(user_company = request.GET['user_name'])
        else:
            user = User.objects.get(user_id = request.session['user_id'])
        
        user_id = user.user_id
        Children = Meter.objects.filter(user_id__range = (user_id,user_id[0:-1]+str(int(user_id[-1])+1))).extra(where = ['LENGTH(user_id) > ' + str(len(user_id))])
        for i in range (0, len(Children)):
#             print('==================')
#             print(Children[i].user_id)
#             print('==================')
            for each in  Meter.objects.filter(user_id = Children[i].user_id):
#                 print Children[i].user_id
                each_dict = {
                      "meter_id": each.meter_id,
                      "user_id": each.user_id,
                      "meter_name": each.meter_name,
                      "meter_type": meterTypeName(each.meter_type),
                      "meter_index": each.meter_index,
                      "meter_eui": each.meter_eui,              
                      "user_meterdata": each.user_meterdata,
                      "user_revise": each.user_revise,              
                      "user_reviseid": each.user_reviseid,
                      "meter_qm":each.meter_qm,
                      "meter_qb":each.meter_qb,
                }
                responseData.append(each_dict)
    except:
        print('user is not existed')
    response = {}
    response['status'] = 'SUCESS'
    response['data'] = responseData
    return HttpResponse(json.dumps(response), content_type="application/json")
    return render_to_response('index.html')

def getReason(warn_type):
    return DataWarnType.objects.get(data_warn = warn_type).data_warn_reason;

def warnList(request):
    responsedata = []
    try:
#         user = User.objects.get(user_id = request.session['user_id'])
        userlist =  User.objects.filter(user_id__startswith = request.session['user_id'])
        for each in userlist:
            meterlist = Meter.objects.filter(user_id__startswith = each.user_id)
            for meter in meterlist:
                datalist = Data.objects.filter(meter_eui = meter.meter_eui, data_warn__gt =  0)
                for data in datalist:
                    data_dict = {
                        "id": data.pk,
                        "data_date": formats.date_format(data.data_date,"SHORT_DATETIME_FORMAT"),
                        "data_vb":     data.data_vb,
                        "data_vm": data.data_vm,
                        "data_p": data.data_p,
                        "data_warn": getReason(data.data_warn),
                    }
                    responsedata.append(data_dict)
    except:
        print "user is not exsited"
    response = {}
    response['status'] = 'SUCESS'
    response['data'] = responsedata
    return HttpResponse(json.dumps(response),content_type ="application/json")    

def userList(request):
    try:
        user = User.objects.get(user_id = request.session['user_id'])
        userlist =  User.objects.filter(user_id__startswith = user.user_id)
        responsedata = []
        for user in userlist:
            user_dict = {
                "id": user.pk,
                "user_company": user.user_company,
                "user_name":     user.user_name,
                "user_password": user.user_password,
                "user_phone": user.user_phone,
            }
            responsedata.append(user_dict)
    except:
        print "user is not exsited"
    response = {}
    response['status'] = 'SUCESS'
    response['data'] = responsedata
    return HttpResponse(json.dumps(response),content_type ="application/json")

def getData(request):
    responsedata = []
    try:
        if 'user_name' in request.GET:
            request.session['user_name'] = request.GET['user_name']
            user = User.objects.get(user_company = request.GET['user_name'])
        elif 'meter_eui' in request.GET:
            request.session['meter_eui'] = request.GET['meter_eui']
            request.session['is_meter_eui'] = True 
            for each in Data.objects.filter(meter_eui = request.GET['meter_eui']):
                    each_dict = {
                        "id": each.pk,
                        "data_id": each.data_id,
                        "meter_id":     each.meter_id,
                        "data_date": formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"),
                        "data_vb": each.data_vb,
                        "data_vm": each.data_vm,
                        "data_p":     each.data_p,
                        "data_t": each.data_t,
                        "data_qb": each.data_qb,    
                        "data_qm": each.data_qm,          
                    }
            #         print(formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"))
                    responsedata.append(each_dict)
            response = {}
            response['status'] = 'SUCESS'
            response['data'] = responsedata
        #     print(json.dumps(response))
            return HttpResponse(json.dumps(response),content_type ="application/json")
        else:
            user = User.objects.get(user_id = request.session['user_id'])
            
        user_id = user.user_id
        Children = Meter.objects.filter(user_id__range = (user_id,user_id[0:-1]+str(int(user_id[-1])+1))).extra(where = ['LENGTH(user_id) > ' + str(len(user_id))])
    #         Children = Meter.objects.filter(user_id__startswith = user_id)
        for i in range (0, len(Children)):
            meterID = Meter.objects.filter(user_id = Children[i].user_id)
            for j in range(0,len(meterID)):
                for each in Data.objects.filter(meter_eui = meterID[j].meter_eui):
                    each_dict = {
                        "id": each.pk,
                        "data_id": each.data_id,
                        "meter_id":     each.meter_id,
                        "data_date": formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"),
                        "data_vb": each.data_vb,
                        "data_vm": each.data_vm,
                        "data_p":     each.data_p,
                        "data_t": each.data_t,
                        "data_qb": each.data_qb,    
                        "data_qm": each.data_qm,          
                    }
            #         print(formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"))
                    responsedata.append(each_dict)
    except:
        print('user is not existed')
    response = {}
    response['status'] = 'SUCESS'
    response['data'] = responsedata
#     print(json.dumps(response))
    return HttpResponse(json.dumps(response),content_type ="application/json")

def submit(request):
#     user = authenticate(username=request.POST['login-username'], password=request.POST['login-password'])
#     if user is None:
#         print(user)
#         return render_to_response('login.html', context_instance=RequestContext(request))
# ? User.objects.filter(user_name='张三').delete()
#     post = User()
#     post.user_name = 'root'
#     post.user_addr = 'xiaole18393@cisco.com'
#     post.user_total = '管理员'
#     post.user_lastmonth = '1998-3-4'
#     post.user_password = 'cisco123'
#     post.save()
#     mm = User.objects.all();
#     print('------------------------')
#     print(mm.first())
#     print('------------------------')
    if request.method == "POST":
            try:
                dbuser = User.objects.get(user_name = request.POST['login-username'], user_password = request.POST['login-password'])
                print(dbuser.user_addr)
                print request.POST['login-username']
                print request.POST['login-password']
                return render_to_response('index.html', context_instance=RequestContext(request))
            except User.DoesNotExist:
                print('user does not exist')
    return render_to_response('login.html', context_instance=RequestContext(request))

    
# def result(request):
#     
#     print("sb")
#     p = request.POST['answer']
#     return render_to_response('result.html', {'answer': p}, context_instance=RequestContext(request))
    
# def login_view1(request):    
#     user = authenticate(username=request.POST['login-username'], password=request.POST['login-password'])
#     print (user)
#     if user is not None:
#         login(request, user)    
#         print request.user    
#         try:
# #             dbuser = User.objects.get(user_name = request.POST['login-username'], user_password = request.POST['login-password'])
# #             if fordbuser is not None:
#             return render_to_response('index.html', context_instance=RequestContext(request))
#         except User.DoesNotExist:
#             print('user does not exist')
#     return render_to_response('login.html', context_instance=RequestContext(request))

def login_view(request):
    try:
        if 'user_id' in request.session:
            return render_to_response('index.html', context_instance=RequestContext(request))
#         print("=================")
        username = request.POST['login-username']
        password = request.POST['login-password']
        user = User.objects.get(user_name = username, user_password = password)
        if user.user_id is not None:
            request.session['user_id'] = user.user_id
            return render_to_response('index.html', context_instance=RequestContext(request))
    except:
        print ('user does not exist')
    loginPage(request)
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout_view1(request):
    logout(request)
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout_view(request):
    del request.session['user_id']
    if 'user_name' in request.session:
        del request.session['user_name']
    loginPage(request)
    return render_to_response('login.html', context_instance=RequestContext(request))

def user_group_show(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    print request.session['user_id']
    userID = User.objects.get(user_id = request.session['user_id']).user_id
#     userID = '0001'
    user_group_json = '{ "children": '+generateTreeJSON(userID)+'}';
    return HttpResponse(user_group_json,content_type ="application/json")

def generateTreeJSON(user_id):
#     firstChild = User.objects.filter(user_id__range = (user_id,user_id[0:-1]+str(int(user_id[-1])+1))).extra(where = ['LENGTH(user_id) > ' + str(len(user_id))]).extra(select = { 'minValue' : "MIN(user_id)" })
    firstChild = User.objects.filter(user_id__startswith = user_id).extra(where = ['LENGTH(user_id) > ' + str(len(user_id))]).order_by('user_id')
    myself = User.objects.filter(user_id = user_id)
    if len(firstChild) == 0:
        #is leaf node
        return '{"text" : "'+myself[0].user_company+'", "leaf" : true}'
    else:
        #is parent node
        children = User.objects.filter(user_id__startswith = user_id).extra(where = ['LENGTH(user_id) = ' + str(len(firstChild[0].user_id))])
        strJson = ''
        for each in children:
            strJson = strJson + generateTreeJSON(each.user_id) + ', '
        strJson = strJson[0:-2] 
        return '{"text" : "'+myself[0].user_company+'", "children" : ['+strJson+']}'
    
def user_level(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    responsedata = []
    for each in User.objects.filter(user_id__startswith = request.session['user_id']).extra(where = ['LENGTH(user_id) < 5']):
        each_dict = {
            "user_id": each.user_id,
            "user_company":     each.user_company,    
        }
#         print(formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"))
        responsedata.append(each_dict)
    response = {}
    response['status'] = 'SUCCESS'
    response['data'] = responsedata
#     print(json.dumps(response))
    return HttpResponse(json.dumps(responsedata),content_type ="application/json")

def meter_level(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    responsedata = []
    for each in User.objects.filter(user_id__startswith = request.session['user_id']).extra(where = ['LENGTH(user_id)  = 8']):
        each_dict = {
            "user_id": each.user_id,
            "user_company":     each.user_company,    
        }
#         print(formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"))
        responsedata.append(each_dict)
    response = {}
    response['status'] = 'SUCCESS'
    response['data'] = responsedata
#     print(json.dumps(response))
    return HttpResponse(json.dumps(responsedata),content_type ="application/json")

def generateID(userName):
    user = User.objects.filter(user_company__exact = userName)
    brother = User.objects.filter(user_id__startswith = user[0].user_id).extra(where = ['LENGTH(user_id) <= ' + str(len(user[0].user_id)+4)]).extra(where = ['LENGTH(user_id) > ' + str(len(user[0].user_id))]).order_by('user_id')
    if len(brother) == 0:
        if user[0].user_id == '00':
            return '0001'
        else:
            return user[0].user_id+'0001'
#     if len(brother) == 0:
#         return user[0].user_id+'0002'
    ID = brother[0].user_id
    for i in range(1,len(brother)):
        if int(brother[i].user_id) - int(ID) >1:
            return ID[0:-1]+str(int(ID[-1])+1)
        else:
            ID = brother[i].user_id
            
    return ID[0:-1]+str(int(ID[-1])+1)

def register_company(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    print request.POST['user']
    userName = request.POST['user']
    userPassword = request.POST['pass']
    userCompany = request.POST['company']
    userPhone = request.POST['phone']
    userParent = request.POST['user_company-inputEl']
    user = User();
    user.user_name = userName;
    user.user_password = userPassword
    user.user_company = userCompany
    user.user_phone = userPhone;
    user.user_id = generateID(userParent)
    user.save();
    response = {}
    response['status'] = 'SUCESS'
    response['data'] = {}
#     print(json.dumps(response))
    return HttpResponse(json.dumps(response),content_type ="application/json")

def generateMeterID(userName):
    user = User.objects.filter(user_company__exact = userName)
    children = Meter.objects.filter(user_id__startswith = user[0].user_id).extra(where = ['LENGTH(user_id) = ' + str(len(user[0].user_id)+8)]).order_by('user_id')
    if len(children) == 0:
        return user[0].user_id+'00000001'
#     if len(children) == 1:
#         return user[0].user_id+'00000002'
    ID = children[0].user_id
    for i in range(1,len(children)):
        if int(children[i].user_id) - int(ID) >1:
            return ID[0:-1]+str(int(ID[-1])+1)
        else:
            ID = children[i].user_id
            
    return ID[0:-1]+str(int(ID[-1])+1)

def register_meter(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    meterName = request.POST['meter_name']
    meterEUI = request.POST['meter_eui']
    meterType = request.POST['meter_type-inputEl']
    userRevise = request.POST['user_revise']
    meterQb = request.POST['meter_qb']
    meterQm = request.POST['meter_qm']
    meterUser = request.POST['user_company-inputEl']
    metertypelist = MeterType.objects.get(meter_type_name = meterType)
    
    meter = Meter();
    meter.meter_name = meterName;
    meter.meter_eui = meterEUI
    meter.meter_type = metertypelist.meter_type
    meter.user_revise = userRevise
    meter.meter_qb = meterQb
    meter.meter_qm = meterQm
    meter.user_id = generateMeterID(meterUser)
    meter.save();
    response = {}
    response['status'] = 'SUCESS'
    response['data'] = {}
#     print(json.dumps(response))
    return HttpResponse(json.dumps(response),content_type ="application/json")

def getExcelFile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Data.csv"'
    #database operation3
    writer = csv.writer(response)
    writer.writerow(['Name', 'Accept Time', 'Vb(Nm3)', 'Vm(m3)','P','T','Qb(Nm3/h)','Qm(m3/h)'])
    try:
        if 'user_name' in request.session:
            user = User.objects.get(user_company = request.session['user_name'])
        else:
            user = User.objects.get(user_id = request.session['user_id'])
            
        if 'meter_eui' in request.session:
            if request.session['is_meter_eui'] == True:
                request.session['is_meter_eui'] = False
                meterName = Meter.objects.get(meter_eui = request.session['meter_eui']).meter_name
                print "meter_name: "+ meterName
                for each in Data.objects.filter(meter_eui = request.session['meter_eui']):
                    writer.writerow([meterName.encode('utf-8'),  formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"), each.data_vb, each.data_vm, each.data_p, each.data_t,each.data_qb,each.data_qm])
                return response
        user_id = user.user_id
        
        print "user_id is " +user_id
        
#             Children = Meter.objects.filter(user_id__range = (user_id,user_id[0:-1]+str(int(user_id[-1])+1))).extra(where = ['LENGTH(user_id) > ' + str(len(user_id))])
        Children = Meter.objects.filter(user_id__startswith = user_id)
        print "meter num is : "+ str(len(Children))
        for i in range (0, len(Children)):
            meterID = Meter.objects.filter(user_id = Children[i].user_id)
            for j in range(0,len(meterID)):
                meterName = meterID[j].meter_name
                for each in Data.objects.filter(meter_eui = meterID[j].meter_eui):
                    writer.writerow([meterName.encode('utf-8'),  formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"), each.data_vb, each.data_vm, each.data_p, each.data_t,each.data_qb,each.data_qm])
            #         print(formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"))
    except:
        print('user is not existed')

    return response

def getMeterType(request):
    responsedata = []
    for each in MeterType.objects.all():
        each_dict = {
            "meter_type": each.meter_type,
            "meter_type_name":     each.meter_type_name,    
        }
#         print(formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"))
        responsedata.append(each_dict)
    response = {}
    response['status'] = 'SUCCESS'
    response['data'] = responsedata
#     print(json.dumps(response))
    return HttpResponse(json.dumps(responsedata),content_type ="application/json")
    