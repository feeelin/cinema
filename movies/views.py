from django.shortcuts import render
from django.utils import timezone
from movies.models import Movie
from django.http import Http404

# Services
from movies.services.get_current_and_next_movies import get_current_and_next_movies


# Create your views here.

def active_movies_list(request):
    context = dict()
    context['current_movies'], context['next_movies'] = get_current_and_next_movies()
    return render(request, 'movies/active_list.html', context)


def movie_page(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    try:
        movie = Movie.objects.get(id=movie_id)
        return render(request, 'movies/movie_page.html', {'movie': movie})
    except Movie.DoesNotExist:
        raise Http404
