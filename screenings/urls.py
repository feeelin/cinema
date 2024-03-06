from django.urls import path
import screenings.views as views

urlpatterns = [
    path('schedule/', views.screenings_schedule, name='schedule')
]

