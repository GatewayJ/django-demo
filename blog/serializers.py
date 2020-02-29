from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Artical

# Serializers define the API representation.


class ArticalSerializer(serializers.ModelSerializer):
    pushed = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Artical
        fields = ('id','title','summary','content','pushed')



class ImageField(serializers.ImageField):
    """
    从 easy_thumbnails.fields.ThumbnailerImageField 字段类型中解析出缩略图信息
    """
    pass
