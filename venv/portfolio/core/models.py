from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Pages(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content =models.TextField (verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='core')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateField(auto_now=True, verbose_name='Fecha de ultima edicion')

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='pages'
    )

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'
        ordering = ['-created']

    def __str__(self):
        return self.title