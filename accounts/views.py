from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('item-list')
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for { username }!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    # print('accounts/register.html\n')
    return render(request, "accounts/register.html", {'form': form})