from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

ACTION_METHOD = (
        ('pt-page-moveToLeft', 'pt-page-moveToLeft'),
        ('pt-page-moveFromLeft', 'pt-page-moveFromLeft'),
        ('pt-page-moveToRight', 'pt-page-moveToRight'),
        ('pt-page-moveFromRight', 'pt-page-moveFromRight'),
        ('pt-page-moveToTop', 'pt-page-moveToTop'),
        ('pt-page-moveFromTop', 'pt-page-moveFromTop'),
        ('pt-page-moveToBottom', 'pt-page-moveToBottom'),
        ('pt-page-moveFromBottom', 'pt-page-moveFromBottom'),
        ('pt-page-moveToLeftFade', 'pt-page-moveToLeftFade'),
        ('pt-page-moveFromLeftFade', 'pt-page-moveFromLeftFade'),
        ('pt-page-moveToRightFade', 'pt-page-moveToRightFade'),
        ('pt-page-moveFromRightFade', 'pt-page-moveFromRightFade'),
        ('pt-page-moveToTopFade', 'pt-page-moveToTopFade'),
        ('pt-page-moveFromTopFade', 'pt-page-moveFromTopFade'),
        ('pt-page-moveToBottomFade', 'pt-page-moveToBottomFade'),
        ('pt-page-moveFromBottomFade', 'pt-page-moveFromBottomFade'),
        ('pt-page-moveToLeftEasing', 'pt-page-moveToLeftEasing'),
        ('pt-page-moveToRightEasing', 'pt-page-moveToRightEasing'),
        ('pt-page-moveToTopEasing', 'pt-page-moveToTopEasing'),
        ('pt-page-moveToBottomEasing', 'pt-page-moveToBottomEasing'),
        ('pt-page-moveIconUp', 'pt-page-moveIconUp'),
        ('pt-page-moveCircle', 'pt-page-moveCircle'),
        ('pt-page-scaleDown', 'pt-page-scaleDown'),
        ('pt-page-scaleUp', 'pt-page-scaleUp'),
        ('pt-page-scaleUpDown', 'pt-page-scaleUpDown'),
        ('pt-page-scaleDownUp', 'pt-page-scaleDownUp'),
        ('pt-page-scaleDownCenter', 'pt-page-scaleDownCenter'),
        ('pt-page-scaleUpCenter', 'pt-page-scaleUpCenter'),
        ('pt-page-rotateRightSideFirst', 'pt-page-rotateRightSideFirst'),
        ('pt-page-rotateLeftSideFirst', 'pt-page-rotateLeftSideFirst'),
        ('pt-page-rotateTopSideFirst', 'pt-page-rotateTopSideFirst'),
        ('pt-page-rotateBottomSideFirst', 'pt-page-rotateBottomSideFirst'),
        ('pt-page-flipOutRight', 'pt-page-flipOutRight'),
        ('pt-page-flipInLeft', 'pt-page-flipInLeft'),
        ('pt-page-flipOutLeft', 'pt-page-flipOutLeft'),
        ('pt-page-flipInRight', 'pt-page-flipInRight'),
        ('pt-page-flipOutTop', 'pt-page-flipOutTop'),
        ('pt-page-flipInBottom', 'pt-page-flipInBottom'),
        ('pt-page-flipOutBottom', 'pt-page-flipOutBottom'),
        ('pt-page-flipInTop', 'pt-page-flipInTop'),
        ('pt-page-rotateFall', 'pt-page-rotateFall'),
        ('pt-page-rotateOutNewspaper', 'pt-page-rotateOutNewspaper'),
        ('pt-page-rotateInNewspaper', 'pt-page-rotateInNewspaper'),
        ('pt-page-rotatePushLeft', 'pt-page-rotatePushLeft'),
        ('pt-page-rotatePushRight', 'pt-page-rotatePushRight'),
        ('pt-page-rotatePushTop', 'pt-page-rotatePushTop'),
        ('pt-page-rotatePushBottom', 'pt-page-rotatePushBottom'),
        ('pt-page-rotatePullRight', 'pt-page-rotatePullRight'),
        ('pt-page-rotatePullLeft', 'pt-page-rotatePullLeft'),
        ('pt-page-rotatePullTop', 'pt-page-rotatePullTop'),
        ('pt-page-rotatePullBottom', 'pt-page-rotatePullBottom'),
        ('pt-page-rotateFoldRight', 'pt-page-rotateFoldRight'),
        ('pt-page-rotateFoldLeft', 'pt-page-rotateFoldLeft'),
        ('pt-page-rotateFoldTop', 'pt-page-rotateFoldTop'),
        ('pt-page-rotateFoldBottom', 'pt-page-rotateFoldBottom'),
        ('pt-page-rotateUnfoldLeft', 'pt-page-rotateUnfoldLeft'),
        ('pt-page-rotateUnfoldRight', 'pt-page-rotateUnfoldRight'),
        ('pt-page-rotateUnfoldTop', 'pt-page-rotateUnfoldTop'),
        ('pt-page-rotateUnfoldBottom', 'pt-page-rotateUnfoldBottom'),
        ('pt-page-rotateRoomLeftOut', 'pt-page-rotateRoomLeftOut'),
        ('pt-page-rotateRoomLeftIn', 'pt-page-rotateRoomLeftIn'),
        ('pt-page-rotateRoomRightOut', 'pt-page-rotateRoomRightOut'),
        ('pt-page-rotateRoomRightIn', 'pt-page-rotateRoomRightIn'),
        ('pt-page-rotateRoomTopOut', 'pt-page-rotateRoomTopOut'),
        ('pt-page-rotateRoomTopIn', 'pt-page-rotateRoomTopIn'),
        ('pt-page-rotateRoomBottomOut', 'pt-page-rotateRoomBottomOut'),
        ('pt-page-rotateRoomBottomIn', 'pt-page-rotateRoomBottomIn'),
        ('pt-page-rotateCubeLeftOut', 'pt-page-rotateCubeLeftOut'),
        ('pt-page-rotateCubeLeftIn', 'pt-page-rotateCubeLeftIn'),
        ('pt-page-rotateCubeRightOut', 'pt-page-rotateCubeRightOut'),
        ('pt-page-rotateCubeRightIn', 'pt-page-rotateCubeRightIn'),
        ('pt-page-rotateCubeTopOut', 'pt-page-rotateCubeTopOut'),
        ('pt-page-rotateCubeTopIn', 'pt-page-rotateCubeTopIn'),
        ('pt-page-rotateCubeBottomOut', 'pt-page-rotateCubeBottomOut'),
        ('pt-page-rotateCubeBottomIn', 'pt-page-rotateCubeBottomIn'),
        ('pt-page-rotateCarouselLeftOut', 'pt-page-rotateCarouselLeftOut'),
        ('pt-page-rotateCarouselLeftIn', 'pt-page-rotateCarouselLeftIn'),
        ('pt-page-rotateCarouselRightOut', 'pt-page-rotateCarouselRightOut'),
        ('pt-page-rotateCarouselRightIn', 'pt-page-rotateCarouselRightIn'),
        ('pt-page-rotateCarouselTopOut', 'pt-page-rotateCarouselTopOut'),
        ('pt-page-rotateCarouselTopIn', 'pt-page-rotateCarouselTopIn'),
        ('pt-page-rotateCarouselBottomOut', 'pt-page-rotateCarouselBottomOut'),
        ('pt-page-rotateCarouselBottomIn', 'pt-page-rotateCarouselBottomIn'),
        ('pt-page-rotateSidesOut', 'pt-page-rotateSidesOut'),
        ('pt-page-rotateSidesIn', 'pt-page-rotateSidesIn'),
        ('pt-page-rotateSlideOut', 'pt-page-rotateSlideOut'),
        ('pt-page-rotateSlideIn', 'pt-page-rotateSlideIn'),
    )

