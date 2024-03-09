from tickets.models import Ticket
from tickets.services.flatten import flatten


class TicketsCollector:
    def __init__(self, screening_id: int):
        self.screening_id = screening_id
        self.__tickets = {}

        for i in range(1, 11):
            self.__tickets[i] = []

    @property
    def tickets(self):
        for row in self.__tickets:
            places = list(flatten(Ticket.objects.filter(screening=self.screening_id, row=row).values_list('place')))
            for place in range(1, 16):
                if place in places:
                    self.__tickets[row].append((False, row, place))
                else:
                    self.__tickets[row].append((True, row, place))
        return self.__tickets


