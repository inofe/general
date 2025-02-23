# accounts/urls.py
from django.urls import path
from .views import user_login,home,user_logout,user_register

app_name="accounts"
urlpatterns = [
    path('', home, name='home'),
    path('register/', user_register, name='register'),
    path('login/', user_login , name='login'),
    path('logout/', user_logout, name='logout'),
]


