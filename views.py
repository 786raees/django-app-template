from django.shortcuts import render


def home(request):
    return render('{{ app_name }}/home.html')