from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator #分页
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from account.models import UserInfo
from .models import Talk
from .forms import TalkForm
from notifications.signals import notify #引入消息通知
import datetime
from django.views import View

def userTalk(request):
    """用户交流"""
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    search = request.GET.get('search')  # 用于搜索
    if search:
        comment = Talk.objects.filter(
            Q(body__contains=search)
        ).order_by('-created')
    else:
        search = ''
        comment = Talk.objects.all()

    paginator = Paginator(comment, 20)  # 每页显示10条记录
    page = request.GET.get('page')  # 获取url的页码
    comments = paginator.get_page(page)


    if request.user.is_authenticated: #用于添加指定头部
        user = User.objects.get(username=request.user.username)
        userinfo_all = UserInfo.objects.get(user=user)

        user_photo=[]
        comment_form = TalkForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            user_photo = UserInfo.objects.get(user_id=request.user.id)
            new_comment.save()

        return render(request, './talk/userTalk.html', {'user_photo':user_photo,'nowtime':nowtime,
            'comment_form':comment_form,'user': user,"total":comment,
                'userinfo_all': userinfo_all, 'comments': comments,'search':search})

    else:
        comment_form = TalkForm()
        return render(request, './talk/userTalk.html', {'nowtime':nowtime,
            "total": comment,'comment_form':comment_form,
                                'comments': comments,'search': search})

def userReply(request,parent_comment_id=None):
    """二级评论"""
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    search = request.GET.get('search')  # 用于搜索
    if search:
        comment = Talk.objects.filter(
            Q(body__contains=search)
        ).order_by('-created')
    else:
        search = ''
        comment = Talk.objects.all()

    paginator = Paginator(comment, 20)  # 每页显示10条记录
    page = request.GET.get('page')  # 获取url的页码
    comments = paginator.get_page(page)

    if request.user.is_authenticated: #用于添加指定头部
        user = User.objects.get(username=request.user.username)
        userinfo_all = UserInfo.objects.get(user=user)
        if request.method == 'POST':
            comment_form = TalkForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.user = request.user

                # 二级回复
                if parent_comment_id:
                    parent_comment = Talk.objects.get(id=parent_comment_id)
                    # 若回复层级超过二级，则转换为二级
                    new_comment.parent_id = parent_comment.get_root().id
                    # 被回复人
                    new_comment.reply_to = parent_comment.user
                    new_comment.save()


                    # 新增代码，给其他用户发送通知
                    if UserInfo.userClass!='3': #防止管理员重复收到
                        notify.send(
                            request.user,
                            recipient=parent_comment.user,
                            verb='回复了你',
                            target=Talk,
                            action_object=new_comment,
                        )
                    return HttpResponse('200 OK')


                new_comment.save()

                # 新增代码，给管理员发送通知
                if UserInfo.userClass !='3':
                    notify.send(
                        request.user,
                        recipient=UserInfo.objects.filter(userClass='3'),
                        verb='回复了你',
                        target=Talk,
                        action_object=new_comment,
                    )

                return render(request, './talk/userTalk.html',{'nowtime':nowtime,
                              'comment_form': comment_form, 'user': user, "total": comment,
                               'userinfo_all': userinfo_all, 'comments': comments, 'search': search,
                               'parent_comment_id': parent_comment_id})
        elif request.method == 'GET':
            comment_form = TalkForm()
            context = {'comment_form': comment_form,
                    'parent_comment_id': parent_comment_id
                }
            return render(request, 'Talk/reply.html', context)

    else:
        comment_form = TalkForm()
        return render(request, './talk/userTalk.html', {"total": comment,'nowtime':nowtime,
                                                        'comment_form':comment_form,
                                                        'comments': comments,
                                                        'search': search,
                                                        'parent_comment_id': parent_comment_id})

# 点赞数 +1
class IncreaseLikesView(View):
    def post(self, request, *args, **kwargs):
        talk = Talk.objects.get(id=kwargs.get('id'))
        talk.likes += 1
        talk.save()
        return HttpResponse('success')

@login_required(login_url='/account/login/')
def talk_delete(request,talk_id):
    """删除评论"""
    talk_user= Talk.objects.get(id=talk_id)# 根据 id 获取需要删除评论
    talk_user.delete()      # 调用.delete()方法删除评论
    return redirect("talk:user_talk")