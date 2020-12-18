from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.blog_home_page, name='blog_home_page'),
    path('<int:blogId>/', views.blog_page, name='blog_page'),
    path('search/', views.blog_search_page, name='blog_search_page'),
    path('', views.blog_home_page, name='blog_home_page_2'),
]