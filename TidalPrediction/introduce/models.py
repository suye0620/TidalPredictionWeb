from django.db import models
from datetime import datetime
from django.utils.html import format_html
from mdeditor.fields import MDTextField


# Create your models here.
class Site(models.Model):
    """ some settings of the site """
    site_name = models.CharField(default='TidalPrediction', max_length=30, verbose_name='网站名字')
    keywords = models.CharField(default='关键字测试', max_length=50, verbose_name='网站关键词')
    desc = models.CharField(max_length=50, verbose_name='网站描述')
    slogan = models.CharField(max_length=50, verbose_name='网站标语')
    icp_number = models.CharField(max_length=40, verbose_name='备案号')
    icp_url = models.URLField(default='http://www.beian.miit.gov.cn/', max_length=100, verbose_name='备案链接')
    index_banner = models.URLField(default='https://s2.loli.net/2022/01/03/XJgetwVDfanWPMk.jpg', max_length=100,
                                   verbose_name='首页横幅')

    class Meta:
        verbose_name = '网站设置'
        verbose_name_plural = verbose_name

    def index_banner_preview(self):  # 背景图片预览
        return format_html('<img src="{}" width="120px" height="90px" alt="IndexPageBanner" />', self.index_banner)

    index_banner.short_description = '首页背景预览'

    def __str__(self):
        return self.site_name


class Introduction(models.Model):
    """ some introduction of the project """
    title = models.CharField(max_length=50, verbose_name='标题')
    author = models.CharField(max_length=10, verbose_name='作者', default='Ye.S', blank=True, null=True)
    desc = models.CharField(max_length=50, verbose_name='简要描述')
    cover = models.URLField(max_length=200, default='https://i.loli.net/2020/04/23/lJLjEtbs2NFwynQ.jpg',
                            verbose_name='页面横幅')
    portfolio_icon = models.CharField(max_length=50, default='fas fa-envelope', verbose_name='归档页图标')
    content = MDTextField(verbose_name='详细内容')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    # 文章创建时间。参数 default=datetime.now 指定其在创建数据时将默认写入当前的时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    # 文章更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '介绍'
        verbose_name_plural = verbose_name
        ordering = ('-add_time',)  # 以创建时间倒序排列

    def cover_preview(self):
        return format_html('<img src="{}" width="200px" height="150px"/>', self.cover, )

    cover_preview.short_description = '页面横幅预览'

    def icon_preview(self):
        return format_html('<h1><i class="{}"></i></h1>', self.portfolio_icon)

    icon_preview.short_description = '介绍归档页图标预览'

    def __str__(self):
        return self.title  # 将文章标题返回
