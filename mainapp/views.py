from django.shortcuts import render
from .models import Person
# Create your views here.

def index(request):
    totalnumber = Person.objects.all().count();
    totalmales = Person.objects.all().filter(gender="M").count()
    totalfemales = Person.objects.all().filter(gender="F").count()

    context = {
        "totalnumber":totalnumber,
        "totalmales": totalmales,
        "totalfemales": totalfemales


    }
    return render(request, 'index.html',context=context)

