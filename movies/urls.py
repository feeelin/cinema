from django.urls import path
import movies.views as views

urlpatterns = [
    path('', views.active_movies_list, name='index')
]

