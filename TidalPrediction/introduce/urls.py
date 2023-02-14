from django.urls import path, include
from . import views

urlpatterns = [
    # index page
    path('portfolio/', views.portfolio, name='portfolio_of_introduction')
]