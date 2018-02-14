from django.conf.urls import url
from . import views

app_name = 'enuda_mag'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post_create/$', views.post_create, name='post_create'),
    url(r'^post_detail/(?P<slug>[-\w\d\_]+)/$', views.post_detail, name='post_detail'),
    url(r'^create_comment/(?P<blog_post>[0-9]+)/$',
        views.CreateComment.as_view(), name="create_comment"),

]

