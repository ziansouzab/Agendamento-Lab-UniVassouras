from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                   password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('agenda:agenda_view')
                else:
                    messages.error(request, 'Conta desabilitada')
            else:
                messages.error(request, 'Credenciais inválidas')
    else:
        form = LoginForm()
    return render(request, 'agenda/pages/login.html', {'form': form})


@login_required(login_url='agenda:user_login', redirect_field_name='next')
def logout_view(request):
    logout(request)
    messages.success(request, "Logout feito com sucesso!")
    return redirect('agenda:user_login')


@login_required(login_url='agenda:user_login', redirect_field_name='next')
def agenda_view(request):
    return render(request, 'agenda/pages/agenda.html')