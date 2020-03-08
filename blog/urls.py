from django.urls import path,include
from blog import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'artical', api.ArticleList)

urlpatterns = router.urls
