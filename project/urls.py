
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app.api import viewsets
from app.views import index
from django.conf import settings
from django.conf.urls.static import static

route = routers.DefaultRouter()

route.register(r'agendamentos',viewsets.AgendamentoViewSet,basename='Agendamentos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='url_index'),
    path('api/',include(route.urls))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
