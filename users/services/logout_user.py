from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.services.auth_logging import log_auth, AuthLoggingAction


def logout_user(request) -> HttpResponseRedirect:
    log_auth(request.user, AuthLoggingAction.LOGOUT)
    auth.logout(request)
    messages.success(request, 'Вы вышли из аккаунта')
    return HttpResponseRedirect(reverse('users:login'))




