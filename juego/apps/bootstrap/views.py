from django.shortcuts import render

# Create your views here.

def principal(request):
    return render(request, 'bootstrap/principal.html')

def postales(request):
    return render(request, 'bootstrap/postales.html')
