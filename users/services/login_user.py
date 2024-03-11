from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm
from users.models import User
from django.conf import settings
import logging


def login_user(request):
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            _log_user_auth(user)
            return HttpResponseRedirect(reverse('users:profile'))
    messages.error(request, 'Пользователь не найден')
    return HttpResponseRedirect(reverse('users:login'))


def _log_user_auth(user: User) -> None:
    logging.basicConfig(level=logging.INFO, filename=settings.LOGS_ROOT / 'auth.log', filemode='w')
    logging.info(f'LOGIN {user.username} ID {user.id}')

