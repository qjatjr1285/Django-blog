from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
        # fields = ('title', 'writer',)
        # widget = {
        #     'content': forms.widgets.Textarea
        # }