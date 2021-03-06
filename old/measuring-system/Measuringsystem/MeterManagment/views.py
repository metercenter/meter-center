# coding=utf8
from django.shortcuts import render_to_response
from MeterManagment.models import Meter
from MeterManagment.models import User
from MeterManagment.models import Data, UserGroup
from django.http import HttpResponse
from django.utils import formats
import json
from datetime import datetime
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def mainPage(request):
#     return render_to_response('index.html')
    return render_to_response('index.html', context_instance=RequestContext(request))

def loginPage(request):
#     return render_to_response('login.html')
    return render_to_response('login.html', context_instance=RequestContext(request))

def getMeter(request):
    posts = Meter()
    posts.meter_id = 1
    posts.user_id = 2
    posts.meter_name = '流量计'
    posts.meter_type =  1
    posts.meter_index = 3
    posts.meter_eui = 'eui64'
    posts.user_meterdata = '1,2,3,4'
    posts.user_revise = '1'
    posts.user_reviseid = '2,3,4,5'
    posts.save()
    responseData = []
    for each in  Meter.objects.all():
        each_dict = {
              "meter_id": each.meter_id,
              "user_id": each.user_id,
              "meter_name": each.meter_name,
              "meter_type": each.meter_type,
              "meter_index": each.meter_index,
              "meter_eui": each.meter_eui,              
              "user_meterdata": each.user_meterdata,
              "user_revise": each.user_revise,              
              "user_reviseid": each.user_reviseid,
            }
        responseData.append(each_dict)
    response = {}
    response['status'] = 'SUCESS'
    response['data'] = responseData
    return HttpResponse(json.dumps(response), content_type="application/json")
    return render_to_response('index.html')

def userList(requst):
    post = User()
    post.user_name = '张三'
    post.user_addr = 'xiaole18393@cisco.com'
    post.user_total = '管理员'
    post.user_lastmonth = '1998-3-4'
    post.save()
#     responsedata = serializers.serialize("json", UserList.objects.all())
    userlist =  User.objects.all()
    responsedata = []
    for user in userlist:
        user_dict = {
            "id": user.pk,
            "Username": user.user_name,
            "Email":     user.user_addr,
            "Roles": user.user_total,
            "LastLoginDate": user.user_lastmonth,
        }
        responsedata.append(user_dict)
    response = {}
    response['status'] = 'SUCESS'
    response['data'] = responsedata
    return HttpResponse(json.dumps(response),content_type ="application/json")

def getData(requst):
#     print('before')
#     post = Data()
#     post.data_id = 1
#     post.meter_id = 2
#     post.data_vb = '12'
#     post.data_vm = '23'
#     post.data_p = '34'
#     post.data_t = '45'
#     post.data_qb = '56'
#     post.data_qm = '78'
#     post.save()
#     print('after')
#     data_id = models.IntegerField(default=0)
#     meter_id = models.IntegerField(default=0)
#     data_date = models.DateTimeField('date published')
#     data_vb = models.CharField(max_length=200)
#     data_vm = models.CharField(max_length=200)
#     data_p = models.CharField(max_length=200)
#     data_t = models.CharField(max_length=200)
#     data_qb = models.CharField(max_length=200)
#     data_qm = models.CharField(max_length=200)
#     print(datetime.now());
    responsedata = []
    for each in Data.objects.all():
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
    
def login_view(request):    
    user = authenticate(username=request.POST['login-username'], password=request.POST['login-password'])
    print (user)
    if user is not None:
        login(request, user)    
        print request.user    
        try:
#             dbuser = User.objects.get(user_name = request.POST['login-username'], user_password = request.POST['login-password'])
#             if dbuser is not None:
            return render_to_response('index.html', context_instance=RequestContext(request))
        except User.DoesNotExist:
            print('user does not exist')
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return render_to_response('login.html', context_instance=RequestContext(request))


def user_group_show(request):
    user_id = UserGroup.objects.get(id = 0).user_id
    user_group_json = generateTreeJSON(user_id);
    print(user_group_json)
    response = {}
    response['status'] = 'SUCESS'
    response['data'] = user_group_json
#     return HttpResponse(json.dumps(response),content_type ="application/json")
    return HttpResponse(user_group_json,content_type ="application/json")

def generateTreeJSON(user_id):
    firstChild = UserGroup.objects.filter(user_name__range = (user_id,user_id[0:-1]+str(int(user_id[-1])+1))).extra(where = ['LENGTH(user_name) > ' + str(len(user_id))]).extra(select = { 'minValue' : "MIN(user_name)" })
    myself = UserGroup.objects.filter(user_name = user_id)
    if firstChild[0].user_name is None:
        #is leaf node
        return '{"text" : "'+myself[0].user_password+'", "leaf" : true}'
    else:
        #is parent node
        children = UserGroup.objects.filter(user_name__range = (user_id,user_id[0:-1]+str(int(user_id[-1])+1))).extra(where = ['LENGTH(user_name) = ' + str(len(firstChild[0].user_name))])
        strJson = ''
        for each in children:
            strJson = strJson + generateTreeJSON(each.user_name) + ', '
        strJson = strJson[0:-2] 
        return '{"text" : "'+myself[0].user_password+'", "children" : ['+strJson+']}'