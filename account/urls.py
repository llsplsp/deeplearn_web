from django.conf.urls import url
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from . import views


urlpatterns=[
    path('home/',views.user_home,name='home'),
    path('login/', views.user_login,name='user_login'), #自己写的登录函数
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register,name='user_register'), #后面的name表示url的name，在后面html中要调用的名称
    path('', views.registerSuccess,name='register_success'),
    path('password-change/',PasswordChangeView.as_view(template_name="account/password_change_form.html", success_url="/account/password-change-done/"), name='password_change'),
    path('password-change-done/',PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"), name='password_change_done'),

    path('password-reset/',
         PasswordResetView.as_view(
             template_name="account/password_reset_form.html",
             email_template_name="account/password_reset_email.html",
             subject_template_name="account/password_reset_subject.txt",
             success_url="/account/password-reset-done/"),
         name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html", success_url='/account/password-reset-complete/'),
         name="password_reset_confirm"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),

    path('my-information/', views.myself, name='my_information'),
    path('edit-my-information/', views.myself_edit, name="edit_my_information"),
    # path(r'^media/(?P<path>.*)$',serve, {'document_root': settings.MEDIA_ROOT}),
    path('my-image/', views.my_image, name="my_image"),
    path('manage-user/', views.user_manage, name="manage_user"),
    path('delete-user/<int:user_id>/', views.user_delete, name="delete_user"),
    path('update-user/<int:id>', views.user_update, name="update_user"),
]

