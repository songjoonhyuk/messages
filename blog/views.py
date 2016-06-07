from django.shortcuts import render, redirect
from .models import Post
from blog.forms import PostForm
# Create your views here.

def index(request):
	post_list = Post.objects.all()
	return render(request, 'blog/index.html', {'post_list':post_list, })

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post, })

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save()
			return redirect('blog:post_detail', post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_new.html', {'form':form,})

def comment_new(request, post_pk):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = Post.objects.get(pk=post_pk)
			comment.save()
			return redirect('blog.views.post_detail', post_pk)
	else:
		form = CommentForm()
	return render(request, 'blog/comment_new.html', {'form':form})

