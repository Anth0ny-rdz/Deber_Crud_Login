# myapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Item
from .forms import UserRegisterForm, ItemForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'myapp/register.html', {'form': form})

@login_required
def home(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'myapp/home.html', {'items': items})

@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, 'Item creado correctamente!')
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'myapp/item_form.html', {'form': form})

@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item actualizado correctamente!')
            return redirect('home')
    else:
        form = ItemForm(instance=item)
    return render(request, 'myapp/item_form.html', {'form': form})

@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk, user=request.user)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item eliminado correctamente!')
        return redirect('home')
    return render(request, 'myapp/item_confirm_delete.html', {'item': item})
