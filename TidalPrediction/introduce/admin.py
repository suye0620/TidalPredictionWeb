from django.contrib import admin
from .models import Introduction, Site
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# 修改后台管理页面头部显示内容和后台名称
admin.site.site_header = 'TidalPrediction Admin'
admin.site.site_title = 'TidalPrediction | Admin'


@admin.register(Introduction)
class IntroductionAdmin(ImportExportModelAdmin):
    # 设置要显示在后台列表中的字段
    list_display = ('add_time', 'title', 'cover_preview', 'icon_preview', 'is_recommend', 'update_time')
    list_per_page = 10  # 设置每页显示多少条记录，默认是100条
    list_editable = ['is_recommend']  # 设置默认可编辑字段，在列表里就可以编辑
    ordering = ('-add_time', 'is_recommend')  # 设置默认排序字段，负号表示降序排序
    list_display_links = ('title',)  # 设置哪些字段可以点击进入编辑界面
    search_fields = ('title', 'desc', 'content')  # 置哪些字段可以查询
    list_filter = ('title', 'add_time')  # 过滤器，按字段进行筛选
    date_hierarchy = 'add_time'  # 详细时间分层筛选　
    readonly_fields = ('cover_preview', 'icon_preview')  # 只读字段，添加该字段才能在后台预览封面，否则报错
    fieldsets = (
        # 后台文章编辑页面排版
        ('编辑文章', {
            'fields': ('title', 'author', 'cover', 'cover_preview','portfolio_icon','icon_preview', 'desc', 'content')
        }),
        ('其他设置', {
            'classes': ('collapse',),
            'fields': ('is_recommend', 'add_time'),
        }),
    )

@admin.register(Site)
class SiteAdmin(ImportExportModelAdmin):
    list_display = ['site_name', 'keywords', 'desc', 'slogan', 'index_banner_preview',
                    'icp_number', 'icp_url']