from django.urls import path
from . import views
#.은 현재파일이 위치한 디렉토리

app_name='posts'

urlpatterns = [
    # path('naver/<str:q>/', views.naver, name=''),
    # path('github/<str:username>/', views.github, name=''),
    path('', views.index, name='list'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('write/', views.new, name='new'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    # path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/<int:update>/', views.update, name='update'),
]