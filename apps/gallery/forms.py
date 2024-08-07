from django import forms

from . import models


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class AlbumForm(forms.ModelForm):
    files = MultipleFileField(label='Файлы', required=False)

    class Meta:
        model = models.Album
        fields = ['title', 'cover', 'is_visible', 'is_deleted']
        exclude = ['slug']


class AlbumContentForm(forms.ModelForm):
    files = MultipleFileField(label='Файлы')

    class Meta:
        model = models.AlbumContent
        fields = ['is_visible', 'is_deleted']
        exclude = ['slug', 'file', 'album', 'file_type']
