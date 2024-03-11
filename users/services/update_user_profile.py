from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import UserProfileForm
from users.models import User


def update_user_profile(user: User, data: dict) -> HttpResponseRedirect:
    form = UserProfileForm(instance=user, data=data)

    if form.is_valid():
        form.save()

    return HttpResponseRedirect(reverse('users:profile'))
