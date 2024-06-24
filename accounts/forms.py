from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fileds = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password']
        