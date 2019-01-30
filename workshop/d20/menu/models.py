from django.db import models


class Question(models.Model):
    title=models.CharField(max_length=50)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    vote = models.IntegerField()
    