from django.contrib import admin

from account.admin import UserInfoAdmin
from .models import User,UserInfo,Paper,Question,Grade
# 修改名称
admin.site.site_header='野生动物物种识别系统管理员后台'
admin.site.site_title='野生动物物种识别系统管理员后台'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """单项选择题"""
    list_display = ('id','subject','title','optionA','optionB','optionC','optionD','answer','score')


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    """试卷"""
    list_display = ('chuti_id','for_user','subject','examtime')
    list_display_links = ('for_user','subject','examtime')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    """分数"""
    list_display = ('user_id','subject','grade',)
    list_display_links = ('user_id','subject','grade',)
