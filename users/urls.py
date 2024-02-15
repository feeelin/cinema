from django.urls import path
import users.views as views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]
