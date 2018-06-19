from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Blog, Category
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields = ('title', 'author__username', 'created')
    list_filter = ('author__username', 'categories__name')
    list_display = ('title', 'author', 'list_display_categories')

    def list_display_categories(self, categories):
        #return ', '.join([category.name for category in categories.categories.all().order_by('name')])
        
        html_categories = ['<option>{}</option>'.format(category) for category in categories.categories.all().order_by('name')]
        html_response = '''
        <select>
            {}
        </select>
        '''.format(html_categories)

        return mark_safe(html_response)

    list_display_categories.short_description = 'Categorias'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
