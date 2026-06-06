from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from blog.models import Category, Tag


def base_context():
    return {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
    }


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
            # auto-create profile for new user
            Profile.objects.get_or_create(user=user)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('posts')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})


def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    profile, _ = Profile.objects.get_or_create(user=profile_user)
    posts = profile_user.post_set.order_by('-created_at')

    context = base_context()
    context.update({
        'profile_user': profile_user,
        'profile': profile,
        'posts': posts,
        'is_own_profile': request.user == profile_user,
    })
    return render(request, 'users/profile.html', context)



@login_required
def edit_profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '').strip()
        request.user.last_name  = request.POST.get('last_name', '').strip()
        request.user.email      = request.POST.get('email', '').strip()
        request.user.save()

        profile.bio      = request.POST.get('bio', '').strip()
        profile.website  = request.POST.get('website', '').strip()
        profile.github   = request.POST.get('github', '').strip()
        profile.linkedin = request.POST.get('linkedin', '').strip()

        if request.FILES.get('image'):
            profile.image = request.FILES['image']

        profile.save()
        messages.success(request, 'Profile updated!')
        return redirect('profile', username=request.user.username)

    context = base_context()
    context['profile'] = profile
    return render(request, 'users/edit_profile.html', context)