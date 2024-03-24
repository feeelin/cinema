from dataclasses import dataclass

from django.utils import timezone

from movies.models import Movie
from screenings.models import Screening


@dataclass
class ValidMovieScreenings:
    movie: Movie
    screenings: list[Screening]
    screenings_time: list[str]


def get_valid_movie_screenings_with_time(movie_id: int) -> ValidMovieScreenings:
    movie = Movie.objects.get(pk=movie_id)
    screenings = Screening.objects.filter(film_id=movie.id).order_by('-time').filter(time__gt=timezone.now())
    screenings_time = list(set(map(lambda x: x[0].date(), screenings.values_list('time'))))

    return ValidMovieScreenings(movie=movie, screenings=screenings, screenings_time=screenings_time)
