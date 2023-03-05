# -*-coding:utf-8 -*-
from datetime import datetime, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from BicycleApp import models
from BicycleApp.models import User, Admin, Bicycle, Record


def logout(request):
    response = HttpResponseRedirect('/login/')
    keys = request.COOKIES.keys()
    for one in keys:
        response.delete_cookie(one)
    return response


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == 'POST':
        msg = {'msg': '信息有误，请重新输入'}
        role = request.POST.get('role_')
        name = request.POST.get('name_')
        pwd = request.POST.get('pwd_')
        if role == 'user':
            try:
                data_u = User.objects.get(username=name, userpwd=pwd)
                if data_u:
                    logtime = datetime.now()+ timedelta(hours=8)
                    User.objects.filter(username=name).update(logtime=logtime)
                    response = HttpResponseRedirect('/index_u/')
                    response.set_cookie(
                        key='name', value=name, expires=datetime.now() + timedelta(days=1))
                    return response
            except:
                return render(request, 'login.html', msg)
        elif role == 'admin':
            try:
                data_a = Admin.objects.get(adminname=name, adminpwd=pwd)
                if data_a:
                    response = HttpResponseRedirect('/index_a/')
                    response.set_cookie(
                        key='name', value=name, expires=datetime.now() + timedelta(days=1))
                    return response
            except:
                return render(request, 'login.html', msg)
        else:
            return render(request, 'login.html', {'msg': '没有选择角色'})


def register(request):
    reg_time = datetime.now() + timedelta(hours=8)
    if request.method == "GET":
        return render(request, 'register.html', {"reg_time": reg_time})
    if request.method == "POST":
        try:
            name = request.POST.get('username_')
            pwd = request.POST.get('userpwd_')
            try:
                if User.objects.get(username=name):
                    return render(request, 'register.html', {'msg': '用户名已存在，请重新填写'})
            except:
                pass
            if name == '' or pwd == '':
                return render(request, 'register.html', {'msg': '信息不能为空'})
            User.objects.create(username=name, userpwd=pwd, regtime=reg_time)
            return render(request, 'register.html', {'msg': '注册成功'})
        except:
            return render(request, 'register.html', {'msg': '请确保信息填写正确'})


def index_a(request):
    if request.method == "GET":
        bicycles = Bicycle.objects.all()
        user = request.COOKIES.get('name', '')
        print(user)
        return render(request, 'index_a.html', {'bicycles': bicycles})
    if request.method == "POST":
        try:
            carid_ = request.POST.get("input_carid")
            search_ = Bicycle.objects.filter(carid=carid_)
        except:
            search_ = Bicycle.objects.all()
            return render(request, 'index_a.html', {'bicycles': search_})
        if search_:
            return render(request, 'index_a.html', {'bicycles': search_})
        else:
            records = {}
            return render(request, 'index_a.html', {'bicycles': records})


def bicycleinfo(request):
    user = request.COOKIES.get('name', '')
    bicycles = Bicycle.objects.all()
    return render(request, 'bicycleinfo.html', {'bicycles': bicycles, 'user': user})


def updatebicycle(request):
    user = request.COOKIES.get('name', '')
    carid = request.GET.get('update_carid')
    c_info = Bicycle.objects.get(carid=carid)
    if request.method == "POST":
        c_info.carid = request.POST.get('cid_')
        c_info.carbrand = request.POST.get('carbrand_')
        c_info.layplace = request.POST.get('layplace_')
        c_info.status = request.POST.get('status_')
        c_info.save()
    return render(request, 'updatebicycle.html', {'c_info': c_info, 'user': user})


def delbicycle(request):
    carid = request.GET.get('delete_carid')
    Bicycle.objects.filter(carid=carid).delete()
    user = request.COOKIES.get('name', '')
    bicycles = Bicycle.objects.all()
    return render(request, 'bicycleinfo.html', {'user': user, 'bicycles': bicycles})


def addbicycle(request):
    if request.method == "GET":
        user = request.COOKIES.get('name', '')
        return render(request, 'addbicycle.html', {'user': user})
    if request.method == "POST":
        carbrand = request.POST.get('carbrand_')
        layplace = request.POST.get('layplace_')
        status = request.POST.get('status_')
        Bicycle.objects.create(
            carbrand=carbrand, layplace=layplace, status=status)
        user = request.COOKIES.get('name', '')
        bicycles = Bicycle.objects.all()
        return render(request, 'bicycleinfo.html', {'user': user, 'bicycles': bicycles})


