"""TidalPrediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # admin page
    path('admin/', admin.site.urls),
    # index page
    path('', views.index, name='index'),
    # introduction pages
    path('introduce/', include('introduce.urls')),
    # dashboard page
    path('dashboard/', include('dashboard.urls')),
    # contact page
    path('contact/', include('contact.urls')),
    # ico for all pages
    url(r'^favicon.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    # django-mdeditor
    url(r'mdeditor/', include('mdeditor.urls'))
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


