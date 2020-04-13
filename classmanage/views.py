from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from account.models import UserInfo
from classmanage.models import Paper, Grade, Question


@login_required(login_url='/account/login/')
def classManage(request):
    """开始答题按钮和计时界面"""
    user = User.objects.get(username=request.user.username)
    userinfo_all = UserInfo.objects.get(user=user)  # 用于访问用户的等级
    return render(request,'./classmanage/start.html',{"userinfo_all":userinfo_all})

@login_required(login_url='/account/login/')
def classManageSubject(request):
    """等级管理，答题升级，志愿者，专家。"""
    user = User.objects.get(username=request.user.username)
    userinfo_all = UserInfo.objects.get(user=user)
    paper = Paper.objects.filter(for_user=userinfo_all.userClass)# 查询考试信息
    grade = Grade.objects.filter(user_id=user.id)# 查询成绩信息

    return render(request, './classmanage/userchange.html',
                  {'user':user,'userinfo_all':userinfo_all,'paper': paper, 'grade': grade})

@login_required(login_url='/account/login/')
def startExam(request):
    """用户考试"""
    user = User.objects.get(username=request.user.username)
    userinfo_all = UserInfo.objects.get(user=user)  # 用于访问用户的等级
    paper=Paper.objects.filter(for_user=userinfo_all.userClass)
    subject1=paper[0].subject
    # print("paper值:", paper)
    return render(request,'./classmanage/exam.html',{'student':user,'paper':paper,'subject':subject1})

@login_required(login_url='/account/login/')
def calGrade(request):
    if request.method=='POST':
        # 得到学号和科目
        sid=request.POST.get('user_id')
        subject1 = request.POST.get('subject')

        # 重新生成Student实例，Paper实例，Grade实例，名字和index中for的一致，可重复渲染
        userinfo_all= UserInfo.objects.get(user_id=sid)
        # grade = Grade.objects.filter(user_id=userinfo_all.user_id)

        # 计算该门考试的学生成绩
        question = Paper.objects.filter(for_user=userinfo_all.userClass).values("timu_id").values('timu_id__id','timu_id__answer','timu_id__score')

        mygrade=0#初始化一个成绩为0
        for p in question:
            qId=str(p['timu_id__id'])#int 转 string,通过pid找到题号
            myans=request.POST.get(qId)#通过 qid 得到学生关于该题的作答
            # print(myans)
            okans=p['timu_id__answer']#得到正确答案
            # print(okans)
            if myans==okans:#判断学生作答与正确答案是否一致
                mygrade+=p['timu_id__score']#若一致,得到该题的分数,累加mygrade变量

        #向Grade表中插入数据
        Grade.objects.create(user_id_id=sid,subject=subject1,grade=mygrade)
        print("分数：",mygrade)
        user = User.objects.get(username=request.user.username)
        if mygrade>=90:
            if userinfo_all.userClass=='0':    #修改用户角色 普通用户--志愿者
                UserInfo.objects.filter(user_id=user.id).update(userClass='1')
            elif userinfo_all.userClass=='1':  #修改用户角色 志愿者---专家
                UserInfo.objects.filter(user_id=user.id).update(userClass='2')
            return render(request, './classmanage/answerSuccess.html',{'userinfo_all':userinfo_all,'mygrade':mygrade})
        else:
            return render(request, './classmanage/answerFail.html',{'userinfo_all':userinfo_all,'mygrade':mygrade})

        # 重新渲染index.html模板
        # return render(request,'./classmanage/passgrade.html',{'userinfo_all':userinfo_all,'grade':grade})