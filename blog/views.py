from django.shortcuts import render
from django.utils import timezone

from blog.models import Post


def index(request):
    posts = Post.objects.filter(id=1)
    return render(request, 'blog/index.html', {'posts': posts})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Create your views here.
