from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'alumnos/index.html')

def discos(request):
    context={}
    return render(request, 'alumnos/discos.html')