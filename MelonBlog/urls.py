"""MelonBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from MelonBlog import settings
from blog import views
import django.views
from django.contrib.sitemaps.views import sitemap
from blog.models import Entry
from django.contrib.sitemaps import GenericSitemap

sitemaps = {
    'blog': GenericSitemap({'queryset': Entry.objects.all(), 'date_field': 'publication_date'}, priority=0.6),
}

urlpatterns = [
    url(r'^$', views.blog, name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^mshow/', include('mshow.urls', namespace='mshow')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]
