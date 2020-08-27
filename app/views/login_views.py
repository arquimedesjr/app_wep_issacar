from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def logar(request, template_name="login.html"):
    next = request.GET.get('next', '/index/')
    if request.method == "POST":
        username = request.POST['inputUser']
        password = request.POST['inputPassword']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)

        else:
            messages.error(request, 'Usuário ou senha informadas, estão incorretas.')
            return redirect('logar')
    else:
        if request.user.is_authenticated:
            return redirect('index')

    return render(request, template_name, {'redirect_to': next})


def deslogar(request):
    logout(request)
    return redirect('logar')
