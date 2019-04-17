from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    
#이름 정리
#class Post : Django - model , DB - Table
#즉 장고에서는 모델이지만 데이터베이스 개념에서는 테이블이다.
#마찬가지로 나머지도 다음과 같이 정의된다.
#post = Post() : Django - Instance or Object, DB - Record or Row
#title : Django - Field, DB - Column

#마이그레이션 (테이블과 데이터베이스 연동)

# CRUD

# 1. Create
#  방법 1
#  post = Post(title='hello-1')
#  post.save()

#  방법 2
#  post2 = Post.objects.create(title='hello-2')

#  방법 3
#  post = Post()
#  post.title = 'hello-1'
#  post.save()

# 2. Read
# 방법 1
# ALL
# posts = Post.objects.all()
# One
# post = Post.objects.get(pk=1) # id = 1, title = 'hello-1'도 가능
# 중복된다면 인덱스가 작은(id순) 값을 가져온다.

# 방법 2(views.py 한정)
# from django.shortcuts import get_objects_or_404
# post = get_objects_or_404(Post,pk = 1) # id = 1, title = 'hello-1'도 가능
# 중복된다면 인덱스가 작은(id순) 값을 가져온다.

# 방법 3(filter)
# post = Post.objects.filter(pk=1)[0]
# post = Post.objects.filter(pk=1).first()

# Post.objects -> 포스트의 모든 오브젝트
# Post.objects.filter(title='hello-1') -> 중 title에 필터적용한 오브젝트(query set)
# Post.objects.filter(title='hello-1').first() or [0] -> 처음 쿼리

# LIKE
# posts = Post.objects.filter(title_contains='lo') 

# 정렬
# Post.objects.order_by('title') # 오름차순
# Post.objects.order_by('-title') # 내림차순

# 쿼리셋의 자료구조
# Post.objects.all()
# <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>, <Post: Post object (3)>]>
# Post.objects.all()[0]
# <Post: Post object (1)>
# 이 구조는 사실 리스트의 인덱스 접근이 아니라 리미트와 오프셋을 이용한 처리이다.
# [0] = offset = 0 limit = 1 오프셋 없음 - 시작은 0부터 limit = 1 한개를 가져온다.
# [1] = offset = 1 limit = 1 offset = 1 - 시작은 1부터 limit = 1 한개를 가져온다.
# [1:3] = [offset: offset + limit]

# 3.Update
# post = Post.objects.get(pk=1)
# post.title = 'hello-5' # 데이터의 변경
# post.save() # 실제 데이터베이스에 반영

# 4.Delete
# post = Post.objects.get(pk=1)
# Post.objects.get(pk=1).delete()
