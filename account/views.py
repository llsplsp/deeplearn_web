from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import LoginForm, RegistrationForm, UserForm, UserInfoForm
from .models import UserInfo

def user_home(request):
    """主页"""
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        userinfo_all = UserInfo.objects.get(user=user)
        return render(request,'home.html',{'user':user,'userinfo_all':userinfo_all})
    else:
        return render(request, 'home.html')

def user_login(request):
    """用户登录视图函数"""
    if request.method=="POST":
        login_form=LoginForm(request.POST) #request.POST表示用户提交的数据
        if login_form.is_valid(): #验证输入数据是否合法
            cd=login_form.cleaned_data #引入字典类型的数据，以键值对形式记录用用户名和密码
            user=authenticate(username=cd['username'],password=cd['password'])
            # 该函数作用是检验用户是否为注册的用户以及密码是否正确，要同时满足

            if user: #如果是注册了的用户
                login(request, user)
                user1 = User.objects.get(username=cd['username'])
                userinfo_all = UserInfo.objects.get(user=user1)

                return render(request, "home.html",{'user':user1,'userinfo_all':userinfo_all})

            else:
                return render(request,"./account/loginFail.html",locals())
        else:
            return render(request,"./account/loginFail.html",locals())

    if request.method=="GET":
        login_form=LoginForm()
        return render(request,"account/login.html",{"form":login_form})

def registerSuccess(request):
    return render(request,'./account/registerSuccess.html')

def register(request):
    """注册的响应函数"""
    if request.method=="POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():#is_valid() 检查数据是否符合要求
            new_user = user_form.save(commit=False)
            #1.将表单数据保存到数据库，并生成该数据的对象，commit=false表示只生成对象，先不存数据库
            new_user.set_password(user_form.cleaned_data['password'])#密码校验
            new_user.save()#2.再次保存，这次保存到数据库里面
            UserInfo.objects.create(user=new_user)

            return HttpResponseRedirect(reverse("account:register_success"))

        else:
            return render(request,'account/registerFail.html')
    else:
        user_form = RegistrationForm()
        return render(request,'account/register.html',{"form":user_form})


def user_logout(request):
    '''用户退出'''
    logout(request)
    return render(request,'account/logout.html')

@login_required(login_url='/account/login') #装饰器，判断用户是否登录，没有登陆时跳转到login_url
def myself(request):
    """显示个人信息"""
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=user)
    return render(request, "account/myself.html", {"user": user, "userinfo_all": userinfo})

@login_required(login_url='/account/login')
def myself_edit(request):
    """修改个人信息"""
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user, 'userinfo') else UserInfo.objects.create(user=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() * userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            request.user.email = user_cd['email']
            userinfo.phone = userinfo_cd['phone']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            request.user.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my-information/')#实现转向，用户提交的修改信息点击保存后执行

    else:
        user_form = UserForm(instance=request.user)
        user = User.objects.get(username=request.user.username)
        userinfo_all = UserInfo.objects.get(user=user)
        userinfo_form = UserInfoForm(initial={"phone": userinfo.phone, "company": userinfo.company, "profession": userinfo.profession, "address": userinfo.address, "aboutme": userinfo.aboutme, "userClass": userinfo.userClass})
        return render(request, "account/myself_edit.html", {"user_form": user_form, "userinfo_form": userinfo_form,"userinfo_all": userinfo_all})

@login_required(login_url='/account/login')
def my_image(request):
    """用户修改头像"""
    user = User.objects.get(username=request.user.username)
    userinfo = UserInfo.objects.get(user=user)
    if request.method == 'POST':
        # 后端拿前端传来的头像数据，保存到数据库
        userinfo.photo = request.FILES['photo']
        userinfo.save()

        return HttpResponseRedirect('/account/my-information/')
    else:
        return render(request,'./account/imagecrop.html',{"userinfo_all":userinfo})

@login_required(login_url='/account/login/')
def user_manage(request):
    """管理员管理用户"""
    user = User.objects.get(username=request.user.username)
    userinfo_all = UserInfo.objects.get(user=user)
    user_all = User.objects.all()
    userinfo = UserInfo.objects.all()
    all = zip(user_all,userinfo) #以列表形式遍历所有的数据
    # 验证登录用户是管理员
    if userinfo_all.userClass=='3' :
        return render(request,'./account/manage_user.html',{'all':all,"userinfo_all":userinfo_all})
    else:
        return HttpResponse("你没有删除操作的权限。")

@login_required(login_url='/account/login/')
def user_delete(request, user_id):
    """删除用户"""
    user_every = User.objects.get(id=user_id)
    user_every.delete()
    return redirect("account:manage_user")

@login_required(login_url='/userprofile/login/')
def user_update(request,id):
    """管理员修改个人信息"""
    user = User.objects.get(username=request.user.username)
    userinfo_all = UserInfo.objects.get(user=user)  #加载头部

    user_id = User.objects.get(id=id).id
    user1 = User.objects.filter(id=user_id).first()
    user2= UserInfo.objects.filter(user_id=user_id).first()

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        userclass=request.POST.get('userClass')
        phone =request.POST.get('phone')
        profession = request.POST.get('profession')
        address = request.POST.get('address')
        UserInfo.objects.filter(user_id=user_id).update(userClass=userclass,
        phone=phone,profession=profession,address=address)
        User.objects.filter(id=user_id).update(username=username,email=email)

        return HttpResponseRedirect('/account/manage-user/')

    return render(request, './account/update_user.html', locals())

