from django.db import models

# Create your models here.


class Ticket(models.Model):
    screening = models.ForeignKey('screenings.Screening', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    row = models.IntegerField(null=False, blank=False)
    place = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.screening} {self.row} ряд {self.place} место'
