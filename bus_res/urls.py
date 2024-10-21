from django.urls import path
from . import views
from .views import ticket_view
urlpatterns = [
    path('', views.booking, name='book'),
    path('booking/', views.booking, name='booking'),  # Correct path
    path('booking/ticket/', ticket_view, name='ticket'),
]


