from django.urls import path, include
from . import views

urlpatterns = [
    # contact page
    path('', views.contact, name='contact')
]