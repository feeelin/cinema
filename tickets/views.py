from django.http import Http404
from django.shortcuts import render
from tickets.models import Ticket
from tickets.services.get_tickets_by_screening_id import get_tickets_by_screening_id
from tickets.services.save_users_tickets import save_users_tickets

# Create your views here


def buy(request, screening_id):
    if request.method == 'POST':
        return save_users_tickets(request, screening_id)

    context = {}
    context['tickets'], context['screening'] = get_tickets_by_screening_id(screening_id)

    return render(request, 'tickets/buy.html', context)


def ticket_page(request, ticket_id):
    ticket = Ticket.objects.select_related('screening').get(id=ticket_id)
    if request.user == ticket.user:
        context = {'ticket': ticket}
        return render(request, 'tickets/ticket_page.html', context)
    else:
        raise Http404('Билет не найден')
