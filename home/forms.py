from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','description','imagelink']
# class PostUpdateForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     content = forms.Textarea()