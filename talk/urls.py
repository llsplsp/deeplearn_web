from django.urls import path

from talk import views

urlpatterns = [
    path('talk-user/',views.userTalk, name="user_talk"),
    # 新增代码，处理二级回复
    path('talk-user/<int:parent_comment_id>', views.userReply, name='talk_reply'),

    #点赞
    path(
        'increase-likes/<int:id>/',
        views.IncreaseLikesView.as_view(),
        name='increase_likes'
    ),

    path('talk-delete/<int:talk_id>/',views.talk_delete, name="talk_delete"),

]
