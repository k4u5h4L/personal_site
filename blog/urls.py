from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.blog_home_page, name='blog_home_page'),
    path('<int:blogId>/', views.blog_page, name='blog_page'),
]