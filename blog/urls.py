from django.urls import path,include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('company/', views.company, name='company'),
    path('moto/', views.moto, name='moto'),
    path('patent/', views.patent, name='patent'),
    path('index/', views.index, name='index'),
]
