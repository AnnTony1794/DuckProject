from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Pages(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='core')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateField(auto_now=True, verbose_name='Fecha de ultima edicion')

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'
        ordering = ['-created']

    def __str__(self):
        return self.title