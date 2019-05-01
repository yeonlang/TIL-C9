from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForm
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# 원래 함수
# def list(request):
#     person = Person.objects.all()
#     return render(request, 'person_list.html',{'person':person})
class PersonList(ListView):
    model = Person
    context_object_name = 'person'
    
def create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person:list')
    else:
        form = PersonForm()
    return render(request, 'person/person_form.html',{'form':form})

class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    form_class = PersonForm
    success_url = '/person/'
    