def userinfo(request):
    user = request.COOKIES.get('name', '')
    if request.method == "GET":
        users = User.objects.all()
        return render(request, 'userinfo.html', {'user': user, 'users': users})
    if request.method == "POST":
        users = User.objects.all()
        msg = request.POST.get('input_username')
        try:
            input_ = User.objects.filter(username=msg)
        except:
            return render(request, "userinfo.html", {"users": users})
        if input_.count() == 0:
            return render(request, "userinfo.html", {"users": users})
        if input_:
            return render(request, "userinfo.html", {"users": input_})


def recordinfo(request):
    user = request.COOKIES.get('name', '')
    if request.method == "GET":
        records = Record.objects.all()
        return render(request, 'recordinfo.html', {'user': user, 'records': records})
    if request.method == "POST":
        records = Record.objects.all()
        carid_ = request.POST.get("input_carid")
        try:
            search_ = Record.objects.filter(carid=carid_)
        except:
            return render(request, 'recordinfo.html', {'records': records, 'user': user})
        if search_.count() == 0:
            return render(request, 'recordinfo.html', {'user': user, 'records': records})
        if search_:
            return render(request, 'recordinfo.html', {'records': search_, 'user': user})
        else:
            return render(request, 'recordinfo.html', {'records': records, 'user': user})


def index_u(request):
    bicycle_use = Bicycle.objects.filter(status='空闲')
    if request.method == "GET":
        user = request.COOKIES.get('name', '')
        bicycle_use = Bicycle.objects.filter(status='空闲')
        return render(request, 'index_u.html', {'bicycles': bicycle_use, 'user': user})
    if request.method == "POST":
        try:
            carid = request.POST.get('input_carid')
        except:
            return render(request, 'index_u.html', {'bicycles': bicycle_use})
        try:
            bicycle_use = Bicycle.objects.filter(carid=carid, status='空闲')
        except:
            return render(request, 'index_u.html', {'bicycles': bicycle_use})
        return render(request, 'index_u.html', {'bicycles': bicycle_use})


def bookingcar(request):
    user = request.COOKIES.get('name', '')
    carid = request.GET.get('bookingcarid')
    borrowplace = Bicycle.objects.filter(carid=carid).values('layplace')[
        0].get('layplace')
    borrowtime = datetime.now()+ timedelta(hours=8)
    Record.objects.create(carid=carid, borrowplace=borrowplace,
                          borrowtime=borrowtime, username=user)
    Bicycle.objects.filter(carid=carid).update(status='使用中')
    bicycle_use = Bicycle.objects.filter(status='空闲')
    return render(request, 'index_u.html', {'bicycles': bicycle_use, 'user': user})


def userrecord(request):
    user = request.COOKIES.get('name', '')
    userrecords = Record.objects.filter(username=user)
    return render(request, 'userrecord.html', {'user': user, 'userrecords': userrecords})


def returncar(request):
    user = request.COOKIES.get('name', '')
    userrecords = Record.objects.filter(
        username=user, returntime=None, returnplace=None)
    return render(request, 'returncar.html', {'user': user, 'userrecords': userrecords})


def returncar_o(request):
    re_time = datetime.now()+ timedelta(hours=8)
    user = request.COOKIES.get('name', '')
    recordid = request.GET.get('recordid_')
    carid_ = Record.objects.filter(id=recordid).values('carid')[0].get('carid')
    if request.method == 'GET':
        c = Record.objects.get(id=recordid)
        return render(request, 'returncar_o.html', {'user': user, 'c': c, 're_time': re_time})
    if request.method == "POST":
        returnplace = request.POST.get('returnplace_')
        Record.objects.filter(id=recordid).update(
            returnplace=returnplace, returntime=re_time)
        Bicycle.objects.filter(carid=carid_).update(
            status='空闲', layplace=returnplace)
        userrecords = Record.objects.filter(
            username=user, returntime=None, returnplace=None)
        return render(request, 'returncar.html', {'user': user, 'userrecords': userrecords})


def usercarinfo(request):
    if request.method == "GET":
        user = request.COOKIES.get('name', '')
        username = request.GET.get('user_name')
        records = Record.objects.filter(username=username)
        return render(request, 'usercarinfo.html', {'user': user, 'userrecords': records})


def usercarinfo2(request):
    carid = request.GET.get('car_id')
    records = Record.objects.filter(carid=carid)
    return render(request, 'usercarinfo.html', {'userrecords': records})
