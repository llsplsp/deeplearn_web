# Generated by Django 2.1 on 2020-04-08 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='speciesRecognition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_photo', models.ImageField(blank=True, upload_to='dataSet/%Y%m%d/', verbose_name='上传需要识别的物种图片')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '物种识别模块',
                'verbose_name_plural': '物种识别模块',
                'db_table': 'deeplearn_speciesrecognition',
            },
        ),
    ]