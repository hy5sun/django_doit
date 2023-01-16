from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-pk') #모든 Post 레코드 가져오기 / pk를 역순으로 정렬 (최신순)

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )