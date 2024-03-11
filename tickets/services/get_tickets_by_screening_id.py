from screenings.models import Screening
from tickets.models import Ticket
from tickets.services.get_flatten_collection_generator import get_flatten_collection_generator
from dataclasses import dataclass


@dataclass
class Place:
    is_taken: bool
    row: int
    place: int


class TicketsCollector:
    def __init__(self, screening_id: int):
        self.screening_id = screening_id
        self.__tickets = {}

        for i in range(1, 11):
            self.__tickets[i] = []

    @property
    def tickets(self) -> dict[int, list[Place]]:
        for row in self.__tickets:
            places = self.get_places_list(self.screening_id, row)
            self.__tickets[row] = [
                Place(is_taken=True if place in places else False, row=row, place=place) for place in range(1, 16)
            ]
        return self.__tickets

    @staticmethod
    def get_places_list(screening_id: int, row: int) -> list[int]:
        return list(
            get_flatten_collection_generator(
                Ticket.objects.filter(screening=screening_id, row=row).values_list('place')
            )
        )


def get_tickets_by_screening_id(screening_id: int) -> tuple[dict[int, list[Place]], list[Ticket]]:
    return TicketsCollector(screening_id).tickets, Screening.objects.select_related('film_id').get(id=screening_id)
