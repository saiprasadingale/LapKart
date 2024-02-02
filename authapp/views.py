from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


def register_view(request):
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('/seller/show/')

    template_name = 'authapp/register.html'
    signup_form = UserCreationForm()
    context = {'signup_form': signup_form}
    return render(request, template_name, context)


def login_view(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('/seller/show/')
        pass

    template_name = 'authapp/login.html'
    login_form = AuthenticationForm()
    context = {'login_form': login_form}
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('/auth/login/')
