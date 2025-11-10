from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class signupForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class  Meta:
        model = User
        fields = ['username','email','password1','password2']

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))
