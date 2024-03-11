from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import UserRegistrationForm
from users.models import User
from users.services.auth_logging import log_auth, AuthLoggingAction


def register_new_user(request) -> HttpResponseRedirect:
    form = UserRegistrationForm(request.POST)

    if form.is_valid():
        form.save()
        log_auth(User.objects.get(username=form.username), AuthLoggingAction.REG)
        messages.success(request, 'Вы успешно зарегистрировались')
        return HttpResponseRedirect(reverse('users:login'))

    messages.error(request, 'Возникла ошибка')
    return HttpResponseRedirect(reverse('users:register'))




