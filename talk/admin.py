from django.contrib import admin
from talk.models import Talk

class TalkAdmin(admin.ModelAdmin):
    """后台管理系统增加工作概况的信息"""
    list_display = ("user_id", "body", "created")  # 属性
    list_filter = ('user_id',)  # 过滤器展示的内容
    search_fields = ('body',)  # 搜索的关键字
    date_hierarchy = 'created'
    ordering = ['-created', ]  # 排序

admin.site.register(Talk,TalkAdmin)
