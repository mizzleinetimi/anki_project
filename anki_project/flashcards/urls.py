from django.urls import path
from . import views


urlpatterns = [
    path('', views.flashcard_list, name='flashcard_list'),
    path('add/', views.add_flashcard, name='add_flashcard'),
    path('edit/<int:pk>/', views.edit_flashcard, name='edit_flashcard'),
    path('delete/<int:pk>/', views.delete_flashcard, name='delete_flashcard'),
]