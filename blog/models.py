from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class ModeloBase(models.Model):

    '''
    Clase abstracta para evitar repetir campos en demás modelos
    '''
    id = models.AutoField(primary_key = True)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)
    fecha_modificacion= models.DateField('Fecha de Modificación', auto_now = True, auto_now_add = False)
    fecha_eliminacion = models.DateField('Fecha de ELiminacion', auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True


class Categoria(ModeloBase):
    nombre = models.CharField('Nombre de la categoria', max_length = 100, unique = True)
    imagen_referencial = models.ImageField('Imagen referencial', upload_to = 'categoria/')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre
    
class Autor(ModeloBase):
    nombre = models.CharField('Nombres', max_length = 100)
    apellidos = models.CharField('Apellidos',  blank = True, max_length = 120)
    email = models.EmailField('Correo electronico', max_length = 200)
    descripcion = models.TextField('Descripcion')
    web = models.URLField('Web', null = True, blank = True) #puede ser dejado en blanco o ser nullo
    facebook = models.URLField('Facebook', null = True, blank = True) #puede ser dejado en blanco o ser nullo
    twitter = models.URLField('Twitter', null = True, blank = True) #puede ser dejado en blanco o ser nullo
    instagram = models.URLField('Instagram', null = True, blank = True) #puede ser dejado en blanco o ser nullo
    imagen_referencial = models.ImageField('Imagen Referencial', null = True, blank = True,upload_to = 'autores/')

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0}, {1}'.format(self.apellidos, self.nombre)



class Post(ModeloBase):
    titulo = models.CharField('Titulo del Post', max_length = 150, unique=True)
    slug = models.CharField('Slug', max_length = 150, unique = True)
    descripcion = models.TextField('Descripcion')
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    contenido = RichTextField()
    imagen_referencial = models.ImageField('Imagen Referencial', upload_to = 'imagenes/', max_length = 255)
    publicado = models.BooleanField('Publicado / No Publicado', default = False)
    fecha_publicacion = models.DateField('Fecha de Publicación') #se ingresa de manera manual
   

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

class Web(ModeloBase):
    nosotros = models.TextField('Nosotros')
    telefono = models.CharField('Telefono', max_length= 10)
    email = models.EmailField('Correo Electronico', max_length = 200)
    direccion = models.CharField('Direccion FIsica', max_length = 200)

    class Meta:
        verbose_name_plural = 'Web'
        verbose_name_plural = 'Webs'

    def __str__(self):
        return self.nosotros
    
class RedesSociales(ModeloBase):
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.facebook

'''
    modelo para formulario de contactos
'''
class Contacto(ModeloBase):
    nombre = models.CharField('Nombre', max_length = 100)
    apellidos = models.CharField('Apellidos ', max_length = 150)
    correo = models.EmailField('Correo electronico', max_length = 200)
    asunto = models.CharField('Asunto', max_length = 100)
    mensaje = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.asunto

class Suscriptor(ModeloBase):
    correo = models.EmailField('Correo electronico', max_length = 200)

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.correo