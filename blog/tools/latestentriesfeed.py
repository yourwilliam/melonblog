'''
Created on 2016-6-6

@author: valentine
'''
from django.contrib.syndication.views import Feed
from blog.models import Entry
from django.core.urlresolvers import reverse


class LatestEntriesFeed(Feed):
    title = "william blog"
    link = 'blog'
    description = 'Updates on changes and additions to police beat central.'

    def items(self):
        return Entry.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('blog:single', args=[item.pk])
