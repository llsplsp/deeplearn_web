#coding=utf-8
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render

from account.models import UserInfo

def experts_vol(request):
    """展示志愿者名单"""
    user = User.objects.get(username=request.user.username)
    userinfo_all = UserInfo.objects.get(user=user)

    userinfo_vol = UserInfo.objects.filter(userClass='1')#所有的志愿者
    id_vol = userinfo_vol.values_list('user_id')

    user_vol=[]
    for i in range(len(userinfo_vol)):
        user_vol.append(User.objects.get(id=id_vol[i][0]))

    all_vol = zip(user_vol,userinfo_vol)

    return render(request, 'experts/volunteer.html', {'all_vol': all_vol,
                                                      "userinfo_all": userinfo_all})

def experts_pro(request):
    """展示专家名单"""
    user = User.objects.get(username=request.user.username)
    userinfo_all = UserInfo.objects.get(user=user)


    userinfo_exp = UserInfo.objects.filter(userClass='2')
    id_exp = userinfo_exp.values_list('user_id')

    user_exp = []
    for i in range(len(userinfo_exp)):
        user_exp.append(User.objects.get(id=id_exp[i][0]))

    all_exp = zip(user_exp,userinfo_exp,)

    return render(request, 'experts/professor.html', {'all_exp': all_exp,
                                                "userinfo_all": userinfo_all})
