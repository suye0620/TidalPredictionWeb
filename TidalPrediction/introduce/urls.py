from django.urls import path, include
from . import views

urlpatterns = [
    # The portfolio of introduction pages
    path('portfolio/', views.portfolio, name='portfolio_of_introduction'),
    path('detail/<int:id>/', views.introduction_detail, name='introduction_detail')

]
