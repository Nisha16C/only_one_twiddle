from django import forms

from .models import Tweet, Mention, retweet


class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ('body',)
        widgets = {'body': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Whats hapening ... '})}


class MentionForm(forms.ModelForm):

    class Meta:
        model = Mention
        fields = ('mention',)
        widgets = {'mention': forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Whats hapening ... '})}

class retweetForm(forms.ModelForm):

    class Meta:
        model = retweet
        fields = ('retweet',)
        widgets = {'retweet': forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Whats hapening ... '})}