
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from mainapp.forms import PersonForm
from .models import Person
# Create your views here.

def index(request):
    totalnumber = Person.objects.all().count();
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
    