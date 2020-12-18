from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.defaults import page_not_found
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.conf import settings

# Create your views here.

def blog_home_page(request):
    return render(request, 'blog/index.html')