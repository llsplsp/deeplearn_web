from django.urls import path
from userbehavior import views

urlpatterns = [
    path('user-behavior/',views.userBehavior, name="user_behavior"),#用户行为

]
