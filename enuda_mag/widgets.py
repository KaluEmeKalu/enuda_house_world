from django import forms


class MediumEditorTextarea(forms.Textarea):
    class Media:
        js = (
            'bower_components/jquery/dist/jquery.min.js',
            'bower_components/medium-editor/dist/js/medium-editor.js',
            'js/mediumeditor/django-mediumeditor.js',
            )