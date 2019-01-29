from django.urls import path
from . import views
#.은 현재파일이 위치한 디렉토리

urlpatterns = [
    path('<int:post_id>/', views.detail),
    path('', views.index),
    path('create/', views.create),
    path('new/', views.new),
    path('naver/<str:q>/', views.naver),
    path('github/<str:username>/', views.github),
    path('<int:post_id>/delete/', views.delete),
    path('<int:post_id>/edit/', views.edit),
    path('<int:post_id>/update/', views.update),
]