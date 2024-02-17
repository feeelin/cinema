from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='users:login')
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Вы вышли из аккаунта')
    return HttpResponseRedirect(reverse('users:login'))


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
