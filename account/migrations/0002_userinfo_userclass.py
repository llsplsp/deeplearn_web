# Generated by Django 3.0.4 on 2020-03-28 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='userClass',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
