from django.shortcuts import render
from mainapp.forms import news_form


def index(request):
    if request.method == 'POST':
        form = news_form(request.POST)
        if form.is_valid():

            # AI Model Proccessing Logic
            pass

    else:
        form = news_form()

    return render(request, 'mainapp/index.html', {'form': form})
