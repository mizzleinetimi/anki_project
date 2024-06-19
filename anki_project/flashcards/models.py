from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Flashcard(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_reviewed = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.question

