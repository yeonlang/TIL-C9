from django.urls import path
from . import views
#.은 현재파일이 위치한 디렉토리

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('new/', views.new),
]