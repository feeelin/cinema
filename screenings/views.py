from django.shortcuts import render

# App services
from screenings.services.get_valid_screenings_with_time import get_valid_screenings_with_time
from screenings.services.get_valid_screenings_with_time_by_movie import get_valid_movie_screenings_with_time


def screenings_schedule(request):

    screenings = get_valid_screenings_with_time()
    context = {
        'screenings': screenings.screenings,
        'time': screenings.screenings_time
    }

    return render(request, 'screenings/schedule.html', context)


def movie_screenings_schedule(request, movie):
    valid_screenings = get_valid_movie_screenings_with_time(movie)

    context = {
        'movie': valid_screenings.movie,
        'screenings': valid_screenings.screenings,
        'time': valid_screenings.screenings_time
    }

    return render(request, 'screenings/movie_schedule.html', context)
