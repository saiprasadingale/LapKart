from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('/seller/show/')
    else:
        signup_form = UserCreationForm()

    template_name = 'authapp/register.html'
    context = {'signup_form': signup_form}
    return render(request, template_name, context)

def login_view(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/seller/show/')
    else:
        login_form = AuthenticationForm()

    template_name = 'authapp/login.html'
    context = {'login_form': login_form}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('/auth/login/')
