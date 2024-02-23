from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def logout_user(request):
    auth.logout(request)
    messages.success(request, 'Вы вышли из аккаунта')
    return HttpResponseRedirect(reverse('users:login'))
