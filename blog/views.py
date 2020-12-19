from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.defaults import page_not_found
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.conf import settings

from .models import Post, Comment, Tag
from users.models import CustomUser, Profile
from .forms import CommentForm
from .filters import PostFilter

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
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                print(Comment.objects.get(author=request.user))
            except Comment.DoesNotExist:
                # raise Http404("No Comments matches the given query.")
                form = CommentForm(request.POST)
                if form.is_valid():
                    comment_text = form.cleaned_data.get('comment_text')

                    try:
                        post = Post.objects.get(id=blogId)
                    except Post.DoesNotExist:
                        raise Http404("No Blog Posts matches the given query.")

                    comment = form.save(commit=False)

                    comment.parent_post = post
                    comment.author = request.user

                    comment.save()

                    print(f'Comment: "{comment_text}" has been saved.')

                    return redirect('blog_page', blogId)
                else:
                    print('Form was not valid\n')
                    print(form.errors)
                    return redirect('blog_page', blogId)

            print('This user already has posted a comment.')

            return redirect('blog_page', blogId)
        else:
            print('User was not authenticated')
            return redirect('landing_page')

    else:
        try:
            post = Post.objects.get(id=blogId)
        except Post.DoesNotExist:
            raise Http404("No Blog Posts matches the given query.")

        comments = post.comment_set.all()

        tags = post.tags.all()

        latest_posts = Post.objects.all().order_by('-post_timestamp')[:3]

        form = CommentForm()

        context = {
            'post': post,
            'comments': comments,
            'latest_posts': latest_posts,
            'tags': tags,
            'form': form,
        }

        return render(request, 'blog/blog.html', context)


def blog_search_page(request):
    posts = Post.objects.all()

    postFilter = PostFilter(request.GET, queryset=posts)

    posts = postFilter.qs

    paginate = Paginator(posts, 5)

    page_num = request.GET.get('page', 1)

    try:
        page = paginate.page(page_num)
    except EmptyPage:
        page = paginate.page(1)

    posts = page

    context = {
        'postFilter': postFilter,
        'posts': posts,
        'page_obj': page,
    }
    # do some searching using query string, and send that to the template
    return render(request, 'blog/search.html', context)


def not_found_page(request, exception):
    context = {
        'message': "Page you are looking for does not exists or has been removed."
    }
    return render(request, 'blog/404.html', context)

def not_found_page_server(request):
    context = {
        'message': "There seems to be an issue on our side. We will be back shortly!"
    }
    return render(request, 'blog/404.html', context)