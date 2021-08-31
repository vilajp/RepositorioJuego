from django.shortcuts import render, redirect

from .forms import RegistroFormulario

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():

            print(dir(form))
            print(form.cleaned_data)

            form.save()
            return redirect('login')
    else:
        form = RegistroFormulario()

    return render(request, 'registro.html', {'form':form})
