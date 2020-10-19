from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = "Categorias"
        ordering = ['-created']
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name



class Blog(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='blogs'
    )
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
    content = models.TextField (verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicacion', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog')
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.SET_DEFAULT, default='Anonimo')
    categories = models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_posts')
    created = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = "Publicaciones"
        ordering = ['-created']
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='user_commnets'
    )
    blog = models.ForeignKey(
        'blog.Blog',
        on_delete=models.CASCADE,
        verbose_name=_('Blog'),
        related_name='comments'
    )
    content = models.TextField (verbose_name='Contenido')
    created = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')