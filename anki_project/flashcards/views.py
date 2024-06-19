from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Flashcard
from .forms import FlashcardForm

def flashcard_list(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'flashcards/flashcard_list.html', {'flashcards': flashcards})

def add_flashcard(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flashcard_list')
    else:
        form = FlashcardForm()
    return render(request, 'flashcards/add_flashcard.html', {'form': form})
