# myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Item

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['usuario', 'email', 'contraseña', 'contraseña1']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['Titulo', 'Descripción']
