from rest_framework import serializers
from django.contrib.auth.models import User

# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ImageField(serializers.ImageField):
    """
    从 easy_thumbnails.fields.ThumbnailerImageField 字段类型中解析出缩略图信息
    """
    pass