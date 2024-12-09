from django import forms 
from .models import Musician

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        widgets = {
            'first_name' : forms.TextInput(attrs={'placeholeder' : 'First Name'}),
            'last_name' : forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email' : forms.EmailField(attrs={'palceholder' : 'Email'}),
            'phone' : forms.TextInput(attrs={'palceholder' : 'Phone number'}),
            'instrument' : forms.TextInput(attrs={'palceholder' : 'Instrument'}),
        }