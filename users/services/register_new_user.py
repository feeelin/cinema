from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import UserRegistrationForm


def register_new_user(request):
    form = UserRegistrationForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Вы успешно зарегистрировались')
        return HttpResponseRedirect(reverse('users:login'))