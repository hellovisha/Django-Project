from django import forms # type: ignore
from .models import UserTweet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserTweetForm(forms.ModelForm):
    class Meta:
        model = UserTweet
        fields = ['text','photo']



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')