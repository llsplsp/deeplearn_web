# Generated by Django 2.1 on 2020-04-05 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200405_2102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户管理模块', 'verbose_name_plural': '用户管理模块'},
        ),
    ]