from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

class TeamWorkWrite(models.Model):
    """工作概况"""
    title = models.CharField(max_length=300)
    # 一个用户对应多篇文章
    author = models.ForeignKey(User, related_name="work_posts", on_delete=models.CASCADE)  # ForeignKey 一对多的关系
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) #带时区的
    total_views = models.PositiveIntegerField(default=0)#总浏览次数

    def instance_recently(self):
        """优化时间显示"""
        diff =  timezone.now()- self.publish #发布文字的时间差值
        seconds = diff.seconds
        minutes,seconds = divmod(seconds,60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        months, days = divmod(days, 30)
        years, months = divmod(months, 12)
        print("时间差：",diff)

        if years!=0:
            time = str(years) + '年前'
            return time
        elif months!=0:
            time = str(months) + '个月前'
            return time
        elif days!=0:
            time = str(days) + '天前'
            return time
        elif hours!=0:
            time = str(hours) + '小时前'
            return time
        elif minutes!=0:
            time = str(minutes) + '分钟前'
            return time
        elif seconds!=0:
            time = str(seconds) + '秒前'
            return time
        else:
            time = '刚刚'
            return time



    # 按照指定的字段进行数据库的排序  用于给 model 定义元数据
    class Meta:
        """元类，可选类，写了可以让我们更好理解"""
        db_table = 'teamwork_teamworkwrite' #数据库表名
        verbose_name = '工作概况'  #后台管理系统的名称
        verbose_name_plural = verbose_name
        ordering = ("-publish",)  # 倒序显示

    # 定义了需要表示数据时应该显示的名称,体现在后台管理系统中。
    def __str__(self):
        return self.title
