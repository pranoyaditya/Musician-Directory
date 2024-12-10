from django.urls import path,include
from .import views

urlpatterns = [
    path('add/', views.MusicianCreateView.as_view(), name='add_musician'),
    path('edit/', views.UpdateMusician.as_view(), name='edit_musician'),
]