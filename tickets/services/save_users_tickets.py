from django.http import HttpResponseRedirect
from django.urls import reverse
from screenings.models import Screening
from tickets.models import Ticket


def save_users_tickets(request, screening_id):
    for place in dict(request.POST)['place']:
        place = place.split(' ')
        ticket = Ticket(screening=Screening.objects.get(id=screening_id), place=place[1], row=place[0],
                        user=request.user)
        ticket.save()
    return HttpResponseRedirect(reverse('users:profile'))
