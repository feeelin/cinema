from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm
from users.services.auth_logging import log_auth, AuthLoggingAction


def login_user(request) -> HttpResponseRedirect:
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            log_auth(request.user, AuthLoggingAction.LOGIN)
            return HttpResponseRedirect(reverse('users:profile'))
    messages.error(request, 'Пользователь не найден')
    return HttpResponseRedirect(reverse('users:login'))




