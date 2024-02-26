from django.urls import path
import movies.views as views

urlpatterns = [
    path('', views.active_movies_list, name='index'),
    path('/movie/<int:movie_id>/', views.movie_page, name='movie_page')
]

