# Generated by Django 2.1 on 2020-04-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamwork', '0002_auto_20200401_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamworkwrite',
            name='total_views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
