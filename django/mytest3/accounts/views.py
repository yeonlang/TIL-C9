from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login , logout as auth_logout , get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ChangeForm

def list(request):
    return render(request, 'list.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:list')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('accounts:list')
    form  = UserCreationForm()
    return render(request, 'signup.html', {'form':form})
    
@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:list')
    
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:list')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('accounts:list')
            
    form = AuthenticationForm()
    return render(request, 'signup.html', {'form':form})

@login_required
def update(request):
    if request.method == 'POST':
        form = ChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:list')
            
    form = ChangeForm(instance = request.user)
    return render(request, 'signup.html', {'form':form})
    