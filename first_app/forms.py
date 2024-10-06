from django import forms
from first_app import models


class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    model = models.Album
    fields = '__all__'