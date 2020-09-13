import random

from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView,DetailView, View
from .models import Post, Categoria, RedesSociales, Web, Autor
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.defaults import page_not_found


from .utils import *
# Create your views here.



class Inicio(ListView):

    def get(self, request, *args, **kwargs):
        
        
        #obtengo solo los id de los posts publicados y estado = true
        posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id', flat = True))
      
        #elijo un post aleatorio
        principal = random.choice(posts)
        posts.remove(principal)
        principal = consulta(principal)

        post1 = random.choice(posts)
        posts.remove(post1)
        secundario = consulta(post1)


        post2 = random.choice(posts)
        posts.remove(post2)
        terciario = consulta(post2)

        #obtengo los ultimos 4 posts mas recientes 
        last_four_posts = Post.objects.filter(
            estado = True,
            publicado = True
        ).order_by('-fecha_publicacion')[:4]
   
        posts_cine = get_posts(nombre_categoria='Cine', cantidad=3)
        posts_musica =  get_posts(nombre_categoria='Música', cantidad=3)
        posts_fotografia =  get_posts(nombre_categoria='Fotografía', cantidad=3)
       

        # 5 posts aleatorios
        random_post = get_random_posts(5)
        autor = Autor.objects.get(id=1)

        contexto = {
            'principal' : principal,
            'secundario': secundario,
            'terciario': terciario,
            'posts_recientes': last_four_posts,
            'posts_cine': posts_cine,
            'posts_musica': posts_musica,
            'posts_fotografia': posts_fotografia,
            'random_posts': random_post,
            'sociales': get_redes(),
            'web': get_web(),
            'autor':autor,
        }
        
        return render(request, 'index.html', contexto)


class DetallePost(DetailView):
    def get(self, request, slug, *args, **kwargs):
        try:
            post = Post.objects.get(slug = slug)
            autor = Autor.objects.get(id=post.autor.id)
            posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id', flat = True))
            
      
                
        except:
            post = None
            autor = None
            
        try:
            post_anterior = Post.objects.get(id=post.id - 1)
            post_posterior = Post.objects.get(id=post.id + 1)

        except:
            post_anterior = None
            post_posterior = None
           
        
        contexto = {
            'post' : post,
            'post_anterior': post_anterior,
            'post_posterior': post_posterior,
            'random_posts':  get_random_posts(5),
            'related_posts': get_posts(nombre_categoria=post.categoria.nombre, cantidad=3),
            'sociales' : get_redes(),
            'web' : get_web(),
            'autor': autor,
        }

        return render(request, 'blog-post.html', contexto)


class AcercaDe(DetailView):
    def get(self, request, *args, **kwargs):
        contexto = {
            'web' : get_web(),
            'sociales' : get_redes(),
        }
        return render(request, 'about.html', contexto)

class FormularioContacto(View):
    def get(self,request,*args,**kwargs):
       
        contexto = {
            'sociales':get_redes(),
            'web':get_web(),
        }
        return render(request,'contact.html',contexto)


class Listado(ListView):

    def get(self,request,nombre_categoria,*args,**kwargs):
        contexto = generarCategoria(request,nombre_categoria)
        return render(request,'category.html',contexto)


class Search_Posts(ListView):
     def get(self,request,*args,**kwargs):
        query = request.GET.get("q")
        queryset_list = Post.objects.all()
        if query:
            queryset_list = queryset_list.filter(Q(titulo__icontains=query) | Q(descripcion__icontains=query) )
        paginator = Paginator(queryset_list, 4)
        pagina = request.GET.get('page')
        posts = paginator.get_page(pagina)
        contexto = {
        'posts':posts,
        'query':query,
        'sociales':get_redes(),
        'web':get_web(),
        }
        return render(request,'list_search.html',contexto)

def mi_error_404(request, exception):
    nombre_template = '404.html'
 
    return page_not_found(request, template_name=nombre_template)