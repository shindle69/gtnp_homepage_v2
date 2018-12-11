from django.urls import path,include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('company/', views.company, name='company'),    
    path('iot/', views.iot, name='iot'),
    path('web/', views.web, name='web'),
    path('app/', views.app, name='app'),
    path('series/', views.series, name='series'),
    path('root/', views.root, name='root'),
]
