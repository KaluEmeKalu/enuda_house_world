from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . forms import (
    UserLoginForm,
    CreateUserForm,
    UserImageForm,
    BlogPostForm)
from django.views.generic.edit import (
    CreateView,
    UpdateView)
from django.views.generic import View
from django.contrib.auth.decorators import (
    login_required,
    user_passes_test)
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    blog_posts = models.BlogPost.objects.all()
    context = {'blog_posts': blog_posts}
    return render(request, 'enuda_mag/index.html', context)


def post_detail(request, slug):
    blog_post = get_object_or_404(models.BlogPost, slug=slug)
    blog_posts = models.BlogPost.objects.all()

    print(blog_post.content)
    context = {'blog_post': blog_post, 'blog_posts': blog_posts}
    if request.method == "POST":
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            return redirect('enuda_mag:post_detail')
    else:
        form = BlogPostForm()
        context['form'] = form
    return render(request, 'enuda_mag/post_detail.html', context)

def post_create(request):

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)

        if form.is_valid():
            blog_post = form.save()
            blog_post.user = request.user
            blog_post.save()
            return redirect('enuda_mag:post_detail')

    return render(request, 'enuda_mag/post_create.html', {'form': BlogPostForm()})



def post_create(request):

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)

        if form.is_valid():
            blog_post = form.save()
            blog_post.user = request.user
            blog_post.save()
            return redirect('enuda_mag:post_detail')

    return render(request, 'enuda_mag/post_create.html', {'form': BlogPostForm()})

class CreateComment(CreateView):
    model = models.Comment
    template_name = 'dashboard/create_comment.html'
    fields = [
        'content'
    ]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context

        context = super(CreateComment, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['blog_post'] = int(self.kwargs['blog_post'])
        return context

    def form_valid(self, form):
        blog_post = models.BlogPost.objects.get(pk=self.kwargs['blog_post'])
        form.save()
        form.instance.blog_post = blog_post
        form.instance.user = self.request.user
        form.save()

        previous_url = self.request.META['HTTP_REFERER']

        return HttpResponseRedirect(previous_url)

#Authenticaiton Views
class RegisterView(View):

    form_class = CreateUserForm
    template_name = 'enuda_mag/register.html'

    def get(self, request):

        if request.user.is_authenticated:
            return redirect('enuda_mag:index')
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']

            user.set_password(password)
            user.username = username
            user.save()

            # returns User objects if credentilas are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    # change this. This is error
                    return redirect('enuda_mag:index')
        else:
            messages.error(request, form.errors)
            return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'enuda_mag/login.html'

    def get(self, request):

        if request.user.is_authenticated():
            return redirect('enuda_mag:index')
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # potential bug if username created somehow with uppercase letters
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                url = settings.SITE_URL
                previous_url = self.request.META['HTTP_REFERER']
                login(request, user)
                # For to Previously Clicked Url
                if '?next=' in previous_url:
                    start_point = previous_url.find('?next=') + 7
                    new_url = url + previous_url[start_point:]
                    return HttpResponseRedirect(new_url)
                return redirect('enuda_mag:index')
            else:
                # An inactive account was used - no logging in!
                messages.error(request, 'Your account is disable')
                form = self.form_class(None)
                context = {'form': form}
                return render(request, self.template_name, context)

        messages.error(request, 'Your username or password did not match')
        form = self.form_class(None)
        context = {'form': form}
        return render(request, self.template_name, context)


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect('enuda_mag:index')


@login_required
def change_user_image(request):
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)

        if form.is_valid():

            # if there is no user_profile create one
            try:
                user_profile = request.user.user_profile
            except Exception as the_exception:
                if the_exception.__str__() == "User has no user_profile.":
                    a = UserProfile(user=request.user)
                    a.save()
                    user_profile = a

            user_image = form.save(commit=False)
            user_image.save()

            user_profile.all_profile_pics.add(user_image)
            user_profile.profile_pic = user_image
            user_profile.save()

            return redirect('enuda_mag:index')

    return render(request, 'enuda_mag/change_user_pic.html', {'form': UserImageForm()})