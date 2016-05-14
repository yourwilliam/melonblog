from django.contrib import admin
from blog.models import Category, Entry

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('content',{'fields': ['title','slug','content','status']}),
        ('head image', {'fields':['head_image','head_image_url']}),
        ('time', {'fields': ['publication_date','start_publication','end_publication','creation_date','last_update'], 'classes': ['collapse']}),
        ('catalog',{'fields':['categorys']}),
    ]
    list_display = ('title', 'slug', 'status', 'creation_date', 'last_update')

admin.site.register(Category)
admin.site.register(Entry, EntryAdmin)