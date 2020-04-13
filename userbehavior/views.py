from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render

from account.models import UserInfo

@login_required(login_url='/account/login/')
def userBehavior(request):
    """记录用户行为"""
    user = User.objects.get(username=request.user.username)
    userinfo_all = UserInfo.objects.get(user=user)
    user_all = User.objects.all()
    userinfo = UserInfo.objects.all()


    all = zip(user_all, userinfo)  # 以列表形式遍历所有的数据
    return render(request, './userbehavior/user_behavior.html', {'all': all, "userinfo_all": userinfo_all})



