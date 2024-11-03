from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from phone_field import PhoneField
from LoginApp.models import UserProfile 


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True) 
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileChange(UserChangeForm):
    email = forms.EmailField(label="Email Address", required=True)
    phone_number = PhoneField(blank=False, help_text='Contact Phone Number')
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic',]