from django.shortcuts import render
from django.utils import timezone
from movies.models import Movie


# Create your views here.

def active_movies_list(request):
    current_movies = Movie.objects.filter(start_of_rolling_date__lt=timezone.now(), end_of_rolling_date__gt=timezone.now())
    next_movies = Movie.objects.filter(start_of_rolling_date__gt=timezone.now())
    context = {
        'current_movies': current_movies,
        'next_movies': next_movies,
    }
    return render(request, 'movies/active_list.html', context)
