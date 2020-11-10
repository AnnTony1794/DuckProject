from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth import get_user_model
from django.db import models

from blog.models import Category
# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=200, verbose_name='Escuela')

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='courses')
    content = models.TextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    categories = models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_blogPost')

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='courses'
    )
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = "Cursos"
        ordering = ['-created']
    
    def __str__(self):
        return self.title

