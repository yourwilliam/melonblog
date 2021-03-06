# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('action', models.CharField(choices=[('pt-page-moveToLeft', 'pt-page-moveToLeft'), ('pt-page-moveFromLeft', 'pt-page-moveFromLeft'), ('pt-page-moveToRight', 'pt-page-moveToRight'), ('pt-page-moveFromRight', 'pt-page-moveFromRight'), ('pt-page-moveToTop', 'pt-page-moveToTop'), ('pt-page-moveFromTop', 'pt-page-moveFromTop'), ('pt-page-moveToBottom', 'pt-page-moveToBottom'), ('pt-page-moveFromBottom', 'pt-page-moveFromBottom'), ('pt-page-moveToLeftFade', 'pt-page-moveToLeftFade'), ('pt-page-moveFromLeftFade', 'pt-page-moveFromLeftFade'), ('pt-page-moveToRightFade', 'pt-page-moveToRightFade'), ('pt-page-moveFromRightFade', 'pt-page-moveFromRightFade'), ('pt-page-moveToTopFade', 'pt-page-moveToTopFade'), ('pt-page-moveFromTopFade', 'pt-page-moveFromTopFade'), ('pt-page-moveToBottomFade', 'pt-page-moveToBottomFade'), ('pt-page-moveFromBottomFade', 'pt-page-moveFromBottomFade'), ('pt-page-moveToLeftEasing', 'pt-page-moveToLeftEasing'), ('pt-page-moveToRightEasing', 'pt-page-moveToRightEasing'), ('pt-page-moveToTopEasing', 'pt-page-moveToTopEasing'), ('pt-page-moveToBottomEasing', 'pt-page-moveToBottomEasing'), ('pt-page-moveIconUp', 'pt-page-moveIconUp'), ('pt-page-moveCircle', 'pt-page-moveCircle'), ('pt-page-scaleDown', 'pt-page-scaleDown'), ('pt-page-scaleUp', 'pt-page-scaleUp'), ('pt-page-scaleUpDown', 'pt-page-scaleUpDown'), ('pt-page-scaleDownUp', 'pt-page-scaleDownUp'), ('pt-page-scaleDownCenter', 'pt-page-scaleDownCenter'), ('pt-page-scaleUpCenter', 'pt-page-scaleUpCenter'), ('pt-page-rotateRightSideFirst', 'pt-page-rotateRightSideFirst'), ('pt-page-rotateLeftSideFirst', 'pt-page-rotateLeftSideFirst'), ('pt-page-rotateTopSideFirst', 'pt-page-rotateTopSideFirst'), ('pt-page-rotateBottomSideFirst', 'pt-page-rotateBottomSideFirst'), ('pt-page-flipOutRight', 'pt-page-flipOutRight'), ('pt-page-flipInLeft', 'pt-page-flipInLeft'), ('pt-page-flipOutLeft', 'pt-page-flipOutLeft'), ('pt-page-flipInRight', 'pt-page-flipInRight'), ('pt-page-flipOutTop', 'pt-page-flipOutTop'), ('pt-page-flipInBottom', 'pt-page-flipInBottom'), ('pt-page-flipOutBottom', 'pt-page-flipOutBottom'), ('pt-page-flipInTop', 'pt-page-flipInTop'), ('pt-page-rotateFall', 'pt-page-rotateFall'), ('pt-page-rotateOutNewspaper', 'pt-page-rotateOutNewspaper'), ('pt-page-rotateInNewspaper', 'pt-page-rotateInNewspaper'), ('pt-page-rotatePushLeft', 'pt-page-rotatePushLeft'), ('pt-page-rotatePushRight', 'pt-page-rotatePushRight'), ('pt-page-rotatePushTop', 'pt-page-rotatePushTop'), ('pt-page-rotatePushBottom', 'pt-page-rotatePushBottom'), ('pt-page-rotatePullRight', 'pt-page-rotatePullRight'), ('pt-page-rotatePullLeft', 'pt-page-rotatePullLeft'), ('pt-page-rotatePullTop', 'pt-page-rotatePullTop'), ('pt-page-rotatePullBottom', 'pt-page-rotatePullBottom'), ('pt-page-rotateFoldRight', 'pt-page-rotateFoldRight'), ('pt-page-rotateFoldLeft', 'pt-page-rotateFoldLeft'), ('pt-page-rotateFoldTop', 'pt-page-rotateFoldTop'), ('pt-page-rotateFoldBottom', 'pt-page-rotateFoldBottom'), ('pt-page-rotateUnfoldLeft', 'pt-page-rotateUnfoldLeft'), ('pt-page-rotateUnfoldRight', 'pt-page-rotateUnfoldRight'), ('pt-page-rotateUnfoldTop', 'pt-page-rotateUnfoldTop'), ('pt-page-rotateUnfoldBottom', 'pt-page-rotateUnfoldBottom'), ('pt-page-rotateRoomLeftOut', 'pt-page-rotateRoomLeftOut'), ('pt-page-rotateRoomLeftIn', 'pt-page-rotateRoomLeftIn'), ('pt-page-rotateRoomRightOut', 'pt-page-rotateRoomRightOut'), ('pt-page-rotateRoomRightIn', 'pt-page-rotateRoomRightIn'), ('pt-page-rotateRoomTopOut', 'pt-page-rotateRoomTopOut'), ('pt-page-rotateRoomTopIn', 'pt-page-rotateRoomTopIn'), ('pt-page-rotateRoomBottomOut', 'pt-page-rotateRoomBottomOut'), ('pt-page-rotateRoomBottomIn', 'pt-page-rotateRoomBottomIn'), ('pt-page-rotateCubeLeftOut', 'pt-page-rotateCubeLeftOut'), ('pt-page-rotateCubeLeftIn', 'pt-page-rotateCubeLeftIn'), ('pt-page-rotateCubeRightOut', 'pt-page-rotateCubeRightOut'), ('pt-page-rotateCubeRightIn', 'pt-page-rotateCubeRightIn'), ('pt-page-rotateCubeTopOut', 'pt-page-rotateCubeTopOut'), ('pt-page-rotateCubeTopIn', 'pt-page-rotateCubeTopIn'), ('pt-page-rotateCubeBottomOut', 'pt-page-rotateCubeBottomOut'), ('pt-page-rotateCubeBottomIn', 'pt-page-rotateCubeBottomIn'), ('pt-page-rotateCarouselLeftOut', 'pt-page-rotateCarouselLeftOut'), ('pt-page-rotateCarouselLeftIn', 'pt-page-rotateCarouselLeftIn'), ('pt-page-rotateCarouselRightOut', 'pt-page-rotateCarouselRightOut'), ('pt-page-rotateCarouselRightIn', 'pt-page-rotateCarouselRightIn'), ('pt-page-rotateCarouselTopOut', 'pt-page-rotateCarouselTopOut'), ('pt-page-rotateCarouselTopIn', 'pt-page-rotateCarouselTopIn'), ('pt-page-rotateCarouselBottomOut', 'pt-page-rotateCarouselBottomOut'), ('pt-page-rotateCarouselBottomIn', 'pt-page-rotateCarouselBottomIn'), ('pt-page-rotateSidesOut', 'pt-page-rotateSidesOut'), ('pt-page-rotateSidesIn', 'pt-page-rotateSidesIn'), ('pt-page-rotateSlideOut', 'pt-page-rotateSlideOut'), ('pt-page-rotateSlideIn', 'pt-page-rotateSlideIn')], max_length=50, verbose_name='action')),
                ('image', models.ImageField(blank=True, null=True, upload_to='mshow/%Y/%m')),
            ],
        ),
        migrations.CreateModel(
            name='ContentText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('action', models.CharField(choices=[('pt-page-moveToLeft', 'pt-page-moveToLeft'), ('pt-page-moveFromLeft', 'pt-page-moveFromLeft'), ('pt-page-moveToRight', 'pt-page-moveToRight'), ('pt-page-moveFromRight', 'pt-page-moveFromRight'), ('pt-page-moveToTop', 'pt-page-moveToTop'), ('pt-page-moveFromTop', 'pt-page-moveFromTop'), ('pt-page-moveToBottom', 'pt-page-moveToBottom'), ('pt-page-moveFromBottom', 'pt-page-moveFromBottom'), ('pt-page-moveToLeftFade', 'pt-page-moveToLeftFade'), ('pt-page-moveFromLeftFade', 'pt-page-moveFromLeftFade'), ('pt-page-moveToRightFade', 'pt-page-moveToRightFade'), ('pt-page-moveFromRightFade', 'pt-page-moveFromRightFade'), ('pt-page-moveToTopFade', 'pt-page-moveToTopFade'), ('pt-page-moveFromTopFade', 'pt-page-moveFromTopFade'), ('pt-page-moveToBottomFade', 'pt-page-moveToBottomFade'), ('pt-page-moveFromBottomFade', 'pt-page-moveFromBottomFade'), ('pt-page-moveToLeftEasing', 'pt-page-moveToLeftEasing'), ('pt-page-moveToRightEasing', 'pt-page-moveToRightEasing'), ('pt-page-moveToTopEasing', 'pt-page-moveToTopEasing'), ('pt-page-moveToBottomEasing', 'pt-page-moveToBottomEasing'), ('pt-page-moveIconUp', 'pt-page-moveIconUp'), ('pt-page-moveCircle', 'pt-page-moveCircle'), ('pt-page-scaleDown', 'pt-page-scaleDown'), ('pt-page-scaleUp', 'pt-page-scaleUp'), ('pt-page-scaleUpDown', 'pt-page-scaleUpDown'), ('pt-page-scaleDownUp', 'pt-page-scaleDownUp'), ('pt-page-scaleDownCenter', 'pt-page-scaleDownCenter'), ('pt-page-scaleUpCenter', 'pt-page-scaleUpCenter'), ('pt-page-rotateRightSideFirst', 'pt-page-rotateRightSideFirst'), ('pt-page-rotateLeftSideFirst', 'pt-page-rotateLeftSideFirst'), ('pt-page-rotateTopSideFirst', 'pt-page-rotateTopSideFirst'), ('pt-page-rotateBottomSideFirst', 'pt-page-rotateBottomSideFirst'), ('pt-page-flipOutRight', 'pt-page-flipOutRight'), ('pt-page-flipInLeft', 'pt-page-flipInLeft'), ('pt-page-flipOutLeft', 'pt-page-flipOutLeft'), ('pt-page-flipInRight', 'pt-page-flipInRight'), ('pt-page-flipOutTop', 'pt-page-flipOutTop'), ('pt-page-flipInBottom', 'pt-page-flipInBottom'), ('pt-page-flipOutBottom', 'pt-page-flipOutBottom'), ('pt-page-flipInTop', 'pt-page-flipInTop'), ('pt-page-rotateFall', 'pt-page-rotateFall'), ('pt-page-rotateOutNewspaper', 'pt-page-rotateOutNewspaper'), ('pt-page-rotateInNewspaper', 'pt-page-rotateInNewspaper'), ('pt-page-rotatePushLeft', 'pt-page-rotatePushLeft'), ('pt-page-rotatePushRight', 'pt-page-rotatePushRight'), ('pt-page-rotatePushTop', 'pt-page-rotatePushTop'), ('pt-page-rotatePushBottom', 'pt-page-rotatePushBottom'), ('pt-page-rotatePullRight', 'pt-page-rotatePullRight'), ('pt-page-rotatePullLeft', 'pt-page-rotatePullLeft'), ('pt-page-rotatePullTop', 'pt-page-rotatePullTop'), ('pt-page-rotatePullBottom', 'pt-page-rotatePullBottom'), ('pt-page-rotateFoldRight', 'pt-page-rotateFoldRight'), ('pt-page-rotateFoldLeft', 'pt-page-rotateFoldLeft'), ('pt-page-rotateFoldTop', 'pt-page-rotateFoldTop'), ('pt-page-rotateFoldBottom', 'pt-page-rotateFoldBottom'), ('pt-page-rotateUnfoldLeft', 'pt-page-rotateUnfoldLeft'), ('pt-page-rotateUnfoldRight', 'pt-page-rotateUnfoldRight'), ('pt-page-rotateUnfoldTop', 'pt-page-rotateUnfoldTop'), ('pt-page-rotateUnfoldBottom', 'pt-page-rotateUnfoldBottom'), ('pt-page-rotateRoomLeftOut', 'pt-page-rotateRoomLeftOut'), ('pt-page-rotateRoomLeftIn', 'pt-page-rotateRoomLeftIn'), ('pt-page-rotateRoomRightOut', 'pt-page-rotateRoomRightOut'), ('pt-page-rotateRoomRightIn', 'pt-page-rotateRoomRightIn'), ('pt-page-rotateRoomTopOut', 'pt-page-rotateRoomTopOut'), ('pt-page-rotateRoomTopIn', 'pt-page-rotateRoomTopIn'), ('pt-page-rotateRoomBottomOut', 'pt-page-rotateRoomBottomOut'), ('pt-page-rotateRoomBottomIn', 'pt-page-rotateRoomBottomIn'), ('pt-page-rotateCubeLeftOut', 'pt-page-rotateCubeLeftOut'), ('pt-page-rotateCubeLeftIn', 'pt-page-rotateCubeLeftIn'), ('pt-page-rotateCubeRightOut', 'pt-page-rotateCubeRightOut'), ('pt-page-rotateCubeRightIn', 'pt-page-rotateCubeRightIn'), ('pt-page-rotateCubeTopOut', 'pt-page-rotateCubeTopOut'), ('pt-page-rotateCubeTopIn', 'pt-page-rotateCubeTopIn'), ('pt-page-rotateCubeBottomOut', 'pt-page-rotateCubeBottomOut'), ('pt-page-rotateCubeBottomIn', 'pt-page-rotateCubeBottomIn'), ('pt-page-rotateCarouselLeftOut', 'pt-page-rotateCarouselLeftOut'), ('pt-page-rotateCarouselLeftIn', 'pt-page-rotateCarouselLeftIn'), ('pt-page-rotateCarouselRightOut', 'pt-page-rotateCarouselRightOut'), ('pt-page-rotateCarouselRightIn', 'pt-page-rotateCarouselRightIn'), ('pt-page-rotateCarouselTopOut', 'pt-page-rotateCarouselTopOut'), ('pt-page-rotateCarouselTopIn', 'pt-page-rotateCarouselTopIn'), ('pt-page-rotateCarouselBottomOut', 'pt-page-rotateCarouselBottomOut'), ('pt-page-rotateCarouselBottomIn', 'pt-page-rotateCarouselBottomIn'), ('pt-page-rotateSidesOut', 'pt-page-rotateSidesOut'), ('pt-page-rotateSidesIn', 'pt-page-rotateSidesIn'), ('pt-page-rotateSlideOut', 'pt-page-rotateSlideOut'), ('pt-page-rotateSlideIn', 'pt-page-rotateSlideIn')], max_length=50)),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='MobileShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('publication_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now, help_text="Used to build the entry's URL.", verbose_name='publication date')),
                ('start_publication', models.DateTimeField(blank=True, db_index=True, help_text='Start date of publication.', null=True, verbose_name='start publication')),
                ('end_publication', models.DateTimeField(blank=True, db_index=True, help_text='End date of publication.', null=True, verbose_name='end publication')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date')),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last update')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('attribute', models.CharField(choices=[('page-cuttent', 'page-current'), ('hide', 'hide')], max_length=50, verbose_name='attribute')),
                ('mobile_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mshow.MobileShow')),
            ],
        ),
        migrations.AddField(
            model_name='contenttext',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mshow.Page'),
        ),
        migrations.AddField(
            model_name='contentimg',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mshow.Page'),
        ),
    ]
