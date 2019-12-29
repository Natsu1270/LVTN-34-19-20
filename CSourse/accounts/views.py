from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, SignInForm


def sign_up(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return reverse_lazy('')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def sign_in(request):
    form = SignInForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return reverse_lazy('')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signin.html', {'form': form})


def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
