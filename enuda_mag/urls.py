from django.conf.urls import url
from . import views

app_name = 'enuda_mag'
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^post_detail/$', views.post_detail, name='post_detail'),
    url(r'^post_create/$', views.post_create, name='post_create'),

]

