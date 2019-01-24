import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def dinner(request):
    menu = ["족발", "햄버거", "치킨", "초밥"]
    pick = random.choice(menu)
    return render(request, 'dinner.html', {'dinner': pick})
    
#Variable routing
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def throw(request):
    return render(request, 'throw.html')
    
def catch(request):
    message = request.GET.get('message')
    return render(request, 'catch.html', {'message': message})
    
def naver(request):
    return render(request, 'naver.html')
    
def bootstrap(request):
    return render(request, 'bootstrap.html')