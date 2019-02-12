from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

# Create your views here.
def new(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('form_app:list')
    
    else :
        form = StudentForm()
    
    return render(request, "new.html", {'form':form})
    
def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})