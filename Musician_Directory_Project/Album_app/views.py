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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add'
        return context

    def form_valid(self, form):
        return super().form_valid(form)
    
class EditAlbum(UpdateView):
    model = Album
    form_class = AlbumForm
    pk_url_kwarg = 'id'
    template_name = 'Album_app/addAlbum.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update'
        return context

    def form_valid(self, form):
        return super().form_valid(form)
    
class DeleteAlbum(DeleteView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'Album_app/deleteAlbum.html'
    success_url = reverse_lazy('home_page')
    