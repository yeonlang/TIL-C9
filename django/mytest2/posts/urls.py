from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:post_id>', views.detail),
    path('<int:post_id>/delete', views.delete),
    
]