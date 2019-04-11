from django import forms
from .models import Post, comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content','image']
    
class CommentForm(forms.ModelForm):
    content = forms.CharField(label ="", widget=forms.TextInput(attrs={'class':'form-controll','placeholder':'댓글을작성하세요'}))
    class Meta:
        model = comment
        fields = ['content',]
        
        