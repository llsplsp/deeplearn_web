import notifications.urls
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(('account.urls','account'),namespace='account')),#用户管理模块
    path('deeplearn/', include(('deeplearn.urls', 'deeplearn'), namespace='deeplearn')),
    path('teamwork/', include(('teamwork.urls','teamwork'),namespace='teamwork')),#工作概况
    path('classmanage/', include(('classmanage.urls','classmanage'),namespace='classmanage')),#等级管理
    path('talk/', include(('talk.urls','talk'),namespace='talk')),#留言互动
    path('userbehavior/',include(('userbehavior.urls','userbehavior'),namespace='userbehavior')),#数据统计模块
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('notice/', include(('notice.urls', 'notice'),namespace='notice')),
    path('experts/', include(('experts.urls', 'experts'),namespace='experts')),#专家库


    path('', include('social_django.urls', namespace='social')),#第三方登录
]
#上传的图片配置好了URL路径
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)