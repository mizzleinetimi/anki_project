from django.urls import path
from . import views

urlpatterns = [
    path('', views.flashcard_list, name='flashcard_list'),
    path('add/', views.add_flashcard, name='add_flashcard'),
]
