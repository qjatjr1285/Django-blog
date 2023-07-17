from django.shortcuts import render
from django.views import View
from .models import Post

# Create your views here.

### Post
class Index(View):
    def get(self, request):
        post_objs = Post.objects.all()
        context = {
            "posts": post_objs,
            'title': 'Blog'
        }
        return render(request, 'blog/post_list.html', context)

