from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import UserProfileForm


def update_user_profile(user, data):
    form = UserProfileForm(instance=user, data=data)

    if form.is_valid():
        form.save()

    return HttpResponseRedirect(reverse('users:profile'))
