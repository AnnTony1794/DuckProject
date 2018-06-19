from django.contrib import admin
from .models import Course
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields = ('title',  'created')
    list_filter = ('title', 'categories__name')
    list_display = ('title', 'list_display_categories')

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