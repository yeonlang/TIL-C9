from django import forms
from .models import Post, comment, Image

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content',]
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file',]    
        
ImageFormSet = forms.inlineformset_factory(Post, Image, form=ImageForm, extra = 3)
    
class CommentForm(forms.ModelForm):
    content = forms.CharField(label ="", widget=forms.TextInput(attrs={'class':'form-controll','placeholder':'댓글을작성하세요'}))
    class Meta:
        model = comment
        fields = ['content',]
        
        