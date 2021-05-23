from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pdf-home'),
    path('text/', views.text, name='pdf-text'),
    path('chart/', views.chart, name='pdf-chart'),
    path('table/', views.table, name='pdf-table'),
]
