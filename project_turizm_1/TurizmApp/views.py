from django.shortcuts import render


def index(request):
    return render(request, 'TurizmApp/index.html')

def test(request):
    return render(request, 'TurizmApp/test.html')


