from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()

    def __str__(self):
        return self.title
    
# Post : Comment = 1 : N
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    
    # on_delete 옵션
    # 1. CASCADE : 부모가 삭제되면, 자기 자신도 삭제.(ex: 게시글이 삭제되면 댓글도 삭제)
    # 2. PROTECT : 자식이 존재하면, 부모 삭제 불가능.
    # 3. 
 
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

