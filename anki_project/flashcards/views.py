
from django.shortcuts import render, redirect, get_object_or_404
from .models import Flashcard
from .forms import FlashcardForm

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

def edit_flashcard(request, pk):
    flashcard = get_object_or_404(Flashcard, pk=pk)
    if request.method == 'POST':
        form = FlashcardForm(request.POST, instance=flashcard)
        if form.is_valid():
            form.save()
            return redirect('flashcard_list')
    else:
        form = FlashcardForm(instance=flashcard)
    return render(request, 'flashcards/edit_flashcard.html', {'form': form})

def delete_flashcard(request, pk):
    flashcard = get_object_or_404(Flashcard, pk=pk)
    if request.method == 'POST':
        flashcard.delete()
        return redirect('flashcard_list')
    return render(request, 'flashcards/delete_flashcard.html', {'flashcard': flashcard})