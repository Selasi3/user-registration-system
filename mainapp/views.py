from django.shortcuts import render
from .models import Person
# Create your views here.

def index(request):
    totalnumber = Person.objects.all().count();
    context = {
        "totalnumber":totalnumber
    }
    return render(request, 'index.html',context=context)

