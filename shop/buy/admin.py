from django.contrib import admin
from .models import *

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'is_published')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug' : ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Goods, GoodsAdmin)
admin.site.register(Category, CategoryAdmin)