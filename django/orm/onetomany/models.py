from django.db import models
# Create your models here.

class User(models.Model):
    name = models.TextField()

class Post(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)




