from django import forms 
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name' : forms.TextInput(attrs={'placeholder' : 'Album name'}),
            'album_release_date' : forms.DateInput(attrs={'type' : 'date'}),
            'album_name' : forms.TextInput(attrs={'placeholder' : 'Album name'}),
        }