from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from account.models import UserInfo


class Talk(MPTTModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='talks')
    # body=models.TextField()
    body=RichTextField() #富文本编辑器类型
    created=models.DateTimeField(auto_now_add=True)

    #新增点赞数统计
    likes = models.PositiveIntegerField(default=0)

    # 新增，mptt树形结构
    parent = TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')

    # 新增，记录二级评论回复给谁, str
    reply_to = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name='replyers')

    class Meta:
        db_table = 'talk_talk'  # 数据库表名
        verbose_name = '留言互动模块'  # 后台管理系统的名称
        verbose_name_plural = verbose_name


    class MPTTMeta:
        order_insertion_by = ['-created']

    def __str__(self):
        return self.body[:20]


