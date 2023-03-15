from django import forms
from .models import User, UserProfile, Kit, Social

from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username", "email", "password", "confirm_password", "is_admin", "is_member")

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("passwords do not match")

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "is_admin", "is_member")

class PasswordUpdateForm(SetPasswordForm):
    class Meta:
        model = User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("picture",)

class PasswordResetForm(PasswordResetForm):
   def __init__(self, *args, **kwargs):
       super(PasswordResetForm, self).__init__(*args, **kwargs)


#for add_kit template
class KitForm(forms.ModelForm):

    class Meta:
        model = Kit
        exclude = ('maintenance_problem','slug', 'maintenance')


class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ("name", "date", "details", "location")
