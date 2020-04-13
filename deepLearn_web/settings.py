import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bo7zaacgvqgjzn)9t8(1q_d-0iq66e)31#*0k09uk34ivm#u6g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #调试时可以打开，正式使用时必须关闭

ALLOWED_HOSTS = [] #域名，配置了只能通过域名访问

AUTHENTICATION_BACKENDS = (
    'social_core.backends.weibo.WeiboOAuth2',
    'social_core.backends.qq.QQOAuth2',
    'social_core.backends.weixin.WeixinOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Application definition
#添加新建的应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', # allauth 启动必须项
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',


    'social_django',

    'django.contrib.staticfiles',
    'ckeditor',#富文本编辑器
    'mptt', #多级评论
    'notifications',#消息通知
    'account', #用户管理模块
    'deeplearn', #物种识别
    'teamwork',#工作概况
    'classmanage',#等级管理
    'talk',     #留言互动
    'userbehavior', #记录用户行为
    'notice',#消息标记为已读和未读
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'deepLearn_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',# allauth 启动必须项
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                #第三方登录
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'deepLearn_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES ={
    'default':{
    'ENGINE' :'django.db.backends.mysql',
    'NAME':'animal_deeplearn',
    'HOST':'127.0.0.1',
    'USER':'root',
    'PASSWORD':'123456',
    'PORT':'3306',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
#指定静态文件存放的位置，根目录下的static里面，以前是应用里面的static里面
STATICFILES_DIRS = (
    # os.path.join(BASE_DIR,"static"),
    os.path.join(BASE_DIR, 'static').replace('\\', '/'),
)
# 静态文件收集目录
# STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

#用于保存用户上传的图片，包括头像和他们的图片数据集
MEDIA_URL = "/media/"   # 上传文件保存
MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'media/')#访问的位置
)


LOGIN_REDIRECT_URL='/deeplearn'

#邮件重置密码操作配置
EMAIL_HOST = 'smtp.qq.com'
EMAIL_HOST_USER = '946076113@qq.com'
EMAIL_HOST_PASSWORD = 'jziwanhbwfjwbfba' #安全码
EMAIL_PORT=587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Redis数据库配置 用于记录阅读次数
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

#指定富文本编辑器的功能，去除那些用不到的功能。
CKEDITOR_CONFIGS = {
    # django-ckeditor默认使用default配置
    'default': {
        # 编辑器宽度自适应
        'width':'auto',
        'height':'250px',
        # tab键转换空格数
        'tabSpaces': 4,
        # 工具栏风格
        'toolbar': 'Custom',
        # 工具栏按钮
        'toolbar_Custom': [
            # 表情 代码块
            ['Smiley', 'CodeSnippet'],
            # 字体风格
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
            # 字体颜色
            ['TextColor', 'BGColor'],
            # 链接
            ['Link', 'Unlink'],
            # 列表
            ['NumberedList', 'BulletedList'],
            # 最大化
            ['Maximize']
        ],
        # 加入代码块插件
        'extraPlugins': ','.join(['codesnippet','prism', 'widget', 'lineutils']),
    }
}

SITE_ID = 1
# 第三方登录，里面的值是你的开放平台对应的值
SOCIAL_AUTH_WEIBO_KEY = '1523260770'
SOCIAL_AUTH_WEIBO_SECRET = '789238b7137d06d2c8b7299bc67a1d00'

#登录成功后跳转到首页
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'account/home/'

# SOCIAL_AUTH_QQ_KEY = 'xxxxxxx'
# SOCIAL_AUTH_QQ_SECRET = 'xxxxxxx'
#
# SOCIAL_AUTH_WEIXIN_KEY = 'xxxxxxx'
# SOCIAL_AUTH_WEIXIN_SECRET = 'xxxxxxx'

#日志记录
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False, #是否禁止默认配置的记录器
    #处理器
    'handlers': {
        'file': {
            'level': 'ERROR',
            # 'class': 'logging.FileHandler',
            #新增内容
            'class': 'logging.handlers.TimedRotatingFileHandler', #Python内置的随时间分割日志文件的模块
            'when': 'midnight',
            'backupCount': 30, #日志文件保存日期为30天
            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
        },
    },
    #记录器
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}