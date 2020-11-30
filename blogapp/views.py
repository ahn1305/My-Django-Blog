from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
	blogapp = Post.objects.all()
	return render(request,"index.html",{'blogapp':blogapp})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def contact(request):
	return render(request,"contact.html")
	
def tutorial(request):
	return render(request,"Django.html")

