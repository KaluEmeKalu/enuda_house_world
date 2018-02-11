from django.shortcuts import render, redirect
from .forms import BlogPostForm, PostForm
from . import models


# Create your views here.
def index(request):
    return render(request, 'enuda_mag/index.html')


def post_detail(request):
    first_blog = models.BlogPost.objects.first()

    print(first_blog.content)
    context = {'first_blog': first_blog}
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            return redirect('enuda_mag:post_detail')
    else:
        form = PostForm()
        context['form'] = form
    return render(request, 'enuda_mag/post_detail.html', context)

def post_create(request):

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)

        if form.is_valid():
            blog_post = form.save()
            return redirect('enuda_mag:post_detail')

    return render(request, 'enuda_mag/post_create.html', {'form': BlogPostForm()})


def post_create_test(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            return redirect('enuda_mag:post_detail')
    else:
        form = PostForm()
    return render(request, 'enuda_mag/post_create.html', {'form': form})