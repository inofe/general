# accounts/views.py
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import time


def home(request):
    return render(request, 'accounts/home.html')



def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Kullanıcıyı doğrulama
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Kullanıcıyı oturum açtır
            messages.success(request, 'Başarıyla giriş yaptınız!')
            return redirect('accounts:home')  # Başka bir sayfaya yönlendirme
        else:
            messages.error(request, 'Hatalı kullanıcı adı veya şifre.')
            
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect("accounts:home")


def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method== "POST":
        username= request.POST["username"]
        password=request.POST["password"]
        confirm_password=request.POST["confirm-password"]
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bu kullanıcı adı zaten alınmış.')
        elif password != confirm_password:
            messages.error(request, 'Şifreler eşleşmiyor.')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Başarıyla kayıt oldunuz!')
            return redirect('accounts:login')
    return render(request,"accounts/register.html")