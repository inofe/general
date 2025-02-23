from django import forms
from .models import User

#This! is the proper form from a model
class UserForm(forms.ModelForm):
    name=forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'placeholder': 'your name sir'}))
    is_active=forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ['name', 'email', 'points']