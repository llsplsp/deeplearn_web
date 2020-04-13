from django.urls import path
from teamwork import views

urlpatterns = [
    path('team-work/',views.teamWork, name="team_work"),#工作概况
    # path('team-work/',views.TeamworkListView.as_view(), name="team_work"),#工作概况
    path('team-work/<int:workcontent_id>/', views.teamWork_content,name='work_detail'),#详情页
    path('teamwork-create/', views.teamwork_write, name='teamwork_create'),#写工作概况
    path('teamwork-delete/<int:workcontent_id>/', views.teamwork_delete, name='teamwork_delete'),
    path('teamwork-update/<int:workcontent_id>/', views.teamwork_update, name='teamwork_update'),
]
