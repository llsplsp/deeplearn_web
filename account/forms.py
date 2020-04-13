#专门存放表单有关的类，也可以用html实现

from django import forms
from django.contrib.auth.models import User
from account.models import UserInfo


class LoginForm(forms.Form):
    """用户登录表单类"""
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)#widget规定类型

#forms.ModelForm 如果要对数据库进行修改 就继承modelform，否则写form
class RegistrationForm(forms.ModelForm):
    """用户注册的另外一种写法，注册不需要重新定义模型类"""
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

    class Meta:#内部类
            model = User
            fields = ("username","email")

    def clean_password2(self):#确认用户输入的密码一致
        cd = self.cleaned_data #检验
        if cd['password']!=cd['password2']:
            raise forms.ValidationError("两次输入的密码不一致，请重新输入")
        return cd['password2']

class UserInfoForm(forms.ModelForm):
    """新增的用户信息"""
    class Meta:
        model = UserInfo
        fields = ("phone", "company", "profession", "address", "aboutme", "photo")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)