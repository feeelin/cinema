from django.urls import path
import screenings.views as views

urlpatterns = [
    path('schedule/', views.screenings_schedule, name='schedule'),
    path('schedule/<int:movie>/', views.movie_screenings_schedule, name='film_schedule')
]

