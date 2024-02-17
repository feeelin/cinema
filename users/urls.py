from django.urls import path
import users.views as views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('register', views.register, name='register')
]
