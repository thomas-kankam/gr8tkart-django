from django.contrib import admin
from .models import Category

# Register your models here.

# adding the prepopulated_fields dictionary to the CategoryAdmin class
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}

admin.site.register(Category, CategoryAdmin)

