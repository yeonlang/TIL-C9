from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()

# 1. Create
# post = Post(title='hello', content='world!')
# post.save()

# 2. Read

# 2.1 All
# posts = Post.objects.all() #반환되는 값이 리스트 형태(내부원소가 각각의 포스트)

# 2.2. Get one
# post = Post.objects.get(pk=1)#하나의 값만 반환

# 2.3 filter (WHERE)
# posts = Post.objects.filter(title='Hello').all()
# post = Post.objects.filter(title='Hello').first()

# 2.4 LIKE
# post = Post.objects.filter(title__contains='He').all()

# 2.5 order_by
# posts= Post.objects.order_by('title').all() #오름차순
# posts= Post.objects.order_by('-title').all() #내림차순

# 2.6 limit&offset
# Post.objects.all()[offset:limit+1]

# 3. Delete
# post = Post.objects.get(pk=2)
# post.delete()

# 4. Update
# post = Post.objects.get(pk=1)
# post.tile = 'hi'
# post.save()

# def throw
# def catch 

