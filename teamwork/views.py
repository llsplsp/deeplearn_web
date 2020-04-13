from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView

from account.models import UserInfo
from teamwork.models import TeamWorkWrite
from django.core.paginator import Paginator #分页
import markdown
from .forms import writeTeamworkForm
from django.db.models import Q #引入Q对象

import redis
from django.conf import settings
r = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

def teamWork(request):
    """工作概况标题"""
    search = request.GET.get('search') #用于搜索
    if search:
        workWrite_all=TeamWorkWrite.objects.filter(
            Q(title__icontains=search)|
            Q(body__contains=search)
        ).order_by('-publish')
        #多个Q对象用管道符|隔开，就达到了联合查询的目的。
    else:
        search=''
        workWrite_new = TeamWorkWrite.objects.all().order_by('-total_views')
        order_new=[workWrite_new[0],workWrite_new[1],workWrite_new[2],workWrite_new[3],workWrite_new[4]]
        workWrite_all = TeamWorkWrite.objects.all()

    paginator = Paginator(workWrite_all,5)#每页显示10条记录
    page = request.GET.get('page')#获取url的页码

    workWrite=paginator.get_page(page)

    if request.user.is_authenticated:
        user1 = User.objects.get(username=request.user.username)
        userinfo_all = UserInfo.objects.get(user=user1)
    return render(request, './teamwork/teamwork_title.html', locals())

# class TeamworkListView(ListView):
#     """基于类的视图"""
#     # 上下文的名称
#     context_object_name = 'workWrite'
#     # 查询集
#     queryset = TeamWorkWrite.objects.all()
#     # 模板位置
#     template_name = 'teamwork/teamwork_title.html'
#
#     def get_context_data(self, **kwargs):
#         # 获取原有的上下文
#         context = super().get_context_data(**kwargs)
#         # 增加新上下文
#         context['order_new'] = 'total_views'
#         return context
#     # def get(self,request):
#     #     search = request.GET.get('search')  # 用于搜索
#     #     if search:
#     #         workWrite_all=TeamWorkWrite.objects.filter(
#     #                 Q(title__icontains=search)|
#     #                 Q(body__contains=search)
#     #             ).order_by('-publish')
#     #     else:
#     #         search=''
#     #         workWrite_new = TeamWorkWrite.objects.all().order_by('-total_views')
#     #         order_new=[workWrite_new[0],workWrite_new[1],workWrite_new[2],workWrite_new[3],workWrite_new[4]]
#     #         workWrite_all = TeamWorkWrite.objects.all()
#     #
#     #     paginator = Paginator(workWrite_all, 5)  # 每页显示10条记录
#     #     page = request.GET.get('page')  # 获取url的页码
#     #     workWrite = paginator.get_page(page)
#     #
#     #     if request.user.is_authenticated:
#     #         user1 = User.objects.get(username=request.user.username)
#     #         userinfo_all = UserInfo.objects.get(user=user1)
#     #     return render(request, './teamwork/teamwork_title.html', locals())


#Django自动生成的用于索引数据表的主键（Primary Key，即pk）
def teamWork_content(request,workcontent_id): #workcontent_id有了它才有办法知道到底应该取出哪篇文章。
    """工作概况的详细"""
    teamwork = get_object_or_404(TeamWorkWrite,id=workcontent_id)#出现没有存在的页面id时报错404最好
    teamwork.total_views += 1
    teamwork.save(update_fields=['total_views'])
    # 将markdown语法渲染成html样式
    teamwork.body = markdown.markdown(teamwork.body,
                    extensions=[
                        # 包含 缩写、表格等常用扩展
                        'markdown.extensions.extra',
                        # 语法高亮扩展
                        'markdown.extensions.codehilite',
                    ])
    """
    第二个参数载入了常用的语法扩展，markdown.extensions.extra中包括了缩写、表格等扩展，
    markdown.extensions.codehilite则是后面要使用的代码高亮扩展。
    """
    pub = teamwork.publish
    if request.user.is_authenticated:
        user1 = User.objects.get(username=request.user.username)
        userinfo_all = UserInfo.objects.get(user=user1)
        return render(request, './teamwork/teamwork_content.html', {'teamwork':teamwork, "publish":pub, 'userinfo_all':userinfo_all}) #render将数据渲染到指定的html页面
    else:
        return render(request, './teamwork/teamwork_content.html',{'teamwork': teamwork, "publish": pub})

@login_required(login_url='/account/login/')
def teamwork_write(request):
    """管理员写工作概述"""
    if request.method=='POST':
        teamwork_post_form = writeTeamworkForm(data=request.POST)#将提交的数据赋值到表单实例中
        if teamwork_post_form.is_valid():
            new_teamwork=teamwork_post_form.save(commit=False)
            new_teamwork.author=User.objects.get(username=request.user.username)
            new_teamwork.save()
            return redirect("teamwork:team_work")
    else:
        # 创建表单类实例
        teamwork_post_form = writeTeamworkForm()
        user1 = User.objects.get(username=request.user.username)
        userinfo_all = UserInfo.objects.get(user=user1)
        # 赋值上下文
        context = {'teamwork_post_form': teamwork_post_form,'userinfo_all':userinfo_all}
        # 返回模板
        return render(request, 'teamwork/create_teamwork.html', context)

@login_required(login_url='/account/login/')
def teamwork_delete(request,workcontent_id):

    teamwork = TeamWorkWrite.objects.get(id=workcontent_id)# 根据 id 获取需要删除的文章
    teamwork.delete()      # 调用.delete()方法删除文章
    return redirect("teamwork:team_work")

@login_required(login_url='/account/login/')
def teamwork_update(request,workcontent_id):
    """修改"""
    # 获取需要修改的具体工作概况文章的对象
    teamwork= TeamWorkWrite.objects.get(id=workcontent_id)
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        teamwork_post_form = writeTeamworkForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if teamwork_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            teamwork.title = request.POST['title']
            teamwork.body = request.POST['body']
            teamwork.save()
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            return redirect("teamwork:work_detail", workcontent_id=workcontent_id)
    else:
        # 创建表单类实例
        teamwork_post_form = writeTeamworkForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = { 'teamwork': teamwork, 'teamwork_post_form': teamwork_post_form }
        # 将响应返回到模板中
        return render(request, 'teamwork/teamwork_update.html', context)