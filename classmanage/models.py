from django.contrib.auth.models import User
from django.db import models
from account.models import UserInfo

class Question(models.Model):
    """选择题题目"""
    ANSWER=(
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
    )
    id = models.AutoField(primary_key=True)
    subject = models.CharField('科目', max_length=20)
    title = models.ImageField('题目',upload_to='classsubject/')
    optionA=models.CharField('A选项',max_length=30)
    optionB=models.CharField('B选项',max_length=30)
    optionC=models.CharField('C选项',max_length=30)
    optionD=models.CharField('D选项',max_length=30)
    answer=models.CharField('答案',max_length=10,choices=ANSWER)
    score=models.IntegerField('分数',default=10)
    class Meta:
        db_table='question'
        verbose_name='单项图像标签题库'
        verbose_name_plural=verbose_name
    def __str__(self):
        return '<%s:%s>'%(self.subject,self.title);


class Paper(models.Model):
    """管理员增加和修改答题题目 组卷"""
    #题号和题库为多对多的关系，一个题库可以有多个题目，一个题目也可以属于多个题库。
    timu_id=models.ManyToManyField(Question)#多对多
    chuti_id=models.ForeignKey(User,on_delete=models.CASCADE)  #出题人编号
    subject=models.CharField('科目',max_length=20,default='')
    for_user=models.CharField('适用用户类别',max_length=20,default='0') #适用用户类别
    examtime=models.DateTimeField()

    class Meta:
        db_table='paper'
        verbose_name='答题升级模块'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.for_user

class Grade(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default='')#添加外键
    subject=models.CharField('科目',max_length=20,default='')
    grade=models.IntegerField()

    def __str__(self):
        return '<%s:%s>'%(self.user_id,self.grade)

    class Meta:
        db_table='grade'
        verbose_name='成绩'
        verbose_name_plural=verbose_name


