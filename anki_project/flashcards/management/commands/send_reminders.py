import os
from django.conf import settings
from django.core.management.base import BaseCommand
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flashcards.models import Flashcard

class Command(BaseCommand):
    help = 'Send daily email reminders to review flashcards'

    def handle(self, *args, **kwargs):
        flashcards = Flashcard.objects.all()
        subject = 'Daily Flashcard Review'
        message_content = 'Here are your flashcards to review:<br><br>'
        for flashcard in flashcards:
            message_content += f'<strong>Q:</strong> {flashcard.question}<br><strong>A:</strong> {flashcard.answer}<br><br>'
        
        message = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails='inetimimizzle@gmail.com',  # Replace with your email or recipient list
            subject=subject,
            html_content=message_content
        )
        
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            self.stdout.write(self.style.SUCCESS(f'Successfully sent email reminders. Status Code: {response.status_code}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))

