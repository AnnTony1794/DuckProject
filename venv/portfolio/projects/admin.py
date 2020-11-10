from django.contrib import admin
from .models import Project

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields = ('title',  'created')
    list_filter = ('title',)
    list_display = ('title',)