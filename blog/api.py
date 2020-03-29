# coding:utf-8
from rest_framework import viewsets, mixins
from blog.serializers import ArticalSerializer
from blog.models import Artical


class ArticleList(viewsets.ReadOnlyModelViewSet):
    queryset = Artical.objects.all()
    serializer_class = ArticalSerializer
    ordering_fields = ['pushed', ]
    lookup_field = 'title'
