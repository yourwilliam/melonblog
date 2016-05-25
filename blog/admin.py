from django.contrib import admin
from blog.models import Category, Entry, BookmarkCategory, Bookmark
from pagedown.widgets import AdminPagedownWidget
from django.db import models

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('content',{'fields': ['title','slug', 'tags','content','blog_abstract','status']}),
        ('head image', {'fields':['head_image','head_image_url']}),
        ('time', {'fields': ['publication_date','start_publication','end_publication','creation_date','last_update'], 'classes': ['collapse']}),
        ('catalog',{'fields':['categorys']}),
    ]
    list_display = ('title', 'slug', 'tags', 'status', 'creation_date', 'last_update')
    search_fields = ['title', 'slug', 'tags']
    #django support 2 method of many to many javascript method. One is filter_horizontal, The other is filter_vertical
    filter_horizontal = ('categorys',)
    list_filter = ('status',)
    list_per_page = 20
    formfield_overrides= {
        models.TextField : {'widget': AdminPagedownWidget},
    }
      
    
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title','slug','description')
    list_display = ('title', 'slug')

class BookmarkCategoryAdmin(admin.ModelAdmin):
    field = ('title', 'slug', 'description')
    list_display = ('title', 'slug')
    
class BookmarkAdmin(admin.ModelAdmin):
    fieldsets = [
        ('content',{'fields':['title', 'slug', 'description', 'status', 'url', 'head_image']}),
        ('others',{'fields':['creation_date','click_times', 'categorys']}),
    ]
    list_display = ('title', 'slug', 'url', 'creation_date', 'status', 'click_times')
    search_fields = ['title', 'slug', 'url']
    filter_horizontal = ('categorys',)
    list_filter = ('status',)
    list_per_page = 20


admin.site.register(Category)
admin.site.register(Entry, EntryAdmin)
admin.site.register(BookmarkCategory)
admin.site.register(Bookmark, BookmarkAdmin)
