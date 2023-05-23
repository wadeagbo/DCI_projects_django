from django import forms

# Create your models here.

class LoginForm(forms.Form):
    username = forms.CharField(label= "Username" , max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())