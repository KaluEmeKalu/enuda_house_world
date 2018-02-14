from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db.models import (
    CharField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    ImageField,
    DecimalField,
    BooleanField,
    TextField,
    OneToOneField,
    ManyToManyField,
    FileField,
    Model,
    SlugField
)
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Transpose
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify


def get_str(field):
    if field:
        return field
    else:
        return 'Created on {}.'.format(
            self.get_date())


def create_slug(self, slug_field, model):
        max_length = self._meta.get_field('slug').max_length
        slug = slugify(slug_field)[:max_length]
        original = slug

        for x in range(1, 1000):
            if not model.objects.filter(slug=slug).exclude(id=self.id).exists():
                break

            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            new_max_length = max_length - len(str(x)) - 1
            short_slug = original[:new_max_length]
            slug = "{}-{}".format(short_slug, x)
        return slug

def get_image(self):
    if self.image:
        return self.image.image.url
    else:
        return "/static/enuda_mag/img/student.jpeg"


def image_upload_location(instance, filename):
    return "images/{}".format(filename)


class IntegerRangeField(IntegerField):
    def __init__(self, verbose_name=None, name=None,
                 min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class TimeStampBaseModel(Model):

    timestamp = DateTimeField(
        editable=False, auto_now_add=True, auto_now=False)
    updated = DateTimeField(auto_now=True, blank=True, null=True)
    slug = SlugField(default='', null=True, blank=True)

    def get_date(self):
        date = self.timestamp.strftime("%A, %d. %B %Y %I:%M%p")
        return date

    def time_ago(self):
        return naturaltime(self.timestamp)

    def __str__(self, name=None):
        """
        If model has name set that as name.

        If model has name or name set by subclass
            Then return that name
        Else return "Class_Name object #*number* cretaed on *date*"
        """

        if name:
            return name
        else:
            return "{} object #{} created on {}".format(
                self.__class__.__name__, self.id, self.timestamp
            )

    class Meta:
        abstract = True


class NameTimeStampBaseModel(Model):

    name = CharField(max_length=80, null=True, blank=True)
    timestamp = DateTimeField(
        editable=False, auto_now_add=True, auto_now=False)
    updated = DateTimeField(auto_now=True, blank=True, null=True)
    slug = SlugField(default='', null=True, blank=True)

    def get_date(self):
        date = self.timestamp.strftime("%A, %d. %B %Y %I:%M%p")
        return date


    def time_ago(self):
        return naturaltime(self.timestamp)

    def __str__(self, name=None):
        """
        If model has name set that as name.

        If model has name or name set by subclass
            Then return that name
        Else return "Class_Name object #*number* cretaed on *date*"
        """
        if self.name:
            name = self.name

        if name:
            return name
        else:
            return "{} object #{} created on {}".format(
                self.__class__.__name__, self.id, self.timestamp
            )

    class Meta:
        abstract = True


class HTMLContentBaseModel(Model):

    content = HTMLField(null=True, blank=True)
    timestamp = DateTimeField(
        editable=False, auto_now_add=True, auto_now=False)
    updated = DateTimeField(auto_now=True, blank=True, null=True)
    slug = SlugField(default='', null=True, blank=True)

    def get_date(self):
        date = self.timestamp.strftime("%A, %d. %B %Y %I:%M%p")
        return date


    def time_ago(self):
        return naturaltime(self.timestamp)

    def __str__(self, name=None):
        """
        If model has name set that as name.

        If model has name or name set by subclass
            Then return that name
        Else return "Class_Name object #*number* cretaed on *date*"
        """
        if self.name:
            name = self.name

        if name:
            return name
        else:
            return "{} object #{} created on {}".format(
                self.__class__.__name__, self.id, self.timestamp
            )

    class Meta:
        abstract = True

class Image(NameTimeStampBaseModel):
    # user = OneToOneField(User, related_name="image", null=True, blank=True)
    # content_object = GenericForeignKey('content_type', 'object_id')
    image = ProcessedImageField(processors=[  # ResizeToFill(
        # 100, 50),
        Transpose()],
        upload_to=image_upload_location,
        null=True,
        blank=True,
        format='JPEG',
        options={'quality': 60})
    mid_size = ImageSpecField(source='image',
                                      processors=[ResizeToFill(750, 450)],
                                      format='JPEG',
                                      options={'quality': 60})
    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(80, 80)],
                                      format='JPEG',
                                      options={'quality': 60})
    my_namespace = CharField(
        default="", max_length=128, null=True, blank=True)
    

    def get_timestamp(self, pretty=False):

        if pretty:
            return self.timestamp.strftime("%Y-%m-%d %H:%M:%S")

        return self.timestamp.strftime("%Y-%m-%d_%H:%M:%S")
