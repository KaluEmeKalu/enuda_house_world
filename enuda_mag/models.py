from django.contrib.auth.models import User
from django.db import models
from . models_utils import (
    IntegerRangeField,
    image_upload_location,
    NameTimeStampBaseModel,
    Image,
    TimeStampBaseModel,
    get_image,
)
from tinymce.models import HTMLField


class BlogPost(TimeStampBaseModel):

    content = HTMLField(null=True, blank=True)
    title = models.CharField(max_length=180, blank=True, null=True)
    subtitle = models.CharField(max_length=180, blank=True, null=True)
    image = models.ForeignKey(Image, null=True, blank=True,
                              on_delete=models.SET_NULL,
                              related_name="blog_posts")
