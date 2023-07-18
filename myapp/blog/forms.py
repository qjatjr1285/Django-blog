# blog/forms.py
from django import forms
from .models import Post, Comment, HashTag

# form () : html에 있는 form 태그
# django안에 form을 쓰는 이유는 유효성 검사를 하기 위해 쓴다.
# Model Form [] : model을 사용하는 form
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
        # fields = ('title', 'writer',)
        # widget = {
        #     'content': forms.widgets.Textarea
        # }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': '5', 'cols': '20'})
        }


class HashTagForm(forms.ModelForm):

    class Meta:
        model = HashTag
        fields = ['name']