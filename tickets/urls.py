from django.urls import path
import tickets.views as views

urlpatterns = [
    path('buy/<int:screening_id>/', views.buy, name='buy'),
    path('<int:ticket_id>/', views.ticket_page, name='ticket_page')
]
