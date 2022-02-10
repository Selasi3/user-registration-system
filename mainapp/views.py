
from itertools import count
from multiprocessing import context
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from mainapp.forms import PersonForm
from .models import Person
# Create your views here.

def index(request):
    totalnumber = Person.objects.all().count()
    totalmales = Person.objects.all().filter(gender="M").count()
    totalfemales = Person.objects.all().filter(gender="F").count()

    context = {
        "totalnumber":totalnumber,
        "totalmales": totalmales,
        "totalfemales": totalfemales,
    }
    return render(request, 'index.html',context=context)

def addPerson(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = PersonForm()
    return render(request, 'add.html', {'form':form})

def details(request):
    
    total_person = Person.objects.all()
    
    context = {
        "total_person": total_person,            
    }
    
    return render(request,'details.html',context=context)

def femaleList(request):
    females = Person.objects.all().filter(gender="F")

    context = {
        "females" : females
    }

    return render(request, 'femalelist.html', context=context)

def maleList(request):
    males = Person.objects.all().filter(gender="M")

    context = {
        "males" : males
    }

    return render(request, 'malelist.html', context=context)

def editPerson(request,id):
    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")

    form = PersonForm(request.POST, instance=person)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form = PersonForm(instance=person)
    context = {
        "person": person,
        "form":form
    }
    return render(request, 'edit.html', context=context)
    
def deletePerson(request, id):
    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    
    if request.method == "POST":
        person.delete()
        return HttpResponseRedirect(reverse('index'))
    return render(request, "delete.html")




