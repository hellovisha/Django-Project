from django import forms
from .models import UserTweet


class UserTweetForm(forms.ModelForm):
    class Meta:
        model = UserTweet
        Fields = ['text','photo']