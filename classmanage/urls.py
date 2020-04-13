from django.urls import path

from classmanage import views

urlpatterns = [
    path('class-manage/',views.classManage, name="class_manage"),#答题入口
    path('class-manage/subject/', views.classManageSubject,name='class_subject'),#答题信息确认
    path('class-manage/exam/', views.startExam,name='class_exam'),#答题题目
    path('class-manage/grade/',views.calGrade,name='class_grade'), #成绩

]
