from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def new(request):
    return render(request, 'new.html')
    
def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    birthday = request.POST.get('birthday')
    age = request.POST.get('age')
    
    #DB insert
    student = Student(name=name, email=email, birthday=birthday, age=age)
    student.save()
    
    return redirect(f'/students/{student.pk}')
    
def detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    
    return render(request, 'detail.html', {'student':student})

def index(request):
    students = Student.objects.all()
    
    return render(request, 'index.html', {'students': students})    
    
def delete(request, student_id):
    student=Student.objects.get(pk=student_id)
    student.delete()
    return redirect('/students/')
    
def edit(request, student_id):
    student=Student.objects.get(pk=student_id)
    return render(request, 'edit.html', {'student':student})
    
def update(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.name=request.POST.get('name')
    student.email=request.POST.get('email')
    student.birthday=request.POST.get('birthday')
    student.age=request.POST.get('age')
    student.save()
        # 수정하는 코드
    return redirect(f'/students/{student_id}/')