from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
# Create your models here.


class Artical(models.Model):

    title = models.CharField(max_length=225,verbose_name='标题')
    content = models.TextField(verbose_name='文章正文')

    def summary(self):
        return mark_safe(self.content[:100])
    summary.short_description = '摘要'

    @property
    def content_display(self):
        return mark_safe(self.content)


class AticalImage(models.Model):
    name = models.CharField((u'name'), max_length=100)
    photo = models.ImageField(upload_to=settings.MEIDA_ROOT, null=True, blank=True, verbose_name=(u'photo'))