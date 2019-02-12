from django.urls import path
from . import views
#.은 현재파일이 위치한 디렉토리

app_name='accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]