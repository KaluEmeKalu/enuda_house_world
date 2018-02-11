from django.contrib import admin
from . import models
from mediumeditor.admin import MediumEditorAdmin


# @admin.register(models.BlogPost)
# class MyModelAdmin(MediumEditorAdmin, admin.ModelAdmin):
#     mediumeditor_fields = ('my_text_field')


# Register your models here.
@admin.register(models.BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    # list_display = ('title', 'content', 'timestamp', 'updated',
    #                 'image')
    mediumeditor_fields = ('content')


# admin.site.register(models.BlogPost, BlogPostAdmin)