class MobileShow(models.Model):
    name = models.CharField("name", max_length=255)
    description = models.TextField("description", null=True, blank=True)
    publication_date = models.DateTimeField("publication date", db_index=True, default=timezone.now, help_text="Used to build the entry's URL.")
    start_publication = models.DateTimeField("start publication", db_index=True, blank=True, null=True, help_text="Start date of publication.")
    end_publication = models.DateTimeField("end publication", db_index=True, blank=True, null=True, help_text="End date of publication.")
    creation_date = models.DateTimeField("creation date", default=timezone.now)
    last_update = models.DateTimeField("last update", default=timezone.now)
    
    def __unicode__(self):
        return self.name
    
class Page(models.Model):
    name = models.CharField("name", max_length=255)
    PAGE_ATTR = (
        ('page-cuttent','page-current'),          
        ('hide','hide'),
    )
    attribute = models.CharField("attribute",max_length=50,choices=PAGE_ATTR)
    mobile_show = models.ForeignKey(MobileShow)
    
    def __unicode__(self):
        return self.name
    
class ContentImg(models.Model):
    name = models.CharField("name", max_length=255)
    action = models.CharField("action",max_length=50, choices=ACTION_METHOD)
    image = models.ImageField(upload_to='mshow/%Y/%m', null=True, blank=True)
    page = models.ForeignKey(Page)
    
    def __unicode__(self):
        return self.name
    
class ContentText(models.Model):
    name = models.CharField("name", max_length=255)
    action = models.CharField(max_length=50, choices=ACTION_METHOD)
    description = models.TextField("description", null=True, blank=True)
    page = models.ForeignKey(Page)
    
    def __unicode__(self):
        return self.name
    
    
    
