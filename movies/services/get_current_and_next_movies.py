from movies.models import Movie
from django.utils import timezone


def get_current_and_next_movies():
    current_movies = Movie.objects.filter(start_of_rolling_date__lt=timezone.now(), end_of_rolling_date__gt=timezone.now()).order_by('start_of_rolling_date')
    next_movies = Movie.objects.filter(start_of_rolling_date__gt=timezone.now()).order_by('start_of_rolling_date')

    return current_movies, next_movies

