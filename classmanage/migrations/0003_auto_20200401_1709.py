# Generated by Django 3.0.4 on 2020-04-01 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classmanage', '0002_auto_20200401_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='chuti_id',
            field=models.CharField(default='admin', max_length=20),
        ),
    ]
