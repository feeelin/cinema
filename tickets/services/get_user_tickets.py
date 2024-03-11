from typing import List

from tickets.models import Ticket
from users.models import User


def get_user_tickets(user: User) -> List[Ticket]:
    return Ticket.objects.filter(user=user).select_related('screening').order_by('-screening__time')
