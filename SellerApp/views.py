from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LaptopForm
from .models import Laptop

@login_required(login_url='/auth/login/')
def add_laptop_view(request):
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    else:
        form = LaptopForm()

    template_name = 'SellerApp/add_laptop.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def show_laptop_view(request):
    template_name = 'SellerApp/show_laptop.html'
    laptop_objs = Laptop.objects.all()
    context = {'laptop_objs': laptop_objs}
    return render(request, template_name, context)


def update_laptop_view(request, id):
    lap_obj = Laptop.objects.get(id=id)
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=lap_obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    else:
        form = LaptopForm(instance=lap_obj)

    template_name = 'SellerApp/add_laptop.html'
    context = {'form': form}
    return render(request, template_name, context)


def delete_laptop_view(request, id):
    lap_obj = Laptop.objects.get(id=id)
    lap_obj.delete()
    return redirect('show_url')


