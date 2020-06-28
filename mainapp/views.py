from django.shortcuts import render
from mainapp.forms import url_form


def index(request):
    if request.method == 'POST':
        form = url_form(request.POST)
        if form.is_valid():

            # AI Model Proccessing Logic
            pass

    else:
        form = url_form()

    return render(request, 'mainapp/index.html', {'form': form})
