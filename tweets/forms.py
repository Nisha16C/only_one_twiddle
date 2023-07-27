from django import forms

from .models import Tweet, Mention, Retweet


class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ('body', 'photo')
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Whats hapening ... '}),
            'photo': forms.ClearableFileInput(attrs={'multiple': False, 'id': 'tweet_photo'} ),
            }


class MentionForm(forms.ModelForm):

    class Meta:
        model = Mention
        fields = ('mention',)
        widgets = {'mention': forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Whats hapening ... '})}

class RetweetForm(forms.ModelForm):

    class Meta:
        model = Retweet
        fields = ('retweet',)
        widgets = {'retweet': forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Whats hapening ... '})}