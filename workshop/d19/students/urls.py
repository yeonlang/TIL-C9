from django.urls import path
from . import views
#.은 현재파일이 위치한 디렉토리

urlpatterns = [
    path('<int:student_id>/', views.detail),
    path('<int:student_id>/delete/', views.delete),
    path('<int:student_id>/edit/', views.edit),
    path('<int:student_id>/update/', views.update),
    path('create/', views.create),
    path('', views.index),
    path('new/', views.new),
]