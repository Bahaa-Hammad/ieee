from django.urls import path
from . import views

urlpatterns = [
    path('<str:id>/', views.event, name="event"),
]
