from django.contrib.auth.models import User
from django.db import models

class speciesRecognition(models.Model):
    data_photo = models.ImageField(verbose_name='上传需要识别的物种图片', upload_to='dataSet/%Y%m%d/', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'deeplearn_speciesrecognition'
        verbose_name = '物种识别模块'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'created {}'.format(self.created)