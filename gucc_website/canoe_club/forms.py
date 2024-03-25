from PIL import Image
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import User, UserProfile, Kit, Social, Trip, Image, Upload

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


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ("name", "location", "date", "length", "members")

class ImageForm(forms.Form):
    class Meta:
        model = Image
        fields = ('image',)
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }


class ImageUploadForm(forms.Form):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('title', 'files',)
        widgets = {
            'files': forms.ClearableFileInput(attrs={'multiple': True}),
        }
