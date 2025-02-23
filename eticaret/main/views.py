from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import DetailView
from .models import User
from .forms import UserForm
from . import forms
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse

def index(request):
    if User.objects.count() > 0:
        pros={
            "users":User.objects.all()
        }
    else:
        pros={}
    return render(request, "main/index.html",pros)

def dynamic_view(request):
    

    if request.method == "POST":
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        pros={
            "name":name,
            "last_name":last_name
        }
       
        return render(request, "main/dynamic_content.html", pros)

    return render(request, "main/dynamic.html")


def get_data(request):
    data={"data": "very effective way of get data"}
    return render(request, "main/get_data.html", data)


#This! is the proper form view
def formView(request):
    form = UserForm(request.POST or None)
    form.fields['name'].widget.attrs.update({'placeholder': 'overrided placeholder'})
    if form.is_valid():
        # User.objects.create(**form.cleaned_data) gelen datadan obje olusturur
        form.save()
        form = UserForm()
    context = {
        "form": form
    }
    return render(request, "main/form.html", context)

"""
def users(request):
    users = User.objects.all()
    return render(request, "main/users.html", {"users": users})
    """ 
"""
def user(request,id):
    user = get_object_or_404(User, id=id)
    
    return render(request, "main/user.html", {"user": user})
"""

class UserListView(ListView):
    model = User
    template_name = "main/users.html"
    context_object_name = "users"
    
class UserDetailView(DetailView):
    model = User
    template_name = "main/user.html"
    context_object_name = "user"

class UserCreateView(CreateView):
    model = User
    form_class = forms.UserForm
    template_name = "main/form.html"
    success_url = "/users/"
    
class UserUpdateView(UpdateView):
    model = User
    form_class = forms.UserForm
    template_name = "main/form.html"
    success_url = "/users/"

class UserDeleteView(DeleteView):
    model = User
    template_name = "main/form.html"
    #success_url = "/users/"
    
    def get_success_url(self):
        return reverse("main:users")
    