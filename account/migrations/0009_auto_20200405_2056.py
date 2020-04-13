# Generated by Django 2.1 on 2020-04-05 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20200402_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='school',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='user_pic/%Y%m%d/', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
