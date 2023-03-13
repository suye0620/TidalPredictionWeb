from django.urls import path
from . import views

urlpatterns = [
    # dashboard page
    path('', views.dashboard, name='dashboard'),
    # query and charts
    path('query',views.line_graph,name='query_and_charts')
]