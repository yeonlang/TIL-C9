from django.contrib import admin
from .models import Post

def __str(self):
    return self.title

# Register your models here.
admin.site.register(Post)