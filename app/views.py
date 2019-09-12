from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm

# Create your views here.

def login(request):    
    if request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            dj_login(request, user)
            return redirect('/inicio')
    return render(request, 'usuarios/login.html')

def cadastro(request):
    form = RegistrationForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/cadastro')
    return render(request, 'usuarios/cadastro.html', context)

def inicio(request):
        return render(request, 'curriculum/inicio.html')
