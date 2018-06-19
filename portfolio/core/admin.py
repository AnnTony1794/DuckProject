from django.contrib import admin
from .models import Pages
from blog.models import Category
# Register your models here.
@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields = ('title',)

   