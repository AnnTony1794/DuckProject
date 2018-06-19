from django.db import models
from ckeditor.fields import RichTextField
from blog.models import Category
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    image = models.ImageField(verbose_name='Imagen', upload_to='courses')
    content = RichTextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    categories = models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_blogPost')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = "Cursos"
        ordering = ['-created']
    
    def __str__(self):
        return self.title