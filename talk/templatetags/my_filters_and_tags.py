#coding=utf-8
from django.utils import timezone
import math
from django import template

register=template.Library()

#获取相对时间
@register.filter(name='timesince_zh')
def time_since_zh(value):
    now = timezone.now()
    diff = now-value

    # if diff.days==0 and diff.seconds>=0 and diff.seconds<60:
    #     return '刚刚'
    # if diff.days==0 and diff.seconds>=60 and diff.seconds<3600:
    #     return str(math.floor(diff.seconds/60))+'分钟前'
    # if diff.days==0 and diff.seconds>=3600 and diff.seconds<86400:
    #     return str(math.floor(diff.seconds/3600))+'小时前'
    # if diff.days>=1 and diff.days<30:
    #     return str(diff.days)+'天前'
    # if diff.days>=30 and diff.days<365:
    #     return str(math.floor(diff.days/30))+'个月前'
    # if diff.days>=365:
    #     return str(math.floor(diff.days/365))+'年前'

    seconds = diff.seconds
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    months, days = divmod(days, 30)
    years, months = divmod(months, 12)
    # print("时间差：", diff)

    if years != 0:
        time = str(years) + '年前'
        return time
    elif months != 0:
        time = str(months) + '个月前'
        return time
    elif days != 0:
        time = str(days) + '天前'
        return time
    elif hours != 0:
        time = str(hours) + '小时前'
        return time
    elif minutes != 0:
        time = str(minutes) + '分钟前'
        return time
    elif seconds != 0:
        time = str(seconds) + '秒前'
        return time
    else:
        time = '刚刚'
        return time