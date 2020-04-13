from django.contrib import admin
from account.models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    """后台管理系统增加的信息"""
    list_display = ("user",'userClass',"phone","address","aboutme",)
    list_filter = ("user",)
    search_fields = ('user','address','profession',)
    ordering = ["user"]

admin.site.register(UserInfo,UserInfoAdmin)
# Register your models here.
