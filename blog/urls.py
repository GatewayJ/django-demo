from django.urls import path
from django.conf.urls import static
from django.conf import settings
from blog import views

urlpatterns = [
    path('blog/', views.ActicleList.as_view({'get': 'list',})),

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEIDA_ROOT)