from django.contrib.auth.models import User
from django.db import models
from . models_utils import (
    IntegerRangeField,
    image_upload_location,
    NameTimeStampBaseModel,
    Image,
    TimeStampBaseModel,
    get_image,
    create_slug,
    HTMLContentBaseModel,
    get_str
)
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.html import strip_tags


class BlogPost(HTMLContentBaseModel):

    title = models.CharField(max_length=180, blank=True, null=True)
    subtitle = models.CharField(max_length=180, blank=True, null=True)
    image = models.ForeignKey(Image, null=True, blank=True,
                              on_delete=models.SET_NULL,
                              related_name="blog_posts")
    content2 = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.SET_NULL,
                             related_name="blog_posts")


    def save(self, *args, **kwargs):
        self.slug = create_slug(self, self.title, BlogPost)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', args=(self.slug,))

    def __str__(self):
        return get_str(self.title)


class Comment(HTMLContentBaseModel):
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.SET_NULL,
                             related_name="comments")
    blog_post = models.ForeignKey(BlogPost, null=True, blank=True,
                             on_delete=models.SET_NULL,
                             related_name="comments")

    def save(self, *args, **kwargs):
        self.slug = create_slug(self, strip_tags(self.content), Comment)
        super().save(*args, **kwargs)


    def __str__(self):
       return get_str(self.content)



    
