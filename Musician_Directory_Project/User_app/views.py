from django.shortcuts import redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class UserRegister(CreateView):
    form_class = RegisterForm
    template_name = 'User_app/signUp.html'
    success_url = reverse_lazy('user_login')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home_page')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class UserLogin(LoginView):
    form_class = LoginForm
    template_name = 'User_app/login.html'
    success_url = reverse_lazy('home_page')
    redirect_authenticated_user = True

    def form_valid(self, form):
        return super().form_valid(form)
    

