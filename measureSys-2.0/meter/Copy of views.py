#coding=utf8
from django.shortcuts import render_to_response
from meter.models import Meter, MeterType, DataWarnType
from meter.models import User
from meter.models import Data, WarnInfo
from meter.models import Company, UserFeedback, IdentificationMeter, outputDiff
from django.http import HttpResponse
from django.utils import formats
import json
from datetime import datetime
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import csv
import sys  
import datetime
from django.db.models import Sum


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
            return render_to_response('angulerMain.html', context_instance=RequestContext(request))
    except:
        print('session has been closed')
    return render_to_response('angulerMain.html', context_instance=RequestContext(request))

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
        if 'user_id' in request.GET:
            userID = request.GET['user_id']
        else:
            userID = request.session['user_id']
        each = Meter.objects.filter(user_id = userID)
        identData = IdentificationMeter.objects.filter(meter_eui = each[0].meter_eui).order_by('-id')
        if len(identData) > 0:
            outputMin =  identData[0].outputMin,
            outputMax =  identData[0].outputMax,
            pressureMin =  identData[0].pressureMin,
            pressureMax = identData[0].pressureMax,
            temperatureMin = identData[0].temperatureMin,
            temperatureMax = identData[0].temperatureMax,
            valid_time = formats.date_format(identData[0].next_identify_date,"SHORT_DATETIME_FORMAT"),
            meter_version = identData[0].meter_version,
            meter_index = identData[0].meter_index
        else:  
            outputMin =  '',
            outputMax =  '',
            pressureMin =  '',
            pressureMax = '',
            temperatureMin = '',
            temperatureMax = '',
            valid_time = '',
            meter_version = '',
            meter_index = '',     
        each_dict = {
              "meter_id": each[0].meter_id,
              "user_id": each[0].user_id,
              "meter_name": each[0].meter_name,
              "meter_type": meterTypeName(each[0].meter_type),
              "meter_index": each[0].meter_index,
              "meter_eui": each[0].meter_eui,              
              "user_meterdata": each[0].user_meterdata,
              "user_revise": each[0].user_revise,              
              "user_reviseid": each[0].user_reviseid,
              "meter_qm":each[0].meter_qm,
              "meter_qb":each[0].meter_qb,
              "outputMin": outputMin,
              "outputMax": outputMax,
              "pressureMin": pressureMin,
              "pressureMax": pressureMax,
              "temperatureMin": temperatureMin,
              "temperatureMax": temperatureMax,
              "valid_time" : valid_time,
              "meter_version": meter_version,
              "meter_index":meter_index 
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
            user = User.objects.get(user_company = request.GET['user_name'])
            meter = Meter.objects.get(user_id = user.user_id)
            if 'start' in request.GET and 'limit' in request.GET:
                start = request.GET['start']
                limit = request.GET['limit']
            else:
                start = 0
                limit = Data.objects.filter(meter_eui = meter.meter_eui).count()
            for each in Data.objects.filter(meter_eui = meter.meter_eui).order_by('-data_date')[start:start+limit]:
                each_dict = {
                    "id": each.pk,
                    "data_id": each.data_id,
                    "meter_eui":     each.meter_eui,
                    "data_date": formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"),
                    "data_vb": each.data_vb,
                    "data_vm": each.data_vm,
                    "data_p":     each.data_p,
                    "data_t": each.data_t,
                    "data_qb": each.data_qb,    
                    "data_qm": each.data_qm,  
                    "data_battery": each.data_battery,        
                }
        #         print(formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"))
                responsedata.append(each_dict)
            response = {}
            response['status'] = 'SUCESS'
            response['totalCount'] = Data.objects.filter(meter_eui = meter.meter_eui).count()
            response['data'] = responsedata
    #     print(json.dumps(response))
        return HttpResponse(json.dumps(response),content_type ="application/json")
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
            return render_to_response('angularMain.html', context_instance=RequestContext(request))
#         print("=================")
        username = request.POST['login-username']
        password = request.POST['login-password']
        user = User.objects.get(user_name = username, user_password = password)
        if user.user_id is not None:
            request.session['user_id'] = user.user_id
            return render_to_response('angularMain.html', context_instance=RequestContext(request))
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
    user_group_json = '['+generateTreeJSON(userID)+']';
    return HttpResponse(user_group_json,content_type ="application/json")

def generateTreeJSON(user_id):
#     firstChild = User.objects.filter(user_id__range = (user_id,user_id[0:-1]+str(int(user_id[-1])+1))).extra(where = ['LENGTH(user_id) > ' + str(len(user_id))]).extra(select = { 'minValue' : "MIN(user_id)" })
    firstChild = User.objects.filter(user_id__startswith = user_id).extra(where = ['LENGTH(user_id) > ' + str(len(user_id))]).order_by('user_id')
    myself = User.objects.filter(user_id = user_id)
    if len(firstChild ) == 0 and len(user_id) > 8: 
        #is leaf node
        return '{"name" : "'+myself[0].user_company+'", "value": "fa-tachometer", "visible" : false, "nodes": []}'
    else:
        if len(firstChild) == 0 and len(user_id) <= 8:
        #is leaf node
            return '{"name" : "'+myself[0].user_company+'", "value": "fa-user", "visible" : true, "nodes": []}'
        else:
        #is parent node
            children = User.objects.filter(user_id__startswith = user_id).extra(where = ['LENGTH(user_id) = ' + str(len(firstChild[0].user_id))])
            strJson = ''
            for each in children:
                strJson = strJson + generateTreeJSON(each.user_id) + ', '
            strJson = strJson[0:-2] 
            return '{"name" : "'+myself[0].user_company+'", "value": "fa-group", "visible": true, "nodes" : ['+strJson+']}'

# def user_group_show(request):
#     if  not 'user_id' in request.session:
#         loginPage(request)
#         return render_to_response('login.html', context_instance=RequestContext(request))
#     print request.session['user_id']
#     userID = User.objects.get(user_id = request.session['user_id']).user_id
# #     userID = '0001'
#     user_group_json = '{ "children": '+generateTreeJSON(userID)+'}';
#     return HttpResponse(user_group_json,content_type ="application/json")
# 
# def generateTreeJSON(user_id):
# #     firstChild = User.objects.filter(user_id__range = (user_id,user_id[0:-1]+str(int(user_id[-1])+1))).extra(where = ['LENGTH(user_id) > ' + str(len(user_id))]).extra(select = { 'minValue' : "MIN(user_id)" })
#     firstChild = User.objects.filter(user_id__startswith = user_id).extra(where = ['LENGTH(user_id) > ' + str(len(user_id))]).order_by('user_id')
#     myself = User.objects.filter(user_id = user_id)
#     if len(firstChild) == 0:
#         #is leaf node
#         return '{"text" : "'+myself[0].user_company+'", "leaf" : true}'
#     else:
#         #is parent node
#         children = User.objects.filter(user_id__startswith = user_id).extra(where = ['LENGTH(user_id) = ' + str(len(firstChild[0].user_id))])
#         strJson = ''
#         for each in children:
#             strJson = strJson + generateTreeJSON(each.user_id) + ', '
#         strJson = strJson[0:-2] 
#         return '{"text" : "'+myself[0].user_company+'", "expanded": true, "children" : ['+strJson+']}'
    
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

def getIndUser(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    responsedata = []
    if not 'user_id' in request.GET:
        userID = request.session['user_id']
    else:
        userID = request.GET['user_id']
    for each in User.objects.filter(user_id__startswith = userID).extra(where = ['LENGTH(user_id) = 8']):
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

def getIndComp (request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    responsedata = []
    for each in User.objects.filter(user_id__startswith = request.session['user_id']).extra(where = ['LENGTH(user_id) = 4']):
        each_dict = {
            "user_id": each.user_id,
            "gas_company":     each.user_company,    
        }
#         print(formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"))
        responsedata.append(each_dict)
    response = {}
    response['status'] = 'SUCCESS'
    response['data'] = responsedata
#     print(json.dumps(response))
    return HttpResponse(json.dumps(responsedata),content_type ="application/json")       

def getIndMeter(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    responsedata = []
    if not 'user_id' in request.GET:
        user_id = request.GET['user_id']
    else:
        user_id = request.session['user_id']
    for each in Meter.objects.filter(user_id__startswith = user_id):
        each_dict = {
            "user_id": each.user_id,
            "meter_eui":     each.meter_eui,    
        }
#         print(formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"))
        responsedata.append(each_dict)
    response = {}
    response['status'] = 'SUCCESS'
    response['data'] = responsedata
#     print(json.dumps(response))
    return HttpResponse(json.dumps(responsedata),content_type ="application/json")    
 

def selectPanel(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    responsedata = []
    if 'user_name' in request.GET:
            user = User.objects.filter(user_company = request.GET['user_name'])
    else:
            user = User.objects.filter(user_id = request.session['user_id'])
    for each in user:
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
    userName = request.POST['user']
    userPassword = request.POST['pass']
    userCompany = request.POST['company']
    userPhone = request.POST['phone']
    userParent = request.POST['user_company']
    user = User();
    user.user_name = userName
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
    ID = children[0].user_id
    for i in range(1,len(children)):
        if int(children[i].user_id) - int(ID) >1:
            return str(int(ID)+1).zfill(16)
        else:
            ID = children[i].user_id
            
    return str(int(ID)+1).zfill(16)

def register_meter(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    response = {}
    meterName = request.POST['meter_name']
    meterEUI = request.POST['meter_eui']
    meterType = request.POST['meter_type']
#     userRevise = request.POST['user_revise']
#     meterQb = request.POST['meter_qb']
#     meterQm = request.POST['meter_qm']
    meterUser = request.POST['user_company']
    metertypelist = MeterType.objects.get(meter_type_name = meterType)
    meteSet = Meter.objects.filter(meter_eui = meterEUI)
    if meteSet.count() != 0:
        response['status'] = 'FAILURE'
        response['data'] =  '您输入的流量计标示已存在，请重新输入'
        return HttpResponse(json.dumps(response),content_type ="application/json")
    meter = Meter();
    meter.meter_name = meterName;
    meter.meter_eui = meterEUI
    meter.meter_type = metertypelist.meter_type
#     meter.user_revise = userRevise
#     meter.meter_qb = meterQb
#     meter.meter_qm = meterQm
    meter.user_id = generateMeterID(meterUser)
    meter.save();
    
    #add user
    user = User();
    user.user_id = meter.user_id
    user.user_company = meter.meter_name
    user.save();
   
    response['status'] = 'SUCCESS'
    response['data'] = {}
#     print(json.dumps(response))
    return HttpResponse(json.dumps(response),content_type ="application/json")

def getExcelFile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Data.csv"'
    #database operation3
    writer = csv.writer(response)
    writer.writerow(['Accept Time', 'Vb(Nm3)', 'Vm(m3)','P','T','Qb(Nm3/h)','Qm(m3/h)'])
    try:
        if 'user_company' in request.GET:
            userID = getUserId(request.GET['user_company'])
            Children = Meter.objects.filter(user_id__startswith = userID)
            print "meter num is : "+ str(len(Children))
            for i in range (0, len(Children)):
                meterID = Meter.objects.filter(user_id = Children[i].user_id)
                for j in range(0,len(meterID)):
                    meterName = meterID[j].meter_name
                    for each in Data.objects.filter(meter_eui = meterID[j].meter_eui):
                        writer.writerow([formats.date_format(each.data_date,"SHORT_DATETIME_FORMAT"), each.data_vb, each.data_vm, each.data_p, each.data_t,each.data_qb,each.data_qm])
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

def getCompanyInfo(request):
    responsedata = []
    response = {}
    response['status'] = 'SUCCESS'
    try:
#         if 'user_id' in request.session:
#             return render_to_response('index.html', context_instance=RequestContext(request))
        company = Company.objects.all()
        each_dict = {
            "title": company[0].company_title,
            "content":company[0].company_content, 
            "addr":company[0].company_addr, 
            "contract":company[0].company_contract, 
            "tel":company[0].company_tel,    
        }
        responsedata.append(each_dict)
        response['status'] = 'SUCCESS'
        response['data'] = responsedata
        print responsedata
        return HttpResponse(json.dumps(responsedata),content_type ="application/json")
    except:
        print ('user does not exist')
        response['status'] = 'FAILURE'
        response['data'] = ''
        return HttpResponse(json.dumps(responsedata),content_type ="application/json")
    
def getUserFeedback(request):
    responsedata = []

    for each in UserFeedback.objects.all():
        each_dict = {
            "id": each.pk,
            "user_company": getUserCompanyName(each.user_id),
            "report_time":     formats.date_format(each.report_time,"SHORT_DATETIME_FORMAT"),
            "solution_deadline": each.solution_deadline,
            "problem": each.problem,
            "solution_result": each.solution_result,
        }
        responsedata.append(each_dict)
    response = {}
    response['status'] = 'SUCESS'
    response['data'] = responsedata
    return HttpResponse(json.dumps(response),content_type ="application/json") 
    
def getIndentificationMeter(request):
    responsedata = []

    for each in IdentificationMeter.objects.order_by('-id'):
        each_dict = {
            "id": each.pk,
            "user_company": getUserName(each.meter_eui),
            "meter_eui": each.meter_eui,
            "identify_date":     formats.date_format(each.identify_date,"SHORT_DATETIME_FORMAT"),
            "next_identify_date":     formats.date_format(each.next_identify_date,"SHORT_DATETIME_FORMAT"),
            "meter_type": meterTypeName(each.meter_type),
            "meter_index": each.meter_index,
            "meter_version": each.meter_version,
            "output_range": each.outputMin+'~'+each.outputMax,
            "medium": each.medium,
            "pressure": each.pressureMin+'~'+each.pressureMax,
            "temperature": each.temperatureMin+'~'+each.temperatureMax,
            "Qmax100": each.Qmax100,
            "Qmax60": each.Qmax60,
            "Qmax40": each.Qmax40,
            "Qmax20": each.Qmax20,
            "Qmax10": each.Qmax10,
        }
        responsedata.append(each_dict)
    response = {}
    response['status'] = 'SUCESS'
    response['data'] = responsedata
    return HttpResponse(json.dumps(response),content_type ="application/json")

def addIndentificationMeter(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    response = {}
    meter_eui = request.POST['meter_eui']
    meter_type = request.POST['meter_type']
    meter_version = request.POST['meter_version']
    meter_index = request.POST['meter_index']
    identify_date = request.POST['identify_date']
    next_identify_date = request.POST['next_identify_date']
    medium = request.POST['medium']
    pressureMax = request.POST['pressureMax']
    pressureMin = request.POST['pressureMin']
    temperatureMax = request.POST['temperatureMax']
    temperatureMin = request.POST['temperatureMin']
    outputMax = request.POST['outputMax']
    outputMin = request.POST['outputMin']
    Qmax100 = request.POST['Qmax100']
    Qmax60 = request.POST['Qmax60']
    Qmax40 = request.POST['Qmax40']   
    Qmax20 = request.POST['Qmax20']
    Qmax10 = request.POST['Qmax10']   
             
    indMeter = IdentificationMeter()
    indMeter.meter_eui = meter_eui
    indMeter.meter_type = meter_type
    indMeter.meter_version = meter_version
    indMeter.meter_index = meter_index
    indMeter.identify_date = datetime.datetime.strptime(identify_date,'%Y-%m-%d')
    indMeter.next_identify_date = datetime.datetime.strptime(next_identify_date,'%Y-%m-%d')
    indMeter.medium = medium
    indMeter.outputMax = outputMax
    indMeter.outputMin = outputMin
    indMeter.pressureMax = pressureMax
    indMeter.pressureMin = pressureMin
    indMeter.temperatureMax = temperatureMax
    indMeter.temperatureMin = temperatureMin
    indMeter.Qmax100 = Qmax100
    indMeter.Qmax60 = Qmax60
    indMeter.Qmax40 = Qmax40
    indMeter.Qmax20 = Qmax20
    indMeter.Qmax10 = Qmax10
    indMeter.save();
   
    response['status'] = 'SUCCESS'
    response['data'] = {}
#     print(json.dumps(response))
    return HttpResponse(json.dumps(response),content_type ="application/json")  

def getUserId(company):
    user = User.objects.get(user_company = company)
    return user.user_id
def getUserCompanyName(userId):
    user = User.objects.get(user_id = userId)
    return user.user_company


def addOutputDiff(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    response = {}
    input = request.POST['input']
    industry_output = request.POST['industry_output']
    resident_output = request.POST['resident_output']
    other_output = request.POST['other_output']
    output_diff = request.POST['output_diff']
    output_date = request.POST['output_date']
    user_company = request.POST['user_company']
    outputInfo = outputDiff();
    outputInfo.input = input
    outputInfo.industry_output = industry_output
    outputInfo.resident_output = resident_output
    outputInfo.other_output = other_output
    outputInfo.output_diff = output_diff
    outputInfo.output_date = datetime.datetime.strptime(output_date,'%Y-%m-%d')
    outputInfo.user_id = getUserId(user_company)
    outputInfo.save();
    
   
    response['status'] = 'SUCCESS'
    response['data'] = {}
#     print(json.dumps(response))
    return HttpResponse(json.dumps(response),content_type ="application/json")
def modifyOutputDiff(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    response = {}
    input = request.POST['input']
    industry_output = request.POST['industry_output']
    resident_output = request.POST['resident_output']
    other_output = request.POST['other_output']
    output_diff = request.POST['output_diff']
    output_date = request.POST['output_date']
    user_company = request.POST['user_company']
    outputInfo = outputDiff.objects.get(user_id = getUserId(user_company), output_date = datetime.datetime.strptime(output_date,'%Y-%m-%d'));
    outputInfo.input = input
    outputInfo.industry_output = industry_output
    outputInfo.resident_output = resident_output
    outputInfo.other_output = other_output
    outputInfo.output_diff = output_diff
    outputInfo.output_date = datetime.datetime.strptime(output_date,'%Y-%m-%d')
    outputInfo.user_id = getUserId(user_company)
    outputInfo.save();
    
   
    response['status'] = 'SUCCESS'
    response['data'] = {}
#     print(json.dumps(response))
    return HttpResponse(json.dumps(response),content_type ="application/json")
    
    
    
def outputDiffChart(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    responsedata = []
    if 'user_company' in request.GET:
        userID = getUserId(request.GET['user_company'])
        

        for each in outputDiff.objects.filter(user_id = userID):
            each_dict = {
                "id": each.pk,
                "output_diff": int(each.output_diff),
                "output_date":     formats.date_format(each.output_date,"DATE_FORMAT"),
            }
            responsedata.append(each_dict)
        response = {}
        response['status'] = 'SUCESS'
        response['data'] = responsedata
        return HttpResponse(json.dumps(response),content_type ="application/json")
        

    for each in outputDiff.objects.all():
        each_dict = {
            "id": each.pk,
            "output_diff": int(each.output_diff),
            "output_date":     formats.date_format(each.output_date,"DATE_FORMAT"),
        }
        responsedata.append(each_dict)
    response = {}
    response['status'] = 'SUCESS'
    response['data'] = responsedata
    return HttpResponse(json.dumps(response),content_type ="application/json")
    
def retrieveNodeNum(request):
    if 'user_company' in request.GET:
        userID = getUserId(request.GET['user_company'])
        meterSet = Meter.objects.filter(user_id__startswith = userID)
        each_dict = {
                "all_node_num": meterSet.count(),
                "valid_node_num": meterSet.count(),
        }
        responsedata = []
        responsedata.append(each_dict)
        response = {}
        response['status'] = 'SUCCESS'
        response['data'] = responsedata
        return HttpResponse(json.dumps(response),content_type ="application/json") 
    
def getMeterName(meterEUI):
    meter = Meter.objects.get(meter_eui = meterEUI)
    return meter.meter_name
def getUserName(meterEUI):
    meter = Meter.objects.get(meter_eui = meterEUI)
    userID =  meter.user_id[0:8]
    user = User.objects.get(user_id = userID)
    return user.user_company
def getGasCompany(meterEUI):
    meter = Meter.objects.get(meter_eui = meterEUI)
    userID =  meter.user_id[0:4]
    user = User.objects.get(user_id = userID)
    return user.user_company    
    
def getWarnInfo(request):
    if 'user_company' in request.GET:
        responsedata = []
        userID = getUserId(request.GET['user_company'])  
        meterSet = Meter.objects.filter(user_id__startswith = userID)
        for i in range (0, len(meterSet)):
            warnInfoSet = WarnInfo.objects.filter(meter_eui = meterSet[i].meter_eui)
            for j in range(0,len(warnInfoSet)):
                warnData = DataWarnType.objects.get(data_warn = warnInfoSet[j].data_warn)
                if 'warn_level' in request.GET:
                    if warnData.data_warn_level == request.GET['warn_level']:
                        each_dict = {
                            "data_warn": warnInfoSet[j].data_warn,
                            "warn_date": formats.date_format(warnInfoSet[j].warn_date,"SHORT_DATETIME_FORMAT"),
                            "meter_info": getMeterName(warnInfoSet[j].meter_eui),
                            "other": warnInfoSet[j].warn_other,
                            "solution": warnData.data_warn_solution,
                            "warn_level": warnData.data_warn_level,
                            "warn_info" : warnData.data_warn_reason,
                            "company": getGasCompany(warnInfoSet[j].meter_eui),
                            "user_id": getUserName(warnInfoSet[j].meter_eui),
                        }       
                        responsedata.append(each_dict)
                    else:
                        continue
                else:       
                    each_dict = {
                        "data_warn": warnInfoSet[j].data_warn,
                        "warn_date": formats.date_format(warnInfoSet[j].warn_date,"SHORT_DATETIME_FORMAT"),
                        "meter_info": getMeterName(warnInfoSet[j].meter_eui),
                        "other": warnInfoSet[j].warn_other,
                        "solution": warnData.data_warn_solution,
                        "warn_level": warnData.data_warn_level,
                        "warn_info" : warnData.data_warn_reason,
                        "company": getGasCompany(warnInfoSet[j].meter_eui),
                        "user_id": getUserName(warnInfoSet[j].meter_eui),
                    }       
                    responsedata.append(each_dict)
        response = {}
        response['status'] = 'SUCCESS'
        response['data'] = responsedata
        return HttpResponse(json.dumps(response),content_type ="application/json")
    
def changeCompanyIntro(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    response = {}
    company_title = request.POST['company_title']
    company_content = request.POST['company_content']
    company_contract = request.POST['company_contract']
    company_tel = request.POST['company_tel']
    company_addr = request.POST['company_addr']
    
    company = Company.objects.get(id = 2);
    company.company_title = company_title
    company.company_content = company_content
    company.company_contract = company_contract
    company.company_tel = company_tel
    company.company_addr = company_addr
    company.save();
    
   
    response['status'] = 'SUCCESS'
    response['data'] = {}
#     print(json.dumps(response))
    return HttpResponse(json.dumps(response),content_type ="application/json")

def AddUserFeedback(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    response = {}
    report_time = request.POST['report_time']
    solution_deadline = request.POST['solution_deadline']
    problem = request.POST['problem']
    solution_result = request.POST['solution_result']
    user_company = request.POST['user_company']
    
    feedback = UserFeedback()
    feedback.user_id = getUserId(user_company)
    feedback.report_time = datetime.datetime.strptime(report_time,'%Y-%m-%d')
    feedback.solution_deadline = solution_deadline
    feedback.problem = problem
    feedback.solution_result = solution_result
    feedback.save();
    
   
    response['status'] = 'SUCCESS'
    response['data'] = {}
#     print(json.dumps(response))
    return HttpResponse(json.dumps(response),content_type ="application/json")  

def getDeviationVal(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    responsedata = []
    if 'meter_eui' in request.GET:
        meterEUI = request.GET['meter_eui']
        dataQm = request.GET['data_qm']
        meterIdent = IdentificationMeter.objects.filter(meter_eui = meterEUI).order_by('-id')
        each_dict = {
#             "qmax_level": '10%Qmax'+str(round(float(meterIdent[0].outputMax)*0.1,1)),
            "deviation_val": round(float(meterIdent[0].Qmax10),2),
            "qmax_level": 0.1,
        }
        responsedata.append(each_dict)
        each_dict = {
#             "qmax_level": '20%Qmax'+str(round(float(meterIdent[0].outputMax)*0.2,1)),
            "deviation_val": round(float(meterIdent[0].Qmax20),2),
            "qmax_level": 0.2,
        }
        responsedata.append(each_dict)
        each_dict = {
#             "qmax_level": '40%Qmax'+str(round(float(meterIdent[0].outputMax)*0.4,1)),
            "deviation_val": round(float(meterIdent[0].Qmax40),2),
            "qmax_level": 0.4,
        }
        responsedata.append(each_dict)
        each_dict = {
#             "qmax_level": '60%Qmax'+str(round(float(meterIdent[0].outputMax)*0.6,1)),
            "deviation_val": round(float(meterIdent[0].Qmax60),2),
            "qmax_level": 0.6,
        }
        responsedata.append(each_dict)
        each_dict = {
#             "qmax_level": '100%Qmax'+str(round(float(meterIdent[0].outputMax),1)),
            "deviation_val": round(float(meterIdent[0].Qmax100),2),
            "qmax_level": 1,
        }
        responsedata.append(each_dict)
        each_dict = {
#             "qmax_level": '100%Qmax'+str(round(float(meterIdent[0].outputMax),1)),
            "single_deviation_val": 0,
            "single_qmax_level": (float(dataQm)/float(meterIdent[0].outputMax)*4)
        }
        responsedata.append(each_dict)
        
    response = {}
    response['status'] = 'SUCESS'
    response['data'] = responsedata
    return HttpResponse(json.dumps(response),content_type ="application/json")

def retrieveIndustryOutput(request):
    if 'user_company' in request.GET:
        userID = getUserId(request.GET['user_company'])
        meterSet = Meter.objects.filter(user_id__startswith = userID)
        today = datetime.datetime.today()
        yestoday = today - datetime.timedelta(days=1)
        outputVal = 0
        for meter in meterSet:
            MeterData = Data.objects.filter(meter_eui = meter.meter_eui, data_date__lt = today.strftime("%Y-%m-%d %H:%M:%S"), data_date__gt = yestoday.strftime("%Y-%m-%d %H:%M:%S")).order_by('-data_date')
            if len(MeterData) > 0:
                outputVal = outputVal + float(MeterData[0].data_qm)
            else:
                outputVal = outputVal + 0
        each_dict = {
                "industry_output": outputVal,
        }
        responsedata = []
        responsedata.append(each_dict)
        response = {}
        response['status'] = 'SUCCESS'
        response['data'] = responsedata
        return HttpResponse(json.dumps(response),content_type ="application/json") 
    
def meterDataChart(request):
    if  not 'user_id' in request.session:
        loginPage(request)
        return render_to_response('login.html', context_instance=RequestContext(request))
    responsedata = []
    if 'user_company' in request.GET:
        userID = getUserId(request.GET['user_company'])
        
        meterEUISet = Meter.objects.filter(user_id__startswith = userID).values_list('meter_eui', flat=True)

        for each in Data.objects.filter(meter_eui__in = meterEUISet).extra({'published':"date(data_date)"}).values('published').annotate(dsum=Sum('data_qb')):
            each_dict = {
                "data_qb": int(each["dsum"]),
#                 "data_date":     formats.date_format(each.published,"DATE_FORMAT"),
                "data_date": each["published"]
            }
            responsedata.append(each_dict)
    response = {}
    response['status'] = 'SUCESS'
    response['data'] = responsedata
    return HttpResponse(json.dumps(response),content_type ="application/json")