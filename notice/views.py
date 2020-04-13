# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import UserInfo


class CommentNoticeListView(LoginRequiredMixin, ListView):
    # 上下文的名称context
    context_object_name = 'notices'
    # 模板位置
    template_name = 'notice/list.html'
    # 登录重定向
    login_url = '/account/login/'

    # 未读通知的查询集
    def get_queryset(self):
        return self.request.user.notifications.unread()

    def get_context_data(self, **kwargs):
        context = super(CommentNoticeListView, self).get_context_data(**kwargs)
        user = User.objects.get(username=self.request.user.username)
        userinfo_all = UserInfo.objects.get(user=user)
        context['userinfo_all'] = userinfo_all
        return context


class CommentNoticeUpdateView(View):
    # 处理 get 请求
    def get(self, request):
        # 获取未读消息
        notice_id = request.GET.get('notice_id')
        # 更新单条通知
        if notice_id:
            request.user.notifications.get(id=notice_id).mark_as_read()
            return redirect('talk:user_talk')
        # 更新全部通知
        else:
            request.user.notifications.mark_all_as_read()
            return redirect('notice:list')