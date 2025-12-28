from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from accounts.forms import *
from accounts.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')

        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')

        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user: User = User.objects.filter(email=email).first()

            if user and user.check_password(password):
                login(request, user)
                messages.success(request, message='با موفقیت وارد شدید')
                return redirect('website:index')

            else:
                messages.error(request, message='کاربر با این مشخصات یافت نشد')

        return render(request, 'accounts/login.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        messages.success(request, 'با موفقیت خارج شدید')
        logout(request)
        return redirect('website:index')