# coding:utf-8
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from blog.serializers import ArticalSerializer
from blog.serializers import ArticalListSerializer
from blog.models import Artical


class ArticleList(viewsets.ReadOnlyModelViewSet):
    queryset = Artical.objects.all()
    serializer_class = ArticalSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('published',)
    ordering = ('-published',)
    lookup_field = 'title'


    def list(self, request, *args, **kwargs):
        self.serializer_class = ArticalListSerializer
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)