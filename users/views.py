from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect('posts')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.POST.get('next') or 'posts')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('posts')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)        # auto login after register
            messages.success(request, 'Account created successfully!')
            return redirect('posts')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})