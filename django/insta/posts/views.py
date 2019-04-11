from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST,require_http_methods
from .forms import PostForm, CommentForm
from .models import Post
from .models import comment as Comment


def list(request):
    posts = Post.objects.order_by('-id').all()
    comment_form = CommentForm()
    return render(request, 'posts/list.html', {'posts': posts ,'comment_form':comment_form}) 
# Create your views here.

@login_required
def create(request):
    if request.method == 'POST':
        post_form = PostForm(data=request.POST, files=request.FILES)    
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:list')
    else:
        post_form = PostForm()
    return render(request, 'posts/form.html', {'post_form': post_form })
    
@login_required
def comment_create(request, post_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id
        comment.save()
    return redirect('posts:list')


@login_required
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user != request.user:
        return redirect('posts:list')
    
    if request.method == 'POST':
        post_form = PostForm(data=request.POST, files=request.FILES, instance = post)    
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance = post)   
    return render(request,'posts/form.html', {'post_form':post_form} )

@login_required    
def delete(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    if post.user != request.user:
        return redirect('posts:list')
        
    post.delete()
    return redirect('posts:list')
    
@require_http_methods(['GET','POST'])
def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id = comment_id)
    post = get_object_or_404(Post, id = post_id)
    if post.user != request.user:
        return redirect('posts:list')
    comment.delete()
    return redirect('posts:list')
  
@login_required  
def like(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    if request.user in post.like_users.all():
        #좋아요 취소
        post.like_users.remove(request.user)
    else: 
        #좋아요
        post.like_users.add(request.user)
    return redirect('posts:list')