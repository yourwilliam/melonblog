from django.contrib import admin
from blog.models import Category, Entry

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('content',{'fields': ['title','slug','content','blog_abstract','status']}),
        ('head image', {'fields':['head_image','head_image_url']}),
        ('time', {'fields': ['publication_date','start_publication','end_publication','creation_date','last_update'], 'classes': ['collapse']}),
        ('catalog',{'fields':['categorys']}),
    ]
    list_display = ('title', 'slug', 'status', 'creation_date', 'last_update')
    search_fields = ['title', 'slug']
    #django support 2 method of many to many javascript method. One is filter_horizontal, The other is filter_vertical
    filter_horizontal = ("categorys",)
    list_filter = ("status",)
    list_per_page = 20
    
    
class CatagoryAdmin(admin.ModelAdmin):
    fields = ("title","slug","description")
    list_display = ('title', 'slug')

admin.site.register(Category)
admin.site.register(Entry, EntryAdmin)