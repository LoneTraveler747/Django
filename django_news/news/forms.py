from django import forms
from django.db.models import fields

from .models import Post

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))

class PostCreateForm(forms.ModelForm): #Поля для ввода статьи
    """Form definition for PostCreate."""
    class Meta:
        """Meta definition for PostCreateForm."""

        model = Post
        fields = ('title', 'text')
