from django import forms
from .models import Comment

class Commentforms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'message', 'post']