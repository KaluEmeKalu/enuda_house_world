from django.shortcuts import render
from .forms import BlogPostForm

# Create your views here.
def index(request):
    return render(request, 'enuda_mag/index.html')


def post_detail(request):
    return render(request, 'enuda_mag/post_detail.html')


def post_edit(request):
    form = BlogPostForm()
    return render(request, 'enuda_mag/post_edit.html', {'form': form})