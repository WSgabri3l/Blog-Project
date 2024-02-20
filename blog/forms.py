from django import forms

from .models import PostTitle, PostText

class PostTitleForm(forms.ModelForm):

    class Meta:

        model = PostTitle

        fields = ['post_title_text']
        labels = {'post_title_text' : ''}

class TextForm(forms.ModelForm):

    class Meta:

        model = PostText

        fields = ['text']
        labels = {'text' : ''}
        widgets = {'text' : forms.Textarea(attrs={'cols' : 80})}
        