# Generated by Django 3.0.4 on 2020-04-01 04:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=20, verbose_name='科目')),
                ('title', models.ImageField(upload_to='', verbose_name='题目')),
                ('optionA', models.CharField(max_length=30, verbose_name='A选项')),
                ('optionB', models.CharField(max_length=30, verbose_name='B选项')),
                ('optionC', models.CharField(max_length=30, verbose_name='C选项')),
                ('optionD', models.CharField(max_length=30, verbose_name='D选项')),
                ('answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=10, verbose_name='答案')),
                ('score', models.IntegerField(default=10, verbose_name='分数')),
            ],
            options={
                'verbose_name': '单项图像标签选择题库',
                'verbose_name_plural': '单项图像标签选择题库',
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(default='admin', max_length=20, verbose_name='出题人')),
                ('subject', models.CharField(default='', max_length=20, verbose_name='科目')),
                ('major', models.CharField(max_length=20, verbose_name='适用用户')),
                ('examtime', models.DateTimeField()),
                ('pid', models.ManyToManyField(to='classmanage.Question')),
            ],
            options={
                'verbose_name': '试卷',
                'verbose_name_plural': '试卷',
                'db_table': 'paper',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='', max_length=20, verbose_name='科目')),
                ('grade', models.IntegerField()),
                ('sid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '成绩',
                'verbose_name_plural': '成绩',
                'db_table': 'grade',
            },
        ),
    ]
