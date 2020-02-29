#coding:utf-8
from rest_framework import viewsets, mixins
from blog.serializers import ArticalSerializer
from rest_framework.response import Response
from blog.models import Artical


class ActicleList(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Artical.objects.all()
    serializer_class = ArticalSerializer
    ordering_fields = ['pushed',]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
