from django.urls import path
from experts import views

urlpatterns = [
    path('user-professor/',views.experts_pro, name="user_professor"),#专家介绍
    path('user-volunteer/',views.experts_vol, name="user_volunteer"),#志愿者介绍

]
