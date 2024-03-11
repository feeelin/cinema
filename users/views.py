from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# App services
from users.services.update_user_profile import update_user_profile
from users.services.logout_user import logout_user
from users.services.login_user import login_user
from users.services.register_new_user import register_new_user
from tickets.services.get_user_tickets import get_user_tickets


@login_required(login_url='users:login')
def profile(request):
    if request.method == 'POST':
        return update_user_profile(user=request.user, data=request.POST)

    context = {
        'form': UserProfileForm(instance=request.user),
        'tickets': get_user_tickets(request.user),
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    return logout_user(request)


def login(request):
    if request.method == 'POST':
        return login_user(request)
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        return register_new_user(request)

    context = {'form': UserRegistrationForm()}

    return render(request, 'users/register.html', context)
