from django.db import models
from django.utils import timezone

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=32, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    director = models.CharField(max_length=32, null=False, blank=False)
    genre = models.CharField(max_length=32, null=False, blank=False)
    duration = models.CharField(max_length=32, null=False, blank=False)
    age_restriction = models.IntegerField(default=0, null=False, blank=False)
    image = models.ImageField(upload_to='movies-images', null=False, blank=False)
    start_of_rolling_date = models.DateField(null=False, blank=False, default=timezone.now)
    end_of_rolling_date = models.DateField(null=False, blank=False, default=timezone.now)

    def __str__(self):
        return f'{self.title} - {self.director}'
