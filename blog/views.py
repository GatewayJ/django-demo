import os
import json
import uuid
from django.shortcuts import HttpResponse
from rest_framework import viewsets,mixins
from django.contrib.auth.models import User
from blog.serializers import UserSerializer
from rest_framework.response import Response
from django.conf import settings
# Create your views here.


class ActicleList(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        print(111)
        return Response({"1":1})


def upload_file(request,blog_id):
    '''
    kindeditor图片上传返回数据格式说明：
    {"error": 1, "message": "出错信息"}
    {"error": 0, "url": "图片地址"}
    '''
    result = {"error": 1, "message": u"上传失败"}
    files = request.FILES.get("imgFile", None)  #input type="file" 中name属性对应的值为imgFile
    type = request.GET['dir']  #获取资源类型
    print(files,type)
    if files:
        result = process_upload(files,type,blog_id)
    #结果以json形式返回
    return HttpResponse(json.dumps(result),content_type="application/json")


def is_ext_allowed(type,ext):
    '''
    根据类型判断是否支持对应的扩展名
    '''
    ext_allowed = {}
    ext_allowed['image'] = ['jpg','jpeg', 'bmp', 'gif', 'png']
    ext_allowed['flash'] = ["swf", "flv"]
    ext_allowed['media'] = ["swf", "flv", "mp3", "wav", "wma", "wmv", "mid", "avi", "mpg", "asf", "rm", "rmvb", "mp4"]
    ext_allowed['file'] = ["doc", "docx", "xls", "xlsx", "ppt", "htm", "html", "txt", "zip", "rar", "gz", "bz2", 'pdf']
    return ext in ext_allowed[type]


def process_upload(files,type,blog_id):
    dir_types = ['image','flash','media','file']
    #判断是否支持对应的类型
    if type not in dir_types:
        return {"error":1, "message": u"上传类型不支持[必须是image,flash,media,file]"}

    cur_ext = files.name.split('.')[-1]  #当前上传文件的扩展名
    #判断是否支持对应的扩展名
    if not is_ext_allowed(type,cur_ext):
        return {'error':1, 'message': u'error:扩展名不支持 %s类型不支持扩展名%s' %(type,cur_ext)}

    image_name = str(blog_id) +"_" + str(uuid.uuid4()) + "_" + files.name

    img_path = os.path.join(settings.MEIDA_ROOT, image_name)
    img_url = os.path.join(settings.MEDIA_URL, image_name)
    with open(img_path,"wb") as file_path:
        for i in files.chunks():
            file_path.write(i)
    return {"error": 0, "url": img_url}
