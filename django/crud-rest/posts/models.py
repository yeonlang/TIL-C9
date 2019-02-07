from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# ResizeToFill : 300,300 맞추고 넘치는 부분 잘라냄
# ResizeToFit : 300,300 맞추고 남는 부분을 빈 공간으로 둠

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    # image = models.ImageField(blank=True) #blank=True 는 빈값을 넣어도 가능
    
    created_at=models.DateTimeField(auto_now_add=True) # create 될 때, 딱 한번 현재 시간
    updated_at=models.DateTimeField(auto_now=True) # 변경이 될 때 마다, 현재시간
    image = ProcessedImageField(
            upload_to='posts/images', # 저장 위치
            processors=[ResizeToFill(300,300)], # 처리할 작업 목록
            format='JPEG', #저장 포맷 (확장자)
            options={'quality':90}, #저장 포맷 관련 옵션
        )

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

