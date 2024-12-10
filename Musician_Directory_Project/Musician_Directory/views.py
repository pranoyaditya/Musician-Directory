from django.shortcuts import render
from django.views.generic import ListView
from Album_app.models import Album

class AlbumView(ListView):
    template_name = 'homePage.html'
    model = Album
    context_object_name = 'albums'