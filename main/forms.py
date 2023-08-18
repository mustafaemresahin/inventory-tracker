from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Inventory, Product, Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]



class Create(forms.ModelForm):
    class Meta:
        model  = Inventory
        fields = ["title", "description"]


class Add(forms.ModelForm):
    class Meta:
        model = Product
        
        fields = ["upc", "description", "count", "manufacturer", "price"]