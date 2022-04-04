from django import forms
from .models import Article

class CommunityPost(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'content']
