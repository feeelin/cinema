from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import UserRegistrationForm
from users.models import User
from django.conf import settings
import logging


def register_new_user(request):
    form = UserRegistrationForm(request.POST)

    if form.is_valid():
        form.save()
        _log_user_registration(User.objects.get(username=form.username))
        messages.success(request, 'Вы успешно зарегистрировались')
        return HttpResponseRedirect(reverse('users:login'))

    messages.error(request, 'Возникла ошибка')
    return HttpResponseRedirect(reverse('users:register'))


def _log_user_registration(user: User) -> None:
    logging.basicConfig(level=logging.INFO, filename=settings.LOGS_ROOT / 'auth.log', filemode='w')
    logging.info(f'REGISTRATION {user.username} ID {user.id}')

