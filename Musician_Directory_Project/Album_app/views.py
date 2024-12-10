from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album
from .forms import AlbumForm

# Create your views here.
class AddAlbum(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'Album_app/addAlbum.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        return super().form_valid(form)