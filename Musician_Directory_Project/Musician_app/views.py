from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Musician
from .forms import MusicianForm


# Create your views here.

# class based view for adding musician.
class MusicianCreateView(LoginRequiredMixin, CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'Musician_app/addMusician.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add'
        return context

    def form_valid(self, form):
        return super().form_valid(form)
    
# class based view for updating musician.
class UpdateMusician(LoginRequiredMixin, UpdateView):
    model = Musician
    form_class = MusicianForm
    pk_url_kwarg = 'id'
    template_name = 'Musician_app/addMusician.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update'
        return context
