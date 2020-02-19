import os
import json
import uuid
from django.shortcuts import HttpResponse
from rest_framework import viewsets, mixins
from django.contrib.auth.models import User
from blog.serializers import ArticalSerializer
from rest_framework.response import Response
from django.conf import settings
from blog.models import Artical
from blog.models import ActicalImage

# Create your views here.


class ActicleList(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Artical.objects.all()
    serializer_class = ArticalSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


from django.core.files.base import ContentFile
def upload_file(request):
    file_content = ContentFile(request.FILES['imgFile'].read())
    # ImageField的save方法，第一个参数是保存的文件名，第二个参数是ContentFile对象，里面的内容是要上传的图片、视频的二进制内容
    image = ActicalImage()
    image.image_path.save(request.FILES['imgFile'].name, file_content)
    image.flieimage='as'
    # image.image_path=request.FILES.get("imgFile", None)
    # image.image_path.save()
    print(image.image_path.url)
    image.save()
    return HttpResponse(json.dumps({"error": 0, "url": image.image_path.url}), content_type="application/json")
def is_ext_allowed(type, ext):
    '''
    根据类型判断是否支持对应的扩展名
    '''
    ext_allowed = {}
    ext_allowed['image'] = ['jpg', 'jpeg', 'bmp', 'gif', 'png']
    ext_allowed['flash'] = ["swf", "flv"]
    ext_allowed['media'] = ["swf", "flv", "mp3", "wav", "wma", "wmv", "mid", "avi", "mpg", "asf", "rm", "rmvb", "mp4"]
    ext_allowed['file'] = ["doc", "docx", "xls", "xlsx", "ppt", "htm", "html", "txt", "zip", "rar", "gz", "bz2", 'pdf']
    return ext in ext_allowed[type]


def process_upload(files, type):
    dir_types = ['image', 'flash', 'media', 'file']
    # 判断是否支持对应的类型
    if type not in dir_types:
        return {"error": 1, "message": u"上传类型不支持[必须是image,flash,media,file]"}

    cur_ext = files.name.split('.')[-1]  # 当前上传文件的扩展名
    # 判断是否支持对应的扩展名
    if not is_ext_allowed(type, cur_ext):
        return {'error': 1, 'message': u'error:扩展名不支持 %s类型不支持扩展名%s' % (type, cur_ext)}

    image_name = str(uuid.uuid4()) + "_" + files.name

    img_path = os.path.join(settings.MEIDA_ROOT, 'blog', image_name)
    img_url = os.path.join(settings.MEDIA_URL, 'blog', image_name)
    with open(img_path, "wb") as file_path:
        for i in files.chunks():
            file_path.write(i)
    return {"error": 0, "url": img_url}
