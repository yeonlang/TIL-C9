from django.urls import path
from . import views
#.은 현재파일이 위치한 디렉토리

app_name='posts'

urlpatterns = [
    # path('naver/<str:q>/', views.naver, name=''),
    # path('github/<str:username>/', views.github, name=''),
    path('', views.index, name='list'),
    path('new/', views.new, name='new'), #GET #POST
    path('<int:post_id>/', views.detail, name='detail'), #GET
    # path('create/', views.create, name='create'), #GET(confirm), POST(view)
    path('<int:post_id>/delete/', views.delete, name='delete'), #GET(edit ), POST(update)
    path('<int:post_id>/edit/', views.edit, name='edit'),
    # path('<int:post_id>/<int:update>/', views.update, name='update'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
]