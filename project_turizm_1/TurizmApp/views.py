from django.shortcuts import render
from .models import RegistrationModel


def index(request):
    return render(request, 'TurizmApp/index.html')


def test(request):
    reg = RegistrationModel.objects.all()
    return render(request, 'TurizmApp/test.html', {'reg': reg})

