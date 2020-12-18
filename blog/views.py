from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.defaults import page_not_found
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.conf import settings

from .models import Post, Comment, Tag
from users.models import CustomUser, Profile

# Create your views here.

def blog_home_page(request):

    posts = Post.objects.all().order_by('-post_timestamp')

    paginate = Paginator(posts, 12)

    page_num = request.GET.get('page', 1)

    try:
        page = paginate.page(page_num)
    except EmptyPage:
        page = paginate.page(1)

    posts = page

    context = {
        'posts': posts,
        'page_obj': page,
    }

    return render(request, 'blog/index.html', context)

def blog_page(request, blogId):

    try:
        post = Post.objects.get(id=blogId)
    except Post.DoesNotExist:
        raise Http404("No Blog Posts matches the given query.")

    comments = post.comment_set.all()

    tags = post.tags.all()

    latest_posts = Post.objects.all().order_by('-post_timestamp')[:3]

    context = {
        'post': post,
        'comments': comments,
        'latest_posts': latest_posts,
        'tags': tags,
    }

    return render(request, 'blog/blog.html', context)