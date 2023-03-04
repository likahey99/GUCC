from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password", "user_type",)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("image",)