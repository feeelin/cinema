from django.http import Http404
from django.shortcuts import render
from screenings.models import Screening
from tickets.models import Ticket
from tickets.services.ticketsCollector import TicketsCollector
from tickets.services.save_users_tickets import save_users_tickets

# Create your views here


def buy(request, screening_id):
    if request.method == 'POST':
        return save_users_tickets(request, screening_id)

    collector = TicketsCollector(screening_id)
    screening = Screening.objects.select_related('film_id').get(id=screening_id)

    context = {
        'tickets': collector.tickets,
        'screening': screening
    }

    return render(request, 'tickets/buy.html', context)


def ticket_page(request, ticket_id):
    ticket = Ticket.objects.select_related('screening').get(id=ticket_id)
    if request.user == ticket.user:
        context = {'ticket': ticket}
        return render(request, 'tickets/ticket_page.html', context)
    else:
        raise Http404('Билет не найден')
