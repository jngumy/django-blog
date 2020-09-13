from django.conf.urls import url
from django.urls import path

from .views import Inicio, DetallePost, AcercaDe, FormularioContacto, Listado, Search_Posts
from django.conf.urls import handler404
from .views import mi_error_404

app_name = 'blog'

handler404 = mi_error_404

urlpatterns = [
    path('', Inicio.as_view(), name = 'index'),
    path('musica/',Listado.as_view(),{'nombre_categoria':'Música'}, name = 'musica'),
    path('cine/',Listado.as_view(),{'nombre_categoria':'Cine'}, name = 'cine'),
    path('fotografia/',Listado.as_view(),{'nombre_categoria':'Fotografía'}, name = 'fotografia'),
    path('literatura/',Listado.as_view(),{'nombre_categoria':'Literatura'}, name = 'literatura'),
    path('literatura/ensayos',Listado.as_view(),{'nombre_categoria':'Ensayos'}, name = 'ensayos'),
    path('literatura/novelas',Listado.as_view(),{'nombre_categoria':'Novelas'}, name = 'novelas'),
    path('literatura/poesia',Listado.as_view(),{'nombre_categoria':'Poesía'}, name = 'poesia'),
    path('literatura/cronicas',Listado.as_view(),{'nombre_categoria':'Crónicas'}, name = 'cronicas'),
    path('literatura/cuentos',Listado.as_view(),{'nombre_categoria':'Cuentos'}, name = 'cuentos'),
    path('acerca/', AcercaDe.as_view(), name='acerca'),
    path('contacto/', FormularioContacto.as_view(), name = 'contacto'),
    path('search/', Search_Posts.as_view(), name = 'search'),
    path('post/<slug:slug>/', DetallePost.as_view(), name='detalle_post')
]