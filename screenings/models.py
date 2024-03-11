from django.db import models
from django.utils import timezone

# Create your models here.


class Screening(models.Model):
    time: models.DateTimeField = models.DateTimeField(null=False, blank=False, default=timezone.now)
    price: models.IntegerField = models.IntegerField(null=False, blank=False, default=299)
    film_id: models.ForeignKey = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    hall: models.IntegerField = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.film_id} - {self.hall} зал - {self.time}'

