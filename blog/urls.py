from django.urls import path
from blog import api

urlpatterns = [
    path('blog/', api.ActicleList.as_view({'get': 'list', }),name = 'artical-detail'),

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEIDA_ROOT)
