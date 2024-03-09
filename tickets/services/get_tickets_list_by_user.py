from tickets.models import Ticket


def get_tickets_list_by_user(user):
    tickets = Ticket.objects.filter(user=user).select_related('screening', 'screening.movie_id')
    return tickets
