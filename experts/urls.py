from django.urls import path
from experts import views

urlpatterns = [
    path('user-professor/',views.experts_pro, name="user_professor"),#ר�ҽ���
    path('user-volunteer/',views.experts_vol, name="user_volunteer"),#־Ը�߽���

]
