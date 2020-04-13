# coding=utf-8
from time import sleep

from django.test import TestCase
import datetime

from django.urls import reverse
from django.utils import timezone
from teamwork.models import TeamWorkWrite
from django.contrib.auth.models import User

class TeamworkModelTests(TestCase):
    """测试模型的用例"""
    def test_was_instance_now_less_second(self):
        author = User(username='user1', password='test_password')
        author.save()
        seconds_before_article = TeamWorkWrite(
            author=author,
            title='test1',
            body='test1',
            publish=timezone.now() - datetime.timedelta(hours=4,minutes=30,seconds=36) #表示两个时间的间隔
        )
        print(seconds_before_article.publish)
        print(seconds_before_article.instance_recently())#测试应该显示‘50秒前’


# class TeamWorkViewTests(TestCase):
#     """测试视图的用例"""
#     def test_increase_views(self):
#         # 请求详情视图时，阅读量 +1
#         author = User(username='user4', password='test_password')
#         author.save()
#         article = TeamWorkWrite(
#             author=author,
#             title='test4',
#             body='test4',
#             )
#         article.save()
#         self.assertIs(article.total_views, 0)
#
#         url = reverse('talk:user_talk')
#         response = self.client.get(url)  #这个起作用
#
#         viewed_article = TeamWorkWrite.objects.get(id=article.id)
#         self.assertIs(viewed_article.total_views, 1)
#
#     # def test_increase_views_but_not_change_updated_field(self):
#     #     # 请求详情视图时，不改变 updated 字段
#     #     author = User(username='user5', password='test_password')
#     #     author.save()
#     #     article = TeamWorkWrite(
#     #         author=author,
#     #         title='test5',
#     #         body='test5',
#     #         )
#     #     article.save()
#     #
#     #     sleep(0.5)
#     #
#     #     url = reverse('talk:user_talk')
#     #     response = self.client.get(url)
#     #
#     #     viewed_article = TeamWorkWrite.objects.get(id=article.id)
#     #     self.assertIs(viewed_article.updated - viewed_article.created < timezone.timedelta(seconds=0.1), True)