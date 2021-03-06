#coding:utf-8

from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup
from django.core.files.storage import FileSystemStorage
from DjangoUeditor.models import UEditorField

fs = FileSystemStorage(settings.MEIDA_ROOT)
# Create your models here.
from django.utils.six.moves.urllib.parse import urljoin

class Artical(models.Model):

    PUBLISHED_STATUS = (
        ('published','发布'),
        ('draft','草稿')
    )
    title = models.CharField(max_length=225, verbose_name='标题')
    content = UEditorField(u'内容	',width='100%',height='100%',toolbars="full", imagePath=settings.MEIDA_ROOT+'/', upload_settings={"imageMaxSize":1204000},
             settings={},blank=True)
    pushed = models.DateTimeField(verbose_name="发布时间")
    published = models.CharField(max_length=32, verbose_name="发布状态", choices=PUBLISHED_STATUS)
    articaltag = models.ManyToManyField('ArticalTag')   
    created = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")  

    def summary(self):
        bs = BeautifulSoup(self.content[:1000], "html.parser")
        return bs.get_text()

    summary.short_description = '摘要'


    def tag(self):
        return ','.join([i.tag_content for i in self.articaltag.all()])

    tag.short_description = '标签'

    @property
    def content_display(self):
        return mark_safe(self.content)

    class Meta:
        db_table = 'blog_artical'
        verbose_name='文章'              # 单数形式 admin 列表现实的名字
        verbose_name_plural='文章'   # 这个是复数形式 admin内新建或更改模型数据时现实的名字


    def __str__(self):
        return '文章:' + self.title


class ArticalImage(models.Model):
    flieimage = models.CharField(max_length=1000)
    image_path= models.ImageField(storage=fs)
    created = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")


class ArticalTag(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="标签id") 
    tag_content= models.CharField(max_length=64,verbose_name="标签内容") 
    created = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")


    def __str__(self):
        return self.tag_content

    class Meta:
        db_table = 'blog_articaltag'
        verbose_name='文章标签'
        verbose_name_plural='文章标签'