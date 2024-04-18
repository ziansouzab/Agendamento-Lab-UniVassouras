from django.shortcuts import render

def login(request):
    return render(request, 'professor/pages/login.html')
