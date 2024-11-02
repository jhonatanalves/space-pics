from django.contrib import admin
from django.urls import path, include
from galeria.views import index, imagem, buscar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('galeria/', buscar, name='buscar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)