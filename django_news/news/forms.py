from turtle import title
from django import forms
from django.db.models import fields

from .models import Post, Tag, User

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))

class PostCreateForm(forms.ModelForm): #Поля для ввода статьи
    """Form definition for PostCreate."""
    class Meta:
        """Meta definition for PostCreateForm."""

        model = Post
        fields = ('title', 'text')

class TagCreateForm(forms.ModelForm):
    """Form definition for TagCreate."""

    class Meta:
        """Meta definition for TagCreateForm."""

        model = Tag
        fields = ('title','slug')

class TagForm(forms.Form):
    tags = forms.ChoiceField(widget=forms.Select, 
        choices=tuple(Tag.objects.values_list('id', 'title')))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
        widgets = {
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            'username' : forms.TextInput(attrs={'class': 'form-control', 'readonly': ''}),
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
        }
    