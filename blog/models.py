from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe


# Create your models here.


class Artical(models.Model):
    title = models.CharField(max_length=225, verbose_name='标题')
    content = models.TextField(verbose_name='文章正文')

    def summary(self):
        return mark_safe(self.content[:100])

    summary.short_description = '摘要'

    @property
    def content_display(self):
        return mark_safe(self.content)

    def __str__(self):
        return 'Artical:' + self.title
