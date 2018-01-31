from django.shortcuts import render, redirect
from .forms import BlogPostForm
from . import models

# Create your views here.
def index(request):
    return render(request, 'enuda_mag/index.html')


def post_detail(request):
    first_blog = models.BlogPost.objects.first()

    print(first_blog.content)
    context = {'first_blog': first_blog}
    return render(request, 'enuda_mag/post_detail.html', context)



def post_edit(request):

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)

        if form.is_valid():
            blog_post = form.save()
            return redirect('enuda_mag:post_detail')

    return render(request, 'enuda_mag/post_edit.html', {'form': BlogPostForm()})
