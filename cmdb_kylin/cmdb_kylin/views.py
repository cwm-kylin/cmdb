#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'kylin'
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
import django


from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    return render(request,'index.html')



def acc_login(request):
    if request.method == "POST":

        username = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            print " django.utils.timezone.now() ", django.utils.timezone.now()
            print "user.valid_begin_time",user.valid_begin_time
            print "user.valid_end_time",user.valid_end_time
            if django.utils.timezone.now() > user.valid_begin_time and django.utils.timezone.now()  < user.valid_end_time:
                auth.login(request,user)
                request.session.set_expiry(60*30)
                #print 'session expires at :',request.session.get_expiry_date()
                return HttpResponseRedirect('/')
            else:
                return render(request,'login.html',{'login_err': 'User account is expired,please contact your IT guy for this!'})

        else:
            return render(request,'login.html',{'login_err': 'Wrong username or password!'})
    else:
        return render(request, 'login.html')
