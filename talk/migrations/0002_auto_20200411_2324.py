# Generated by Django 2.1 on 2020-04-11 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talk', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'verbose_name': '留言互动模块', 'verbose_name_plural': '留言互动模块'},
        ),
        migrations.AlterModelTable(
            name='talk',
            table='talk_talk',
        ),
    ]
