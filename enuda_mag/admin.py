from django.contrib import admin
from . import models


# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'timestamp', 'updated',
                    'image')


admin.site.register(models.BlogPost, BlogPostAdmin)
