from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Artical
from blog.models import ArticalTag

# Serializers define the API representation.

class ArticalTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticalTag
        fields = ('id', 'tag_content')

class ArticalSerializer(serializers.ModelSerializer):
    pushed = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    articaltag = ArticalTagSerializer(many = True)
    class Meta:
        model = Artical
        fields = ('id', 'title', 'content', 'articaltag', 'pushed')


class ArticalListSerializer(serializers.ModelSerializer):
    pushed = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    articaltag = ArticalTagSerializer(many = True)
    class Meta:
        model = Artical
        fields = ('id', 'title', 'summary', 'articaltag', 'pushed')