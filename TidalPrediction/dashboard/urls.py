from django.urls import path, include
from . import views

urlpatterns = [
    # dashboard page
    path('', views.dashboard, name='dashboard')
]