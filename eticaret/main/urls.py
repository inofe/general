from django.urls import path,include
from .views import index,dynamic_view,formView,get_data
from . import views

app_name = 'main'
urlpatterns = [
    path("", index, name="index"),
    path("dynamic",dynamic_view,name="dynamic"),
    path("form",formView,name="form"),
    path("get_data/",get_data,name="get_data"),
    #path("users/",views.users,name="users"),
    #path("users/user/<int:id>/",views.user,name="user"),
    path('users/', views.UserListView.as_view(), name='users'),
    path('users/user/<int:pk>/', views.UserDetailView.as_view(), name='user'),
    path('users/user/new/', views.UserCreateView.as_view(), name='user_new'),
    path('users/user/<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('users/user/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
]   