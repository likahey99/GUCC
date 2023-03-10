from django import forms
from .models import User, UserProfile
from .models import Kit

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
#setting up the form
class KitForm(forms.ModelForm):
    NAME_MAX_LENGTH = 40
    name = forms.CharField(max_length=NAME_MAX_LENGTH)
    size = forms.IntegerField()
    colour = forms.CharField(max_length=20)
    brand = forms.CharField(max_length=20)
    type = forms.CharField(max_length=20)
    maintenance_problem = forms.CharField(max_length=20)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False) 

    class Meta:
        model = Kit

        exclude = ('owner',)