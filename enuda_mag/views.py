from django.shortcuts import render
from .forms import BlogPostForm
from . import models

# Create your views here.
def index(request):
    return render(request, 'enuda_mag/index.html')


def post_detail(request):
    first_blog = models.BlogPost.objects.first()
    context = {'first_blog': first_blog}
    return render(request, 'enuda_mag/post_detail.html', context)


def post_edit(request):
    form = BlogPostForm()
    return render(request, 'enuda_mag/post_edit.html', {'form': form})