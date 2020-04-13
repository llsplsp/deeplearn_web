from django.contrib import admin
from teamwork.models import TeamWorkWrite

class TeamWorkWriteAdmin(admin.ModelAdmin):
    """后台管理系统增加工作概况的信息"""
    list_display = ("title", "author", "publish")  # 属性
    list_filter = ('publish', 'author')  # 过滤器展示的内容
    search_fields = ('title', 'body')  # 搜索的关键字
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['-publish', 'author']  # 排序

admin.site.register(TeamWorkWrite,TeamWorkWriteAdmin)