from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'Reloj de plastilina - Blog - Admin'

admin.site.site_title = 'Reloj de plastilina - Blog - Admin'

admin.site.index_title = 'Panel de control'



class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_creacion', 'fecha_publicacion', 'publicado')
    list_filter = ('fecha_publicacion','categoria', 'publicado')


admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Post, PostAdmin)
admin.site.register(Web)
admin.site.register(RedesSociales)
admin.site.register(Contacto)
