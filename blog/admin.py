from django.contrib import admin
from blog.models import Category, Entry
from pagedown.widgets import AdminPagedownWidget
from django.db import models
from django import forms

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
    filter_horizontal = ("categorys",)
    list_filter = ("status",)
    list_per_page = 20
    formfield_overrides= {
        models.TextField : {'widget': AdminPagedownWidget},
    }
      
    
class CatagoryAdmin(admin.ModelAdmin):
    fields = ("title","slug","description")
    list_display = ('title', 'slug')

admin.site.register(Category)
admin.site.register(Entry, EntryAdmin)