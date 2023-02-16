from django.urls import path, include
from . import views

urlpatterns = [
    # The portfolio of introduction pages
    path('portfolio/', views.portfolio, name='portfolio_of_introduction'),
    path('introduction/', views.introduce, name='introduction')

]
