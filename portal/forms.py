from portal.models import UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'password', 'email')


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('name', 'age', 'bodyweight', 'goals')





