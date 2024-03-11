from django.db import models
from screenings.models import Screening
from users.models import User

# Create your models here.


class Ticket(models.Model):
    screening: models.ForeignKey = models.ForeignKey('screenings.Screening', on_delete=models.CASCADE)
    user: models.ForeignKey = models.ForeignKey('users.User', on_delete=models.CASCADE)
    row: models.IntegerField = models.IntegerField(null=False, blank=False)
    place: models.IntegerField = models.IntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.screening} {self.row} ряд {self.place} место'
