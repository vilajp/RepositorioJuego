from django.shortcuts import render

# Create your views here.

def principal(request):
    return render(request, 'bootstrap/principal.html')

def postales(request):
    return render(request, 'bootstrap/postales.html')

def masinfo(request):
    return render(request, 'bootstrap/masinfo.html')

def equipo(request):
    return render(request, 'bootstrap/equipo.html')

def contacto(request):
    return render(request, 'bootstrap/contacto.html')

def detalle_portfolio(request):
    return render(request, 'bootstrap/portfolio-details.html')