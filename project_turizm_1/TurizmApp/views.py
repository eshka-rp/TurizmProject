from dbm import error

from django.shortcuts import render
from .models import RegistrationModel
from .forms import RegistrationForm


def index(request):
    return render(request, 'TurizmApp/index.html')


def test(request):
    error = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Некорректное заполнение'

    reg = RegistrationModel.objects.all()
    form = RegistrationForm()

    data = {
        'form' : form,
        'error': error
    }

    return render(request, 'TurizmApp/test.html', data)

