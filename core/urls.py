from django.urls import path, include
from core import views
from .views import index,perfil1,perfil2,perfil3,formatos1,formatos2,cartas_crear,cartas,cartas2,reportes,reportes2,repositorio,repositorio2,login
from .views import usuarios,empresas,seguimiento,archivos,revisiones
from django.contrib.staticfiles.urls import static
from django.conf import settings


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('master/<int:user_id>/', perfil1, name='perfil1'),
    path('master/<int:user_id>/usuarios', usuarios, name='usuarios'),
    path('master/<int:user_id>/empresas', empresas, name='empresas'),
    path('master/<int:user_id>/seguimiento', seguimiento, name='seguimiento'),
    path('master/<int:user_id>/archivos', archivos, name='archivos'),
    path('oficina/<int:user_id>/', perfil2, name='perfil2'),
    path('alumno/<int:user_id>/', perfil3, name='perfil3'),
    path('oficina/<int:user_id>/formatos', formatos1, name='formatos1'),
    path('alumno/<int:user_id>/formatos', formatos2, name='formatos2'),
    path('oficina/<int:user_id>/carta-detalle/<int:solicitud_id>', cartas_crear, name='cartas_crear'),
    path('oficina/<int:user_id>/cartas', cartas, name='cartas1'),
    path('alumno/<int:user_id>/cartas', cartas2, name='cartas2'),
    path('oficina/<int:user_id>/reportes', reportes, name='reportes1'),
    path('alumno/<int:user_id>/reportes', reportes2, name='reportes2'),
    path('oficina/<int:user_id>/repositorio', repositorio, name='repositorio1'),
    path('oficina/<int:user_id>/repositorio/<int:archivo_id>', revisiones, name='revisar'),
    path('alumno/<int:user_id>/repositorio', repositorio2, name='repositorio2'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
