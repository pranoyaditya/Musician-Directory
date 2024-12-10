from django.urls import path
from django.contrib.auth.views import LogoutView
from .import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('signup/', views.UserRegister.as_view(), name='sign_up'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
]