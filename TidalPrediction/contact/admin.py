from django.contrib import admin
from .models import Valine

# Register your models here.
@admin.register(Valine)
class ValineAdmin(admin.ModelAdmin):
    list_display = ['appid', 'appkey', 'avatar', 'pagesize', 'placeholder']
