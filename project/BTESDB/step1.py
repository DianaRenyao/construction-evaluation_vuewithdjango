from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from BTESDB.models import Project,User_Info
from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
from django.views.decorators.csrf import csrf_exempt


def step1(request):
    print(1)
    response={}
    #获取表单数据
    try:
        print(2)
        project=int(request.GET['project'])
        project_name=request.GET['project_name']
        client_name=request.GET['client_name']
        project_description=request.GET['project_description']
        project_leader=request.GET['project_leader']
        username=request.GET['username']
        this_user=User_Info.objects.get(username=username)
        if len(project_name)==0:
            response['msg']='项目名称不能为空！'
            response['error_num']=1
            return JsonResponse(response)
        elif Project.objects.filter(user=this_user,project_name=project_name).exists() and project==0:
            response['msg']='项目名称不得重复！'
            response['error_num']=1
            return JsonResponse(response)
        
        if len(client_name)==0:
            response['msg']='客户名称不能为空！'
            response['error_num']=1
            return JsonResponse(response)
        if len(project_leader)==0:
            response['msg']='项目负责人不能为空！'
            response['error_num']=1
            return JsonResponse(response)
        if len(project_description)==0:
            response['msg']='项目描述不能为空！'
            response['error_num']=1
            return JsonResponse(response)
        
        if project!=0:
            print('更新')
            update=Project.objects.get(id=project)
            #对数据进行更新
            update.project_name=project_name
            update.client_name=client_name
            update.project_description=project_description
            update.project_leader=project_leader
            try:
                update.save()
                response['msg']='项目信息修改成功！'
                response['error_num']=0
            except Exception as e:
                print (str(e))
                response['msg']=str(e)
                response['error_num']=1
            return JsonResponse(response)
        
        #获取user外键
        #this_user=User_Info.objects.get(username='13051997327')

        response['error_num']=0
        response['msg']='success'
        print(3)
        
    except Exception as e:
        print (4)    
        print (str(e))
        response['msg']=str(e)
        response['error_num']= 1
    return JsonResponse(response)
        
 