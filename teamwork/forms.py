from django import forms
from .models import TeamWorkWrite

class writeTeamworkForm(forms.ModelForm):
    """管理员写工作概述"""
    class Meta:
        model = TeamWorkWrite
        fields = ('title','body')