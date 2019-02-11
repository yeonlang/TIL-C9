from django.urls import path
from . import views

app_name = 'form_app'

urlpatterns=[
    path('create/', views.new, name='create'),
    path('', views.index , name='list'),
    # path('<int:article_id>/', views.detail, name='detail'),
    # path('<int:article_id>/edit', views.update, name='update'),
    ]
    