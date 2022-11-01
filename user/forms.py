from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    mobile_phone = forms.CharField(max_length=11)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    profile_pic = forms.ImageField(required=False)
    facebook_url = forms.URLField(required=False)
    Birthdate = forms.DateField(required=False)
    country = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'mobile_phone', 'password1', 'password2']
