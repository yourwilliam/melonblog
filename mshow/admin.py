from django.contrib import admin
from mshow.models import Page, MobileShow, ContentImg, ContentText

# Register your models here.
class ContentImgInline(admin.TabularInline):
    model = ContentImg
    extra = 4
    
class ContentTextInline(admin.TabularInline):
    model = ContentText
    extra = 1

class PageInLine(admin.TabularInline):
    model = Page
    extra = 4

class MobileShowAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','description']}),
        ('time', {'fields': ['publication_date','start_publication','end_publication','creation_date','last_update'], 'classes': ['collapse']}),

    ]
    inlines = [PageInLine]
    list_display = ('name', 'description', 'creation_date')
    list_filter = ['creation_date']
    search_fields = ['name']

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['name','attribute','mobile_show']}),
    ]
    inlines = [ContentImgInline, ContentTextInline]
    list_display  = ('name','attribute', 'mobile_show')
    list_filter = ['mobile_show']
    search_fields = ['name', 'attribute','mobile_show']
    
admin.site.register(MobileShow, MobileShowAdmin)
admin.site.register(Page, PageAdmin)