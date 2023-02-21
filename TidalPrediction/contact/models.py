from django.db import models


# Create your models here.
class Valine(models.Model):
    """ valine 评论"""
    appid = models.CharField(max_length=100, verbose_name='appId')
    appkey = models.CharField(max_length=100, verbose_name='appKey')
    avatar = models.CharField(default='', blank=True, max_length=100, verbose_name='发帖形象')
    pagesize = models.IntegerField(default='10', verbose_name='pageSize')
    placeholder = models.CharField(max_length=100, verbose_name='占位描述')

    class Meta:
        verbose_name = 'valine评论'
        verbose_name_plural = verbose_name
