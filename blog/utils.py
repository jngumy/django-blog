import random
from django.core.paginator import Paginator
from .models import Post,Categoria,RedesSociales,Web

def consulta(id):
    try:
        return Post.objects.get(id = id)
    except:
        return None

def get_redes():
    return RedesSociales.objects.filter(estado = True).latest('fecha_creacion')

def get_web():
    return Web.objects.filter(estado = True).latest('fecha_creacion')

def generarCategoria(request,nombre_categoria):
    posts = Post.objects.filter(
                        estado = True,
                        publicado = True,
                        categoria = Categoria.objects.get(nombre = nombre_categoria)
                        )
    try:
        categoria = Categoria.objects.get(nombre = nombre_categoria)
    except:
        categoria = None

    paginator = Paginator(posts,4)
    pagina = request.GET.get('page')
    posts = paginator.get_page(pagina)
    contexto = {
        'posts':posts,
        'sociales':get_redes(),
        'web':get_web(),
        'categoria':categoria,
        'popular_posts': get_posts(categoria.nombre, 4),
    }
    return contexto

def get_posts(nombre_categoria, cantidad):
    posts = Post.objects.filter(
                        estado = True,
                        publicado = True,
                        categoria = Categoria.objects.get(nombre = nombre_categoria)
                        ).order_by('-fecha_publicacion')[:cantidad]
    return posts
    
def get_random_posts(cantidad):

    posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id', flat = True))
    
    random_post = list()

    for x in range(cantidad):
        post = random.choice(posts)
        posts.remove(post)
        random_post.append(consulta(post))
    
    return random_post