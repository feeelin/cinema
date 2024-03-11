from django.conf import settings
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import logging
from users.models import User


def logout_user(request):
    _log_logout_user(request.user)
    auth.logout(request)
    messages.success(request, 'Вы вышли из аккаунта')
    return HttpResponseRedirect(reverse('users:login'))


def _log_logout_user(user: User) -> None:
    logging.basicConfig(level=logging.INFO, filename=settings.LOGS_ROOT / 'auth.log', filemode='a')
    logging.info(f'LOGOUT {user.username} ID {user.id}')

