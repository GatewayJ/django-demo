from django.shortcuts import render,HttpResponse
from rest_framework import serializers,viewsets,mixins
from django.contrib.auth.models import User
from blog.serializers import UserSerializer,ImageField
from rest_framework.response import Response
# Create your views here.


class ActicleList(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        print(111)
        return Response({"1":1})

#
# class UploadFile(viewsets.GenericViewSet,mixins.ListModelMixin):
#     # queryset = User.objects.all()
#     # serializer_class = UserSerializer
#
#     def list(self, request, *args, **kwargs):
#         print(request.data)
#         return Response({"status":1})


def upload_file(request):
    return