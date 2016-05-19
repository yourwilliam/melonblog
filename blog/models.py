from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from tagging.fields import TagField

# Create your models here.

class Category(models.Model):
    title = models.CharField("title", max_length=255)
    slug = models.SlugField("slug", unique=True, max_length=255, help_text="Used to build the catagory's URL.")
    description = models.TextField("description", blank=True)
    # the TreeForignKey need to install the mptt package and import it , after to import it .
    # parent = TreeForignKey('self', relate_name='children', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('parent catagory'))
    
    def __unicode__(self):
        return self.title
    
class Entry(models.Model):
    
    STATUS_CHOICES = ((0, 'draft'), (1, 'hidden'), (2, 'publish'))
    title = models.CharField("title", max_length=255)
    blog_abstract = models.TextField("blog abstract", null=True, blank=True, max_length=200)
    slug = models.CharField("slug", max_length=255)
    status = models.IntegerField("status", db_index=True, choices=STATUS_CHOICES, default=0)
    publication_date = models.DateTimeField("publication date", db_index=True, default=timezone.now, help_text="Used to build the entry's URL.")
    start_publication = models.DateTimeField("start publication", db_index=True, blank=True, null=True, help_text="Start date of publication.")
    end_publication = models.DateTimeField("end publication", db_index=True, blank=True, null=True, help_text="End date of publication.")
    creation_date = models.DateTimeField("creation date", default=timezone.now)
    last_update = models.DateTimeField("last update", default=timezone.now)
    #content
    content = models.TextField("content", null=True, blank=True)
    # after to convert the content to html or markdown modle. add some method
    categorys = models.ManyToManyField(Category, blank=True, related_name="entries", verbose_name="categories");

    tags = TagField()
    head_image_url = models.URLField("head image url", max_length=255, null=True, blank=True)
    head_image = models.ImageField(upload_to='photos/%Y/%m',null=True, blank=True)
    def __unicode__(self):
        return self.title