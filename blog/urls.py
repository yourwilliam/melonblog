"""TestSite URL Configuration

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
from django.conf.urls import url
from . import views
from blog.tools import latestentriesfeed


urlpatterns = [
    url(r'^$', views.blog, name="index"),
    url(r'^blog', views.blog, name="blog"),
    url(r'^single/(?P<post_id>[0-9]+)/$', views.single, name="single"),
    url(r'^category/(?P<category_id>[0-9]+)/$',
        views.category, name="category"),
    url(r'^tags/(?P<tag_id>[0-9]+)/$', views.taglist, name="tags"),
    url(r'^bookmark', views.bookmarklist, name="bookmark"),
    url(r'^appcategory/(?P<appcategory_id>[0-9]+)/$',
        views.appcategory, name="appcategory"),
    url(r'^contact', views.contact, name="contact"),
    url(r'^sendmail', views.sendmail, name="sendmail"),
    url(r'^latest/feed/$', latestentriesfeed.LatestEntriesFeed(),
        name="latestentriesfeed"),
    url(r'^crawler', views.crawler, name="crawler"),
    url(r'^tools', views.tools, name="tools"),
    url(r'^readdoc', views.readdoc, name="readdoc"),
]
