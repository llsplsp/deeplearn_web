from django.db import models
from django.contrib.auth.models import User



class UserInfo(models.Model):
    """用户个人信息"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    userClass = models.CharField(default='0',max_length=10) #用户类别，游客，志愿者，专家，管理员
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    aboutme = models.TextField(blank=True)
    photo = models.ImageField(verbose_name='头像',upload_to='avatar/%Y%m%d/',blank=True) #头像

    class Meta:
        """修改数据默认显示名称"""
        db_table = 'account_userinfo'
        verbose_name = '用户管理模块'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'user {}'.format(self.user.username)
