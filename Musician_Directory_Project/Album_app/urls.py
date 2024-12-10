from django.urls import path,include
from .import views

urlpatterns = [
    path('add/', views.AddAlbum.as_view(), name='add_album'),
]