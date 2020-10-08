from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


# User Registration Form
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)


# User Data Change Form
class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email',)


# User Login Form
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)