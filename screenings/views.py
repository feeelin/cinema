from django.shortcuts import render
from django.utils import timezone

from movies.models import Movie
from screenings.models import Screening
import itertools


# Create your views here.


def screenings_schedule(request):
    screenings = Screening.objects.order_by('time')
    screenings_time = list(set(map(lambda x: x[0].date(), screenings.values_list('time'))))

    context = {
        'screenings': screenings,
        'time': screenings_time
    }

    return render(request, 'screenings/schedule.html', context)


def movie_screenings_schedule(request, movie):
    movie = Movie.objects.get(pk=movie)
    screenings = Screening.objects.filter(film_id=movie.id).order_by('time')
    screenings_time = list(set(map(lambda x: x[0].date(), screenings.values_list('time'))))

    context = {
        'movie': movie,
        'screenings': screenings,
        'time': screenings_time
    }

    return render(request, 'screenings/movie_schedule.html', context)
